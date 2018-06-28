import csv
import os
from pprint import pprint

from eventbrite import Eventbrite


KEY_FILENAME = 'db_keys - Sheet1.csv'

# Get token from key file
with open(KEY_FILENAME) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
    	oath_token = row['Eventbrite']

eventbrite = Eventbrite(oath_token)

# Get user information
user = eventbrite.get('/users/me')
print(user)

# Get events information
events = eventbrite.get('/users/me/owned_events')
for event in events['events']:
    print(event['name']['text'], event['id'])

# Get information for an event
an_event = events['events'][0]
event_id = an_event['id']

# Get information for the specified event
event_info = eventbrite.get('/events/' + str(event_id))
pprint(event_info)
