#!/usr/bin/python3
"""
Enrichment: Range() | Author: Mike Greene
Script that will output all 99 lines of the song, '99 Bottles of Beer on the Wall'
"""

def main():
    # create a number for tracking the verses in the song
    num = 99

    # loop through 99 times, reducing the number through each verse
    for n in range(99):
        # check how many bottles are left to create proper grammar
        if(num == 1):
            print(f"{num} more bottle of beer on the wall! {num} more bottle of beer~! You take it down, pass it around,")
        elif(num == 0):
            print("No more bottles of beer on the wall.......DANGIT!")
        else:
            print(f"{num} bottles of beer on the wall! {num} bottles of beer~!\nYou take one down, pass it around,")
       
        # decrement the number
        num -= 1
        
        ## check how many bottles are left to change sentence for proper grammar
        if(num == 1):
            print(f"Only {num} more bottle of beer on the wall~!")
        elif(num == 0):
            print("No more bottles of beer on the wall~!")
        else:
            print(f"{num} bottles of beer on the wall~!")

if __name__ == "__main__":
    main()

