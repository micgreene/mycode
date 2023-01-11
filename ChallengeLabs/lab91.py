#!/usr/bin/env python3

import requests
import wget

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    # print out the URL to the front_default sprite for this pokemon
    img_url = pokeapi.get("sprites").get("front_default")
    print("Front_defualt sprite URL: " + img_url)
    wget.download(img_url, "../../static/")

    # looping through the pokemon's moves and printing each one
    for move in pokeapi.get("moves"):
        print(move["move"]["name"])

    # print out the count of how many games this pokemon has appeared in
    print(f"{pokeapi['name'].upper()} has appeared in {len(pokeapi['game_indices'])} Pokemon titles! ")

main()
