#!/usr/bin/env python3
# Alta3 Research || Author: Michael Greene
# Check hostname against expected value

# receive input from user
hostname = input("What value should we set for hostname?")

## use the .lower() method to ensure user doesn't have to match case sensitive data 
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
