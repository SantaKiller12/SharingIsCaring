import base64
import requests
import json
import os
import csv
from datetime import datetime, timedelta

def get_bearer_token(api_key, api_secret):
    url = "https://api.intelligence.mandiant.com/token"

    auth_token_bytes = f"{api_key}:{api_secret}".encode("ascii")
    base64_auth_token_bytes = base64.b64encode(auth_token_bytes)
    base64_auth_token = base64_auth_token_bytes.decode("ascii")

    headers = {
                 "Authorization": f"Basic {base64_auth_token}",
                      "Content-Type": "application/x-www-form-urlencoded",
                           "Accept": "application/json",
                                "X-App-Name": "insert app name"
                                    }

    params = {"grant_type": "client_credentials", "scope": ""}

    response = requests.post(url=url, headers=headers, data=params)
    response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx

    return response.json().get("access_token")

def write_to_file(access_token):
        # Get the current date
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Open the file in append mode, so it doesn't overwrite the existing contents
    with open('bearer.txt', 'w') as f:
                # Write the current date and access token to the file, separated by a newline
        f.write(f'{current_date}\n{access_token}\n')

def bearer_valid():
        # Open the file and read the first line
    with open('bearer.txt', 'r') as f:
                date_str = f.readline().strip()

    # Parse the date and time from the string
    date_time = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

    # Get the current date and time
    current_date_time = datetime.now()

    # Calculate the difference between the current date and time and the date and time from the file
    difference = current_date_time - date_time

    # If the difference is less than 12 hours, return True, otherwise return False
    return difference < timedelta(hours=12)

# Make request for CVE data and save it to a CSV file
def get_indicator_data(bearer_token):
    url = "https://api.intelligence.mandiant.com/v4/vulnerability"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Accept": "application/json",
        "X-App-Name": "",
        "Content-Type": "application/json"
    }

    # Load the CVEs from the file
    with open('CVE.txt', 'r') as f:
        cves = [line.strip() for line in f]

    for cve in cves:
        post_body = {
            "requests": [
                {
                    "values": [cve]
                }
            ]
        }

        params = None
        
        while True:
            resp = requests.post(url=url, headers=headers, data=json.dumps(post_body))
            if resp.status_code != 429:
                # If the status is not 429, break the loop
                break
            else:
                # If the status is 429, sleep for 10 seconds
                print('Sleeping for 10 seconds due to rate limit...')
                time.sleep(10)

        # Send the response to handle_csv
        handle_csv(resp.json())


# Adds data temporarily to a output.txt file and then calls CSV function
def handle_csv(resp):
        # Convert JSON data to text and write it to output.txt
    with open('output.txt', 'w') as f:
                f.write(json.dumps(resp, indent=4))

    # Create or append data to CSV
    create_csv()

# Creates the CSV file and calls the filter data function
def create_csv():
    # Load the queries
    with open('queries.txt', 'r') as f:
        queries = [line.strip() for line in f]

    # Create a dictionary to hold the data
    data = {query: '' for query in queries}

    # Go through each query
    for query in queries:
        # Go through each line in output.txt
        with open('output.txt', 'r') as f:
            for line in f:
                # If the line exists with the query
                if query in line:
                    # Split the line at the first ':'
                    parts = line.split(':', 1)
                    # If there is something after the ':'
                    if len(parts) > 1:
                        # Save everything after the ':' to the data dictionary, removing leading and trailing whitespace
                        data[query] = parts[1].strip()
                    break  # Stop iterating once a match is found

    # Open the CSV file for writing. If it already exists, append data; if not, create it.
    mode = 'a' if os.path.exists('format.csv') else 'w'

    # Write the data to a CSV file
    with open('format.csv', mode, newline='') as f:
        writer = csv.writer(f)
        # Write the header row if the file was just created
        if mode == 'w':
            writer.writerow(queries)
        # Write the data row
        writer.writerow([data[query] for query in queries])

def clean_csv_data():
    # Read data from the CSV file
    with open('format.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    # Clean up the data
    cleaned_data = []
    for row in data:
        cleaned_row = [entry[1:-2] if entry.startswith('"') and entry.endswith('",') else entry for entry in row]
        # Remove trailing comma from the end of the text within a cell
        cleaned_row = [entry[:-1] if entry.endswith(',') else entry for entry in cleaned_row]
        cleaned_data.append(cleaned_row)

    # Check if garbage.txt exists
    if os.path.exists('garbage.txt'):
        # Read data from garbage.txt
        with open('garbage.txt', 'r') as f:
            garbage_data = [line.strip() for line in f]

        # For each cell in cleaned_data, if it contains a string from garbage_data, replace that part of the cell with an empty string
        for i in range(len(cleaned_data)):
            for j in range(len(cleaned_data[i])):
                for garbage in garbage_data:
                    cleaned_data[i][j] = cleaned_data[i][j].replace(garbage, '')    

    # Write cleaned data back to the CSV file
    with open('format.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(cleaned_data)


#MAIN FUNCTION

# Check if the file exists and create it if it doesn't
if not os.path.exists('bearer.txt'):
    with open('bearer.txt', 'w') as f:
        f.write('2001-12-12 01:01:01\nxxxxx\n')

# Use your actual api_key and api_secret
api_key = ""
api_secret = ""

counter = "0"

if not bearer_valid():
    access_token = get_bearer_token(api_key, api_secret)
    write_to_file(access_token)

# Open the file and read the second line
with open('bearer.txt', 'r') as f:
    lines = f.readlines()
    if len(lines) > 1:
        access_token = lines[1].strip()

# Get the indicator data and have it saved to a CSV file
indicator_data = get_indicator_data(access_token)

clean_csv_data()

