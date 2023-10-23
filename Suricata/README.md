# Requirements
- VSCode
- Python extension

# Files
| File Name | Purpose |
| - | - |
| `iocList.csv` | The list of IOCs that are meant to be converted to Suricata rules<br>**NOTE:** This is an example file. It is not meant to be used |
| `main.py` | Main script that pulls all the IOCs from the `iocList.csv` file |
| `remove_dups.py` | Extra script to remove duplicate rules |
| `suricata_rules.rules` | The list of Suricata rules created by the `main.py` <br>**NOTE:** This is an example file. It is not meant to be used |


# Instructions

1. Use the `iocList.csv` template for listing the IOCs 
    1. The `main.py` will automatically ignore the first "header" row
    2. The first column is for the IOC
    3. Second column if for the type of IOC. The script accepts the following
    - IPV4
    - SHA256
    - FQDN
    - IPV4
    - URL
    4. The last column is for the actor/APT the IOC is related to
2. Run `main.py` to generate the `iocList.csv`
3. Run `remove_dups.py` to remove any duplicate lines that exist in the `iocList.csv`
