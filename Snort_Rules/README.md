# Snort Rule Creater

## Description

This tool will create a list of snort rules using iocdomains.txt and iocips.txt files. Files available are as follows:

- `base64PS.ps1` : This file is a basic script to base64 encode a given file
- `snort_script.sh` : This is the decoded version of the script that will create the snort rules
- `snort_scriptB64.txt` : The base64 encoded version of the script

## Setup

1. Copy the snort_scriptB64.txt contents and paste them into a blank file on the VM desktop.

Note: Make sure the `iocdomains.txt` and `iocips.txt` file are in the same location as the script. 

2. Decode the Base64 encoded script and output the file as a bash script

```bash
base64 -d snort_scriptB64.txt | tr -d '\r' > snort_script.sh && chmod +x snort_script.sh
```

3. Execute the script and output the files to a chosen file

```bash
./snort_script.sh >> rules.txt
```

4. Verify contents of `rules.txt`, and replace with new rules `/etc/nsm/rules/local.rules`
```bash
sudo snort -T -c rules.txt
```

```bash
sudo mv rules.txt /etc/nsm/rules/local.rules
```

5. Update rules

```bash 
sudo rule-update
```

6. Update rules on sensor

```bash
sudo rule-update
```

7. Edit `/etc/nsm/so-sensor-eth1/snort.conf`
Change the following: 
```
config checksum_mode: none
```

8. Replay contents on sensor

```bash
sudo tcpreplay -i eth1 --topspeed /path/to/your/file.pcap
```

## Other useful commands

### Check status
```
sudo sostat
```

### Check firewall on server (Note: Not 100% sure this helps anything...)

1. List firewall rules. If blocked, it should list it toward the top of the output
```
sudo iptables -L -n | less
```

2. Delete rules blocking IP
```
sudo iptables -D INPUT -s 10.10.10.7 -j DROP
```
```
sudo iptables -D FORWARD -s 10.10.10.7 -j DROP
```
