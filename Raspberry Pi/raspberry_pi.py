import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import googlemaps
from datetime import datetime

#
# Init API
#

cred = credentials.Certificate("Private Key/commuter-clock-firebase-adminsdk-q5p6m-d316723468.json")
firebase_admin.initialize_app(cred)

gmaps = googlemaps.Client(key='AIzaSyCnGQ5oITGwl8B9TJckesr5X__rCnJ3klI')

#
# Constants
#

# 1 for uptown, 0 for downtown, blank not listed
uptown_downtown_dictionary = {
    "Flatbush Av-Brooklyn College": 0,
    "Crown Hts-Utica Av": 0,
    "Woodlawn": 1,
    "Eastchester-Dyre Av": 1,
    "Wakefield-241 St": 1,
    "Van Cortlandt Park-242 St": 1,
    "North White Plains": 1,
    "Euclid Av": 0,
    "New Lots Av": 0,
    "96 St": 1,
    "145 St": 1,
    "168 St": 1,
    "Ozone Park-Lefferts Blvd": 0,
    "Brighton Beach": 0,
    "Coney Island-Stillwell Av": 0,
    "Bay Ridge-95 St": 0,
    "Far Rockaway-Mott Av": 0,
    "Church Av": 0,
    "Court Sq": 1,
    "Pelham Bay Park": 1,
    "Harlem - 148 St": 1,
    "Inwood-207 St": 1,
    "Astoria-Ditmars Blvd": 1,
    "Jamaica-179 St": 1,
}

#
# Functions
#

# 1 for uptown, 0 for downtown, -1 for blank
def check_uptown_downtown(headsign):
    if headsign in uptown_downtown_dictionary:
        return uptown_downtown_dictionary[headsign]
    return -1


user_id = open("user_id.txt", "r").read();
db = firestore.client()
doc_ref = db.collection(u'settings').document(user_id)
doc = doc_ref.get()

if doc.exists:
    doc_dictionary = doc.to_dict()

    wait_seconds = doc_dictionary['wait_seconds']
    destination = doc_dictionary['destination']
    origin = doc_dictionary['origin']
    start_hour = doc_dictionary['start_hour']
    end_hour = doc_dictionary['end_hour']
else:
    raise Exception("User ID does not exist")


def get_line_info():
    directions_result = gmaps.directions(origin, destination, mode="transit", departure_time=datetime.now(),
                                         alternatives=False)
    for leg in directions_result[0]['legs']:
        arrival_time_Unix = leg['arrival_time']['value']
        for step in leg['steps']:
            if step['travel_mode'] == 'TRANSIT':
                transit_details = step['transit_details']
                line = transit_details['line']
                if line['vehicle']['type'] == 'SUBWAY':
                    minutes = round(
                        (datetime.now() - datetime.fromtimestamp(arrival_time_Unix)).total_seconds() / 60.0);
                    direction = check_uptown_downtown(transit_details['headsign'])
                    return line['short_name'], direction, minutes


def update_motors():
    line_num, direction, minutes = get_line_info()
    pass
