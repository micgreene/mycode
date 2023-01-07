#!/usr/bin/python3
"""
Practice with Lists/Strings in Oython | Author: Mike Greene
some light practice manipulating output in python
"""

def main():
    mylist = [1,2,3,4,5, "Python"] # create a mixed type list

    name = input("What is your name?\n>") # ask user for name

    # This is what you should see when print runs:
    # Hi <name>! Welcome to Day 2 of Python Training!
    print("Hi ",name.upper(),"! Welcome to Day ",mylist[1]," of ",mylist[5]," Training!",sep="")

if __name__ == "__main__":
    main()
