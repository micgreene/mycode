#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import crayons
import requests
import pprint

AOIF_BOOK = "https://www.anapioficeandfire.com/api/books/"
AOIF_HOUSE = "https://www.anapioficeandfire.com/api/houses/"
AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)
        print("\n\n")
        # print some info on the character selected
        print(f"{crayons.blue('Name:')} \n{got_dj['name']}")

        # print out all allegiances this character has
        print(f"\n{crayons.red('Allegiances:')}")
        for ally in got_dj['allegiances']:
            ally = requests.get(ally).json() # response is a url, so call the api again
            pprint.pprint(ally['name']) # split name from response and print

        # print all books this character has appeared in
        print(f"\n{crayons.green('Novels Appeared In:')}")        
        for book in got_dj['books']:
            book = requests.get(book).json() # response is a url, so call api again
            pprint.pprint(book['name']) # split name from response and print 

if __name__ == "__main__":
        main()
