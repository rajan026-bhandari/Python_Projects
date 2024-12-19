import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Example phone number in E.164 format (replace with your own)
from myphone import number

# Parse the phone number
pepnumber = phonenumbers.parse(number)

# Get the general location of the phone number
location = geocoder.description_for_number(pepnumber, "en")
print("Location:", location)

# Get the carrier information
service_pro = carrier.name_for_number(pepnumber, "en")
print("Carrier:", service_pro)

# Use OpenCage to get coordinates for the location
key = '30d1ee1353ad4fef882e2e616a8e1b21'
geocoder = OpenCageGeocode(key)

query = str(location)
results = geocoder.geocode(query)

if results:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print("Latitude:", lat, "Longitude:", lng)

    # Create a map with the location
    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)

    # Save the map to an HTML file
    myMap.save('mylocation.html')
    print("Map saved as mylocation.html")
else:
    print("Error: Unable to get location coordinates from OpenCage.")