#!/usr/bin/python3
"""
Enrichment: Range() | Author: Mike Greene
Script that will output all 99 lines of the song, '99 Bottles of Beer on the Wall'
"""

def main():
    # instantiate num as 100 to keep user in while loop until they select a valid response
    num = str(100)

    # user must select a number under 100 to continue
    while(int(num) > 99):
        num = input("How many bottle should we sing for?: ")
        loop = int(num)
        counter = int(num)
        
        if(int(num) > 99):
            print("That's too many bottles! Select a number under 100!")

    # loop through `loop` times, reducing the number through each verse
    for n in range(loop):
        # check how many bottles are left to create proper grammar
        if(counter == 1):
            print(f"{counter} more bottle of beer on the wall! {counter} more bottle of beer~! You take it down, pass it around,")
        elif(counter == 0):
            print("No more bottles of beer on the wall.......DANGIT!")
        else:
            print(f"{counter} bottles of beer on the wall! {counter} bottles of beer~!\nYou take one down, pass it around,")
       
        # decrement the number
        counter -= 1
        
        ## check how many bottles are left to change sentence for proper grammar
        if(counter == 1):
            print(f"Only {counter} more bottle of beer on the wall~!")
        elif(counter == 0):
            print("No more bottles of beer on the wall~!")
        else:
            print(f"{counter} bottles of beer on the wall~!")

if __name__ == "__main__":
    main()

