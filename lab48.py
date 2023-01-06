#!/usr/bin/python3

try: # try to do this
    ## create booleans to track when data has been collected
    morality_selected = False
    conduct_selected = False
    
    ## Welcome user to program
    print('Welcome to the D&D Alignment Tool!')

    name = ""
    ## allow user to define their name
    while(name == ""):
        name = input('\nWhat\'s your name?: \n')

    job = ""
    ## collects user input
    while(job == ""):
        job = input('\n\nWhat is your JOB or CLASS? (i.e. Baker, Rogue, Knight, Lumberjack): \n')

    ## continues to loop until user has selected a valid character morality
    while(morality_selected == False):
        ## collects duser input
        morality = input('\n\nDo you conisder your self GOOD (virtuistic, selfless), EVIL (bad spirited, selfish), or NEUTRAL (you waver between these two) : \n')
        print('I see.')

        ## ensures user has selected a valid morality type, if not then ask for input again
        if(morality.lower() == 'good'):
            print(f'\nExcellent, a champion of {morality}!')
            morality_selected = True
        elif(morality.lower() == 'evil'):
            print(f'\nA dastardly-doer of {morality} appears!')
            morality_selected = True
        elif(morality.lower() == 'neutral'):
            print(f'\nA supporter of the winning side, ever {morality}')
            morality_selected = True
        else:
            print(f'\n{morality} is NOT a valid choice!')
    
    ## continues to loop until user has selected a valid conduct
    while(conduct_selected == False):
        ## collect user data
        conduct = input('\n\nHow would you consider your conduct?  GOOD (consistently law abiding, honorable), EVIL (acts outside the law, dishonest), or NEUTRAL (you act as you see fit for the situation)? : \n')
        print('Ah!')

        if(conduct.lower() == 'good'):
            print(f'\nA truly {conduct} citizen!')
            conduct_selected = True
        elif(conduct.lower() == 'evil'):
            print(f'\nLaws? Traditions? The inherently {conduct} only wish to witness the riseof themselves and the fall of others...')
            conduct_selected = True
        elif(conduct.lower() == 'neutral'):
            print(f'\nTo act as if in the thrall of thy own stream of consciousness, a {conduct} one, through and through.')
            conduct_selected = True
        else:
            print(f'\n{conduct} is NOT a valid choice!')
except: # if any errors occurred
    print('General error with obtaining user data.')
else: # if there were no errors
    print('\nAll paramters accepted.')
finally: # in all cases, print the user's selections
    if(morality.lower() == 'good' and conduct.lower() == 'good'):
        print(f'\n\nWelcome, {name}, the truly GOOD {job}! For the greater truths of this world we fight!')
    elif(morality.lower() == 'evil' and conduct.lower() == 'evil'):       
        print(f'\n\nWelcome, {name}, the pure EVIL {job}! Go and claim what is yours...')
    elif(morality.lower() == 'neutral' and conduct.lower() == 'neutral'):               
            print(f'\n\nWelcome, {name}, the TRUE NEUTRAL {job}! Captain Jack Sparrow himself would envy thy capriciousness!')
    else:
        print(f'\n\nWelcome, {name}, the {morality}/{conduct} {job}! Now venture forth to victory!')
