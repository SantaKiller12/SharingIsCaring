# Mandiant Script

## Description
This is a simple script meant to pull CVE data from Mandiant and organize it into an excel document. 
All that needs to be done to run the script is download all the `.txt` files. 
Then, go into the `main.py` and place your API keys into the respective variables at the bottom of the script. 

Below is a list of every file used and its purpose. 

## `CVE.txt`
Place all CVEs in this file, each sepearted with a new line character.

### Example:
```example
CVE-123-1234
CVE-123-1234
```

## `queries.txt`
Here are the different field values that are desired to be queried and placed into the excel documents. 
To query other data, look at the output in `output.txt` to see other fields that are available to query based on the output. 
Here are the defaults:
```default
cve_id
executive_summary
exploitation_consequence
observed_in_the_wild
```

## `garbage.txt`
In the output from Mandiant, it may contain characters that aren't desireable. Any info that is desired to be removed can be placed in here. Again, seperated by new line characters

### Example:
```example
<p>
</p>
```

## `output.txt`
This is a temporary file used by the script. Ignore it. 

## `bearer.txt`
This file is used to contain the Bearer Token that is used to access Mandiants API. Ignore it. 

## `format.csv`
This is the output of the script. If it already exists, it will append the new data to it. If it does not exist, the script will create it. 
> **NOTE:** It does not delete duplicates. 