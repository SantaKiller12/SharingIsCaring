1. Update system
```bash
sudo apt-get update
sudo apt-get upgrade -y
```
2. Install required dependencies. Not all of these are required. Look at their [walkthrough]([Installing Guacamole natively — Apache Guacamole Manual v1.5.2](https://guacamole.apache.org/doc/gug/installing-guacamole.html)) and verify which components you want
```bash
sudo apt install build-essential libcairo2-dev libjpeg-turbo8-dev libpng-dev libtool-bin libossp-uuid-dev libavcodec-dev libavutil-dev libswscale-dev freerdp2-dev libpango1.0-dev libssh2-1-dev libvncserver-dev libtelnet-dev libssl-dev libvorbis-dev libwebp-dev libavformat-dev libpulse-dev libwebsockets-dev -y
```
3. Use `wget` to download `guacamole-server.tar.gz` and `guacamole.war` [here]([Apache Guacamole™: Release Archive](https://guacamole.apache.org/releases/))
```bash
wget <url>
tar -xvf guacamole-server.tar.gz
```
4. Move to the `guacamole-server` folder and configure the file. After running the config file, be sure to install any missing [dependencies](https://guacamole.apache.org/doc/gug/installing-guacamole.html)
```bash
sudo ./configure --with-init-dir=/etc/init.d
sudo make
sudo make install
sudo ldconfig
# Verify and start/enable service
sudo systemctl daemon-reload
sudo systemctl status guacd.service
sudo systemctl enable guacd.service
sudo systemctl start guacd.service
``` 
4. Install `tomcat` and guacamole client (`guacamole.war`)
```bash
# old: sudo apt install tomcat9 tomcat9-admin tomcat9-common tomcat9-user -y
sudo apt install default-jdk tomcat9 tomcat9-admin tomcat9-user -y
sudo mv guacamole-1.3.0.war /var/lib/tomcat9/webapps/guacamole.war
sudo systemctl restart tomcat9
sudo systemctl enable tomcat9
```
5. Make configuration folders
```bash
sudo mkdir /etc/guacamole
```
6. Create config file `/etc/guacamole/guacamole.properties`
```
guacd-hostname: localhost
guacd-port:     4822
user-mapping:   /etc/guacamole/user-mapping.xml
auth-provider:  net.sourceforge.guacamole.net.basic.BasicFileAuthenticationProvider
```
7. Create the `/etc/guacamole/user-mapping.xml` file. Add in the password hash
```xml
<user-mapping>
    <authorize username="elevationstudnt" password="<insert hash>" encoding="md5">
        <connection name="UbuDesktop">
            <protocol>vnc</protocol>
            <param name="hostname">10.182.0.2</param>
            <param name="port">5901</param>
            <param name="password">password</param>
        </connection>

		<!-- Second connection for another monitor if wanted
		<connection name="UbuDesktop2">
            <protocol>vnc</protocol>
            <param name="hostname">10.182.0.2</param>
            <param name="port">5902</param>
            <param name="password">password</param>
        </connection>
		-->
    </authorize>
</user-mapping>
```
8. Link the Guacamole config files to `Tomcat9`'s directory
```bash
sudo ln -s /etc/guacamole /usr/share/tomcat9/.guacamole
```
9. Restart services
```bash
sudo systemctl restart guacd
sudo systemctl restart tomcat9
```
## Setup VNC with desktop startup
1. Install TightVNC, xfce4 GUI and copy/paste tool
```bash
sudo apt install tightvncserver xfce4 xfce4-goodies autocutsel -y
```
2. Set the password
```bash
vncpasswd
```
3. Start and kill the vncserver to create files
```bash
vncserver
vncserver -kill :1
```
4. Edit startup script for VNC at `$HOME/.vnc/xstartup` and add these contents:
```
autocutsel -fork
autcutsel -selection PRIMARY -fork
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
startxfce4 &
```
5. Start the service with the resolution and color depth
```bash
vncserver -geometry 1920x1080 -depth 16
# Hosting on the same system as Guac? Add `-localhost` option
```
6. To run at startup, create a service in `/etc/systemd/system/vncserver@1.service` 
```
[Unit]
Description=Start TightVNC server at startup for display :1
After=syslog.target network.target

[Service]
Type=forking
User=elevationstudnt
Group=elevationstudnt
WorkingDirectory=/home/elevationstudnt

PIDFile=/home/elevationstudnt/.vnc/%H:1.pid
ExecStartPre=/bin/sleep 30
ExecStart=/usr/bin/vncserver -geometry 1920x1080 -depth 16 :1
ExecStop=/usr/bin/vncserver -kill :1

[Install]
WantedBy=multi-user.target
```
7. Optional: If you want to be able to access the server on 2 different instances, add a second `vncserver@2.service` file. 
```
[Unit]
Description=Start TightVNC server at startup for display :2
After=syslog.target network.target

[Service]
Type=forking
User=elevationstudnt
Group=elevationstudnt
WorkingDirectory=/home/elevationstudnt

PIDFile=/home/elevationstudnt/.vnc/%H:2.pid
ExecStartPre=/bin/sleep 35
ExecStart=/usr/bin/vncserver -geometry 1920x1080 -depth 16 :2
ExecStop=/usr/bin/vncserver -kill :2

[Install]
WantedBy=multi-user.target
```
8. Enable the service
```bash
sudo systemctl daemon-reload
sudo systemctl enable vncserver@1.service
```

## Adding SSL over HTTPS

1. Create private key and the certificate signing request (CSR)
```bash
openssl req -newkey rsa:2048 -nodes -keyout server.key -out server.csr
```
2. Upload the CSR to the SSL certificate provider of your choosing and wait for approval. Then, download the `.pem` file
3. Convert the private key and the certificate to a PKCS12 keystore (CHANGE THE PASSWORD)
```bash
openssl pkcs12 -export -in server.pem -inkey server.key -out keystore.p12 -name tomcat
```
4. Move the `keystore.p12`
```bash
sudo mv keystore.p12 /etc/tomcat9/keystore.p12
```
5. Add the configuration info to `tomcat` in `/etc/tomcat9/server.xml` (update password to match in here)
```xml
<Connector port="80" protocol="HTTP/1.1"
		  connectionTimeout="20000"
		  redirectPort="443" />

<Connector port="443" protocol="org.apache.coyote.http11.Http11NioProtocol"
		   maxThreads="150" SSLEnabled="true">
	<SSLHostConfig>
		<Certificate certificateKeystoreFile="/etc/tomcat9/keystore.p12"
					 type="RSA" certificateKeystoreType="PKCS12"
					 certificateKeystorePassword="password" />
    </SSLHostConfig>
</Connector>
```
6. Restart services
```bash
sudo systemctl restart tomcat9
```

## Adding Two-Factor with Duo to Guac
1. Create a free duo account [Duo Security](https://duo.com/)
	1. After account creation, add a user
		1. Add phone number(s) to the user
	2. Add an application
		1. Search/choose `Web SDK`
		2. Take note of
		   - `Integration key`
		   - `Security key`
		   - `API hostname`
2. Generate a random key
```
pwgen 40 1
```
3. Edit `/etc/guacamole/guacamole.properties`
```
# Duo settings
duo-api-hostname: <your Duo API hostname>
duo-integration-key: <your Duo Client ID>
duo-secret-key: <your Duo Client Secret>
duo-application-key: <your randomly generated key from last step>
```
4. Download `guacmole-auth-duo.tar.gz`: [Apache Guacamole](https://guacamole.apache.org/releases/)
5. Place the `.jar` file from the downloaded file in the `/etc/guacamole/extensions`
6. Restart Guacamole
```
sudo systemctl restart guacamole
```

##  Troubleshooting

- Check firewall status
```bash
sudo ufw status
```
- Verify your IP from your ISP hasn't changed and if it has, update your DNS record
