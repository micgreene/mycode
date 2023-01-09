#!/usr/bin/env python3
"""
A script used to find your Chinese zodiac sign | Author: Mike Greene
Asks for name and date from user. Uses year of your birthdate to determine your zodiac sign
and outputting the results to the console.
"""
def main():
    """
    User input required for name and year of birth. Prints results to console
    """
    usr_name = input("Please enter your name:\n>").title() # ask for user's name
    usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
    sign= usr_date % 12 ## find which zodiac sign by determining the results:
                        # <user's birthdate year> % 12

    # a list of zodiac sign explanations
    zodiac= [
      "your zodiac sign is Monkey, you are sharp, smart, curious, and mischievious.",
      "your zodiac sign is Rooster, you are hardworking, resourceful, courageous, and talented.",
      "your zodiac sign is Dog, you are loyal, honest, cautious, and kind.",
      "your zodiac sign is Pig, you are a symbol of wealth, honesty, and practicality.",
      "your zodiac sign is Rat, you are artistic, sociable, industrious, charming, and intelligent.",
      "your zodiac sign is Ox, you are strong, thorough, determined, loyal, and reliable.",
      "your zodiac sign is Tiger, you are courageous, enthusiastic, confident, charismatic, and a leader.",
      "your zodiac sign is Rabbit, you are vigilant, witty, quick-minded, and ingenious.",
      "your zodiac sign is Dragon, you are talented, powerful, lucky, and successful.",
      "your zodiac sign is Snake, you are wise, like to work alone, and determined.",
      "your zodiac sign is Horse, you are animated, active, and energetic.",
      "your zodiac sign is Sheep, you are creative, resilient, gentle, mild-mannered, and shy."
    ]

    print(f"{usr_name}, {zodiac[sign]}") # prints the results

if __name__ == "__main__":
    main()
