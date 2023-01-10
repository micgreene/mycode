#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import crayons
import json
import os
import time

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]

      To Win:
        find the <key> and the <potion>
        escape through the <Garden>

      To Lose:
        find the <Monster>
    ''')
    time.sleep(2)
    input(crayons.blue("Press ENTER to continue"))
    print(crayons.red("\nEntering the Dungeon..."))
    time.sleep(2)

def showStatus():
    os.system('clear')
    """determine the current status of the player"""
    # print the player's current location
    print(crayons.yellow('---------------------------', bold=True))
    print('You are in the ' + currentRoom + '\n')
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print(crayons.green('- You see a ' + rooms[currentRoom]['item']))
    # print what the player is carrying
    print(crayons.blue(f'\n\nInventory: {", ".join(inventory)}'))
    print(crayons.yellow("---------------------------", bold=True))


# an inventory, which is initially empty
inventory = []

# loads a dictionary which acts as a map
with open("dungeon_map.json", "r") as map_file:
    rooms = json.load(map_file)


# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print(crayons.red('You can\'t go that way!', bold=True))
            time.sleep(1)

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(f'\nYou got the {crayons.magenta(move[1])}!\n\n')
            input(crayons.blue("Press ENTER to continue"))
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    
    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
    
    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

