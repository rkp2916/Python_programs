import json
import geopy
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from pprint import pprint
import operator


lis = []
#zipcode = raw_input("Enter the zipcode from Philadelphia:")
with open ('bikeStation.json') as j_data:
	bikeStation = json.load(j_data)
for i in bikeStation["features"]:
                lis.append((i["properties"]["name"]))
                lis.append((i["properties"]["addressZipCode"]))
                lis.append((i["geometry"]["coordinates"][0],i["geometry"]["coordinates"][1]))
#print lis
		

zipcode = raw_input("enter the zipcode:")                
geolocator = Nominatim()
location = geolocator.geocode(zipcode)
print location
lis1= {}
for i in bikeStation["features"]:
        if zipcode == i["properties"]["addressZipCode"]:
                distance = vincenty((location.latitude,location.longitude),(i["geometry"]["coordinates"][1],i["geometry"]["coordinates"][0]))
                lis1[str(i["properties"]["name"])] = str(distance)
        #else:
         #       print "no zipcode found"
sorted_lis = sorted(lis1.items(), key = operator.itemgetter(1))

for i in sorted_lis:
        print i
