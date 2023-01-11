#!/usr/bin/python3
"""
Practice using Python requests | Author: Mike Greene
Allows user to provide dates to retrieve near earth object information from that time period.
"""

import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    start_date_input = input("Enter a start date: ")
    end_date_input = input("Enter an end date within 7 days (optional): ")

    startdate = f"start_date={start_date_input}"
    end_date = f"end_date={end_date_input}"

    # make a request with the request library
    if len( end_date ) > 0: # use an end date if user provided one
        neowrequest = requests.get(NEOURL + startdate + "&" + end_date + "&" + nasacreds)
        print("end date found")
    else: # if not, use just the start date
        neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)
        print("no end date found")

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()
