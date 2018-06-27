import os

from eventbrite import Eventbrite

# FIRST MUST SET THE EVENTBRITE TOKEN TO ENVIRONMENTAL VARIABLE
oath_token = os.environ['OAUTH_TOKEN']

eventbrite = Eventbrite(oath_token)

# Get user information
user = eventbrite.get('/users/me')
print(user)

# Get events information
events = eventbrite.get('/users/me/owned_events')
print(events)

# TODO Get event id from list of events
event_id = 0

# Get information for specific event
event = eventbrite.get('/events/' + str(event_id))
print(event)
