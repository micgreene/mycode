0#!/usr/bin/env python3
## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    
    ## each item of the list now has the "\n" characters back
    print(configlist)
    ## print the number of lines inside vlaconfig.cfg
    print("Number of lines: ",len(configlist))

## file was just auto closed (no more indenting)

