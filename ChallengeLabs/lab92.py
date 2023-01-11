#!/usr/bin/env python3
"""
ISS Coordinates Code | Author: Mike Greene
Returns the location of the ISS in latitude/longitude coordinates
"""
import requests
import datetime
import reverse_geocoder as rg

# URI for ISS locations api
api = "http://api.open-notify.org/iss-now.json"

def main():
    ## everything in main function

    # make the call
    resp = requests.get(api).json()

    # splice out coordinates from response
    lat = resp["iss_position"]["latitude"]
    lon = resp["iss_position"]["longitude"]
    coords = (lat, lon)

    # use coords to search for physical location from reverse geocoder api
    loc_data = rg.search(coords)

    # print coords, physical location, and current timestamp
    print(f"Current coordinates of the ISS: \nLat<{lat}> / Lon<{lon}>\n{loc_data[0]['name']}, {loc_data[0]['admin2']}, {loc_data[0]['admin1']}, {loc_data[0]['cc']}") # parse out location data

    print(f"Timestamp: {datetime.datetime.fromtimestamp(resp['timestamp'])}") # use datetime api to convert Epoch time to normal date-time-group

if __name__ == "__main__":
    main()

