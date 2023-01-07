#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginsuccess = 0 # counter for successes

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1

            # print the IP address of the failed attempts
            print("Failed attempt associated with IP Address: ", line.split(" ")[-1])
        
        # if the success pattern appears in the line...
        if "-] Authorization failed" in line:
            loginsuccess += 1 # this increments loginsuccess

print("The number of failed log in attempts is", loginfail) # print number of fails
print("The number of successful log in attempts is", loginsuccess) # print successes
