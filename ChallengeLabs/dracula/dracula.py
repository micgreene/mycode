#!/usr/bin/python3
"""
Dracula Looping Exercise | Author: Mike Greene
A script which uses a text file of Bram Stoker's Dracula for data manipulation
"""


def main():
    # create a text file to log lines later
    vampire_log = open("vampytime.txt", "w")

    # open the text file
    with open("dracula.txt", "r") as dracula:
        dracula_lines = dracula.readlines() # send lines to a list
        
        vampire_counter = 0 # count the number of times "vampire" appears in the text
        
        ## loop through each line of the book
        for line in dracula_lines:
            if("vampire" in line.lower()): # checks for vampire in any case
                print(line) # print lines that feature the word 'vampire"
                print(line, file=vampire_log) # write vampire lines to log file
                vampire_counter += 1 # increment the vampire counter

        # print how many times vampire was counted
        print("The word 'vampire' is written: ", vampire_counter, " times!")
        
    # close the log file
    vampire_log.close()

if __name__ == "__main__":
    main()
