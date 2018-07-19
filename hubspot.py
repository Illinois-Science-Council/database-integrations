import csv
import json
import os

from urllib.request import urlopen
from pprint import pprint


API_BASE_URL = 'https://api.hubapi.com'
KEY_FILENAME = 'db_keys - Sheet1.csv'


def get_hubspot_data(resource):
    '''Given the resource URL returns a Python dictionary from the JSON'''
    resource.strip('/')
    with urlopen(API_BASE_URL + resource + '?hapikey=' + oath_token) as response:
        data = json.load(response)
    return data


# Get token from key file
with open(KEY_FILENAME) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
    	oath_token = row['Hubspot']

contacts = get_hubspot_data('/contacts/v1/lists/all/contacts/all/')

# Get a particular contact ID from contacts
for contact in contacts['contacts']:
    if contact['properties']['firstname'] == 'Spencer':
        pprint(contact)
        contact_id = contact['vid']

# Get contact info for a particular contact ID
contact_info = get_hubspot_data('/contacts/v1/contact/vid/{}/profile'.format('2401'))
pprint(contact_info)





