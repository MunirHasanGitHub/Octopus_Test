import os
import requests
import json
import csv


#list to be used to sort the data
outages_list = [] 
sorted_outages_list = []
filtered_sorted_outages_list = []
site_id_outage_info = []
site_id_outage_id =[]
site_outage_full_info_list = []

##### Part 1 - get all the outage data
# URL for the outage data
api_url_outage = "https://api.krakenflex.systems/interview-tests-mock-api/v1/outages"

# Retrieve API key from environment variables
api_key = os.getenv('API_KEY')

# Set up the headers with the API key
headers = {
    'Content-Type': 'application/json',
    'X-API-Key': api_key
}

# Make a GET request to the get Outage Data
response = requests.get(api_url_outage, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # store the JSON data of all the outaged
    data = response.json()
    print('Data retrieved successfully:')
    #print(data)

    # Open a file to write CSV data
    with open('outages_output.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Extract headers from the outage data
        csv_headers = data[0].keys()
        writer.writerow(csv_headers)

        # Write out data rows in the list and copy of the data to a csv file
        for item in data:
            writer.writerow(item.values())
            outages_list.append(item)

#an error in the GET request, record the error code
else:
    print(f'Failed to retrieve data. Status code: {response.status_code}')
    print('Response:', response.text)

#sort the outage data into ascending data order
sorted_outages_list = sorted(outages_list, key=lambda item: item['begin'])

#only put the outage if it occurs after 2022-01-01T00:00:00.000Z
filtered_sorted_outages_list = [start for start in sorted_outages_list if start['begin'] > '2022-01-01T00:00:00.000Z']


##### Part 2 - get site information

site_id = "norwich-pear-tree"
url_site_id = "https://api.krakenflex.systems/interview-tests-mock-api/v1/site-info/norwich-pear-tree"

header = {
    'Content-Type': 'application/json',
    'X-API-Key': api_key
}

# Make a GET request to the API
response_data = requests.get(url_site_is, headers=header)

# Check if the request was successful
if response_data.status_code == 200:
    # get the JSON data
    site_data = response_data.json()
    print('Data retrieved successfully:')
    print(site_data)

    # Open a file to write CSV data
    with open('norwich_site_outage_output.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write site data into a list and into the csv file
        for item in site_data['devices']:
            writer.writerow(item.values())
            site_id_outage_info.append(item)
        
#print(site_id_outage_info)

##### Part 3 - populate the side id with the outage times

# got through each of the devices on the site
for item in norwich_site_outage_info:

    # check if the device id from the site is in the list of outages
    for data in filtered_sorted_outages_list:

        # if there is a match add the site info device and time of the outage
        if item["id"] == data["id"]:
            entry = {"id": item["id"], "name": item["name"], "begin": data["begin"], "end": data["end"]}
            site_outage_full_info_list.append(entry)

#print(site_outage_full_info_list)


# Post the data to the site outage URL
post_url = "https://api.krakenflex.systems/interview-tests-mock-api/v1/site-outages/norwich-pear-tree"

# Headers including the x-api-key
post_headers = {
    'X-API-Key': api_key
}

post_data = site_outage_full_info_list

# POST the full outage data
post_url = "https://api.krakenflex.systems/interview-tests-mock-api/v1/site-outages/norwich-pear-tree"

# Set up the headers with the API key
post_headers = {
    'Content-Type': 'application/json',
    'X-API-Key': api_key,
    'Accept': '*/*',
    'Connection': 'keep-alive'
}

post_data = site_outage_full_info_list

# Make the POST request
response = requests.post(url=post_url, headers=post_headers, json=post_data)

print(f'Status Code: {response.status_code}')
response_json = response.json()
print('Response JSON:', response_json)
