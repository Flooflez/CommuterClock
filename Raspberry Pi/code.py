import firebase_admin
from firebase_admin import credentials
import googlemaps
from datetime import datetime





#cred = credentials.Certificate("path/to/serviceAccountKey.json")
#firebase_admin.initialize_app(cred)

gmaps = googlemaps.Client(key='AIzaSyCnGQ5oITGwl8B9TJckesr5X__rCnJ3klI')
now = datetime.now()
directions_result = gmaps.directions("89 E 42nd St, New York, NY 10017", "City Hall Park, New York, NY 10007",mode="transit",departure_time=now, alternatives=True)
print(directions_result)

