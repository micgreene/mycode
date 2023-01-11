#!/usr/bin/env python3
"""
Trivia API| Author: Mike Greene
Returning Data from Complex JSON Using an API
"""

import crayons
import random
import requests
import html

# api url for trivia
api = "https://opentdb.com/api.php?amount=3&category=15&difficulty=medium&type=multiple"

def main():
    ## all content in main function

    # data will be a python dictionary rendered from response JSON
    data = requests.get(api).json()
    
    # print the questions and their answers
    for trivia in data['results']: # iterate through each question returned
        print(crayons.yellow('\n\n------------------------------------------------------'))
        print(f"{crayons.blue(html.unescape(trivia['question']))}") # parse out html chars
        print(crayons.yellow('------------------------------------------------------'))

        print("\nIs it...")
        counter = 1 # create a counter to number the responses

        # create a list of answers
        answers = trivia['incorrect_answers']
        answers.append(trivia['correct_answer'] + '  <---------')

        # loop through the list of answers and print them randomly 
        while len(answers) > 0: # while there are items in the list continue
            i = random.randint(0, len(answers) - 1) # grab a random number from the index list
            answer = answers.pop(i) # remove the item at the random index
            print(f"{counter}) {crayons.green(answer)}")
            counter += 1 # increment the counter

if __name__ == "__main__":
    main()
