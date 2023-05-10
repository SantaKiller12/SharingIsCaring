#!/bin/bash

# Place this script on your desktop with both the iocdomains.txt and iocips.txt

SID=1000001

# Generate rules for domains
while IFS= read -r line
do
    domain=$(echo "$line" | tr -d '\n\r')
    echo "alert ip any any <> any any (msg:\"Bad DNS ${domain}\"; pcre:\"/${domain}/im\"; sid:${SID};)"
    ((SID++))
done < iocdomains.txt

# Generate rules for IPs
while IFS= read -r line
do
    ip=$(echo "$line" | tr -d '\n\r')
    echo "alert ip ${ip} any <> any any (msg:\"Bad IP ${ip}\"; sid:${SID};)"
    ((SID++))
done < iocips.txt