import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import googlemaps
from datetime import datetime

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

def get_user_id():
    reader = open("user_id.txt", "r")
    user_id = reader.read();
    reader.close()
    return user_id


# 1 for uptown, 0 for downtown, -1 for blank
def check_uptown_downtown(headsign):
    if headsign in uptown_downtown_dictionary:
        return uptown_downtown_dictionary[headsign]
    return -1


def get_line_info(origin, destination, gmaps):
    directions_result = gmaps.directions(origin, destination, mode="transit", departure_time=datetime.now(),
                                         alternatives=False)
    for leg in directions_result[0]['legs']:
        for step in leg['steps']:
            if step['travel_mode'] == 'TRANSIT':
                transit_details = step['transit_details']
                line = transit_details['line']
                if line['vehicle']['type'] == 'SUBWAY':
                    arrival_time_Unix = leg['arrival_time']['value']
                    minutes = round(
                        ((datetime.fromtimestamp(arrival_time_Unix) - datetime.now()).total_seconds()) / 60.0);
                    direction = check_uptown_downtown(transit_details['headsign'])
                    return line['short_name'], direction, minutes


def get_car_info(origin, destination, gmaps):
    directions_result = gmaps.directions(origin, destination, mode="driving", departure_time=datetime.now(),
                                         alternatives=False)
    duration_time_seconds = directions_result[0]['legs'][0]['duration']['value'];
    traffic_duration_time_seconds = directions_result[0]['legs'][0]['duration_in_traffic']['value'];
    minutes = round(max(duration_time_seconds,traffic_duration_time_seconds)/60)

    return minutes;


def update_display(origin, destination, gmaps, should_consider_car):
    line_num, direction, minutes = get_line_info(origin, destination, gmaps)
    if should_consider_car:
        car_minutes = get_car_info(origin, destination, gmaps)
        if car_minutes < minutes:
            print("Car, Minutes:", minutes)
    else:
        print(line_num, "Train, Direction:", direction, ", Minutes:", minutes)


def get_document_data(user_id):
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
        should_consider_car = doc_dictionary['should_consider_car']

        return wait_seconds, destination, origin, start_hour, end_hour, should_consider_car
    else:
        raise Exception("User ID does not exist")


#
# Init API
#
def main():
    cred = credentials.Certificate("Private Key/commuter-clock-firebase-adminsdk-q5p6m-d316723468.json")
    firebase_admin.initialize_app(cred)

    gmaps = googlemaps.Client(key='AIzaSyCnGQ5oITGwl8B9TJckesr5X__rCnJ3klI')

    user_id = get_user_id()
    print(user_id)
    wait_seconds, destination, origin, start_hour, end_hour, should_consider_car = get_document_data(user_id)

    print(get_car_info(origin, destination, gmaps));

    # insert loop:
    # check button press
    # get_document_data
    # update_display(origin, destination, gmaps, should_consider_car)
    # DO NOT CALL update_display UNLESS NECESSARY.
    # wait

    # Tasks:
    # check delay/sudden line/time change
    # check if driving faster


main()
