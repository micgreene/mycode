#!/usr/bin/env python3

# create a mixed list
my_list = [ "192.168.0.5", 5060, "UP" ]

# print each index in the list, converting the port number to a string 
print("The first item in the list (IP): " + my_list[0] )
print("The second item in the list (port): " + str(my_list[1]) )
print("The last item in the list (state): " + my_list[2] )

# list for lab 30 challenge 01
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]


# printing only IP addresses from `iplist`
print(f"IP Addresses from iplist:  {iplist[3]}, {iplist[4]}")

