import time

import firebase_admin
from google.cloud import firestore
from firebase_admin import credentials
from firebase_admin import firestore
import googlemaps
from datetime import datetime, timedelta

import sched

import RPi.GPIO as GPIO

# Motor Controller Python Script
import motor_controller

#
# Constants
#

# 1 for uptown, 0 for downtown, blank not listed (returns 2)
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
# Global Vars
#

global wait_seconds, destination, origin, start_hour, end_hour, should_consider_car, user_id
global start_time, end_time  # parsed from strings
global next_update_time
gmaps = googlemaps.Client(key='AIzaSyCnGQ5oITGwl8B9TJckesr5X__rCnJ3klI')
cred = credentials.Certificate("Private Key/commuter-clock-firebase-adminsdk-q5p6m-d316723468.json")
firebase_admin.initialize_app(cred)
scheduler = sched.scheduler(time.time, time.sleep)

button_pin = 4 #can be changed

#
# Functions
#

# Reads user id from user_id.txt and returns it as string
def get_user_id():
    reader = open("user_id.txt", "r")
    global user_id
    user_id = reader.read();
    reader.close()
    return user_id


# Given a headsign, returns the direction
# 1 for uptown, 0 for downtown, 2 for blank
def check_uptown_downtown(headsign):
    if headsign in uptown_downtown_dictionary:
        return uptown_downtown_dictionary[headsign]
    return 2


# Reads the public variables origin and destination
# Returns line information in the form of line number/letter, direction number, minutes
def get_line_info():
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

# returns how many minutes it will take to destination there by car
def get_car_info():
    directions_result = gmaps.directions(origin, destination, mode="driving", departure_time=datetime.now(),
                                         alternatives=False)
    duration_time_seconds = directions_result[0]['legs'][0]['duration']['value'];
    traffic_duration_time_seconds = directions_result[0]['legs'][0]['duration_in_traffic']['value'];
    minutes = round(max(duration_time_seconds, traffic_duration_time_seconds) / 60)

    return minutes

# will get the routing information and update the motors
def update_display():
    #DEBUG ONLY
    print("Spin the thing", datetime.now().time())
#     return #DEBUG ONLY

    line_num, direction, minutes = get_line_info()
    if should_consider_car:
        car_minutes = get_car_info()
        if car_minutes < minutes:
            print("Car, Minutes:", minutes)
            
            #motor controller update to show car
            motor_controller.update_car(minutes)
            
    else:
        print(line_num, "Train, Direction:", direction, ", Minutes:", minutes)
        
        #motor controller update to show train
        motor_controller.update_train(line_num, direction, minutes)
        
        

# makes a firebase call to get all variables
# saves them to global variables
def get_document_data():
    db = firestore.client()
    doc_ref = db.collection(u'settings').document(user_id)
    doc = doc_ref.get()

    if doc.exists:
        global wait_seconds, destination, origin, start_hour, end_hour, should_consider_car, start_time, end_time, next_update_time
        doc_dictionary = doc.to_dict()
        wait_seconds = int(doc_dictionary['wait_seconds'])
        destination = doc_dictionary['destination']
        origin = doc_dictionary['origin']
        start_hour = doc_dictionary['start_hour']
        end_hour = doc_dictionary['end_hour']
        should_consider_car = doc_dictionary['should_consider_car']
        
        start_time_time = datetime.strptime(start_hour, '%H:%M')
        end_time_time = datetime.strptime(end_hour, '%H:%M')

        start_time = datetime.now().replace(hour=start_time_time.hour, minute=start_time_time.minute, second=0, microsecond=0)
        end_time = datetime.now().replace(hour=end_time_time.hour, minute=end_time_time.minute, second=0, microsecond=0)
        
        print("Start time/End time:", start_time.time(), end_time.time())
        
        if datetime.now() > start_time:
            next_update_time = datetime.now()
        else:
            next_update_time = start_time
    else:
        raise Exception("User ID does not exist")


# called when the sync button is pressed, updates the user data variables
# also restarts all scheduled events
def sync_button_pressed():
    #print("Resetting display...")
    #reset_all() #ENABLE WHEN INTEGRATING
    
    print("Syncing...")

    get_document_data()
    
    print("Syncing complete.")


#
# GPIO Init
#
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#
# MAIN
#

def main():
    global user_id, next_update_time, end_time, start_time
    user_id = get_user_id()
    get_document_data()
    
    print("Start time/End time:\n", start_time,"\n" ,end_time)
    print("next update:",next_update_time.time())
    
    try:
        while True:
            if GPIO.input(button_pin) == GPIO.HIGH:
                sync_button_pressed()
                time.sleep(3)
            elif datetime.now() >= next_update_time:
                update_display()
                if datetime.now() < end_time: #still updating today
                    next_update_time += timedelta(seconds=wait_seconds)
                    
                else: #past end time, set next_update_time for tomorrow
                    start_time += timedelta(1) #add one day
                    end_time += timedelta(1) #add one day
                    next_update_time = start_time
                    reset_all()
                print("next update:",next_update_time.time())
            else:
                time.sleep(5) #sleep for 5 seconds.
                        
    except KeyboardInterrupt:
        print("Program ended with ctrl+C")
        #reset all motors
        motor_controller.reset_all()
        motor_controller.clean_pins()
        

    print("done")

    # Tasks:
    # check delay/sudden line/time change?

# call main
main()
