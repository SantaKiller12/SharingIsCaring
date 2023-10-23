import csv

def rule_md5(hash: str, sid: int, actor: str):
    return f'alert http any any -> any any (msg:"{actor}: FILE MD5 match for malicious file"; filemd5:{hash}; sid:{sid}; rev:1;)'

def rule_sha256(hash: str, sid: int, actor: str):
    return f'alert http any any -> any any (msg:"{actor}: FILE SHA-256 match for malicious file"; filesha256:{hash}; sid:{sid}; rev:1;)'

def rule_fqdn(fqdn: str, sid: int, actor: str):
    return f'alert dns any any -> any any (msg:"{actor}: Malicious FQDN detected"; dns.query; content:"{fqdn}"; sid:{sid}; rev:1;)'

def rule_ipv4_src(ip: str, sid: int, actor: str):
    return f'alert ip {ip} any -> any any (msg:"{actor}: Malicious source IP detected"; sid:{sid}; rev:1;)'

def rule_ipv4_dst(ip: str, sid: int, actor: str):
    return f'alert ip any any -> {ip} any (msg:"{actor}: Malicious destination IP detected"; sid:{sid}; rev:1;)'

def rule_url(url: str, sid: int, actor: str):
    return f'alert http any any -> any any (msg:"{actor}: Malicious URL detected"; http.uri; content:"{url}"; sid:{sid}; rev:1;)'

def generate_rules(csv_filename: str, start_sid: int = 1000000):
    sid = start_sid
    with open(csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        with open('suricata_rules.rules', 'w') as f:
            for row in reader:
                ioc, ioc_type, actor = row
                rule = None

                if ioc_type == 'MD5':
                    rule = rule_md5(ioc, sid, actor)
                elif ioc_type == 'SHA-256':
                    rule = rule_sha256(ioc, sid, actor)
                elif ioc_type == 'FQDN':
                    rule = rule_fqdn(ioc, sid, actor)
                elif ioc_type == 'IPV4':
                    rule_src = rule_ipv4_src(ioc, sid, actor)
                    f.write(rule_src + '\n')
                    sid += 1
                    rule_dst = rule_ipv4_dst(ioc, sid, actor)
                    f.write(rule_dst + '\n')
                    sid += 1
                    continue
                elif ioc_type == 'URL':
                    rule = rule_url(ioc, sid, actor)

                if rule:
                    f.write(rule + '\n')
                    sid += 1

generate_rules('iocList.csv')
