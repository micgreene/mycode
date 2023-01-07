#!/usr/bin/python3
"""
Looping with For | Author: Mike Greene
Practice using the python for loop
"""
## 3 lists which we will use for the code block inside main()

# creating a list of farm dicts
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

# creating a list of all non-animal products for Challenge 3
non_animals = ["carrots", "celery", "bananas", "apples", "oranges"]

# creating a list of all farm names for validating user info easily
farm_names = []
for farm in farms:
    farm_names.append(farm["name"].lower())

## There are 3 sections of code challenges, described below
def main():
    
    # 1) a loop that returns all animals from the NE farm!
    print("Challenge 1: NE Farm's Animals ")
    for animal in farms[0]["agriculture"]:
        print(animal, end=" ") # prints all results on same line

    
    # 2) ask the user to choose a farm, then return the agriculture from that farm
    print("\n\nChallenge 2: User Selects a Farm\n")
    
    # prints a list of farms for the user to choose from
    for farm in farms:
        print(farm["name"], end=" ") # prints all results on same line

    # create a boolean to track when the user makes a valid selection
    valid_farm = False
    
    ## continue to loop until user makes a valid choice
    while(valid_farm == False):
        user_farm1 = input("\nSelect a farm from the list: ") # user selects a farm

        # checks the list of valid farm names
        if(user_farm1.lower() not in farm_names):
            print(f"This is not a valid choice - {user_farm1}")
        else: # if a valid selection is made then exit the loop
            valid_farm = True

    ## once a valid selection is made by the user, loop through the farms
    for farm in farms:
        # if a farm name matches the user choice, then print out its "agriculture"
        if(farm["name"].lower() == user_farm1.lower()):
            for agr in farm["agriculture"]:
                print(agr, sep=" ") # print each item on the same line

    
    # 3) ask the user to choose a farm, but only return 5the animals
    print("\n\nChallenge 3: User Selects a Farm, only return the ANIMALS\n")
    
    # loop through the farms and print each name so the user knows what their choices are
    for farm in farms:
        print(farm["name"], end=" ")
    
    # reset to False to begin new loop
    valid_farm = False

    ## continue to loop until user makes a valid choice
    while(valid_farm == False):
        user_farm1 = input("\nSelect a farm from the list: ") # user slects a farm

        # checks the list of valid farm names
        if(user_farm1.lower() not in farm_names):
            print(f"This is not a valid choice - {user_farm1}")
        else: # if a valid selection is made then exit the loop
            valid_farm = True
    
    # after a valid choice is made, loop through the farms again
    for farm in farms:
        # if a matching farm is found
        if(farm["name"].lower() == user_farm1.lower()):
            for agr in farm["agriculture"]: # loop through the farm's "agriculture"
                if(agr not in non_animals): # not print items in the non_animals list
                    print(agr, sep=" ")

if __name__ == "__main__":
    main()
