# Snort Rule Creater

## Description

This tool will create a list of snort rules using iocdomains.txt and iocips.txt files. Files available are as follows:

- base64PS.ps1 : This file is a basic script to base64 encode a given file
- snort_script.sh : This is the decoded version of the script that will create the snort rules
- snort_scriptB64.txt : The base64 encoded version of the script

## Setup

1. Copy the snort_scriptB64.txt contents and paste them into a blank file on the VM desktop.

Note: Make sure the `iocdomains.txt` and `iocips.txt` file are in the same location as the script. 

2. Decode the Base64 encoded script and output the file as a bash script

```bash
base64 -d snort_scriptB64.txt | tr -d '\r' > snort_script.sh && chmod +x snort_script.sh
```

3. Execute the script and output the files to a chosen directory

```bash
./snort_script.sh >> /etc/nsm/rules/local.rules
```

4. Update rules

```bash
sudo rule-update
```