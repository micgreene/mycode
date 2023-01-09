#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Creating a simple dice program utilizing classes."""


# imports from cheadice.py (this is in the local directory)
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice
from cheatdice import Cheat_Force_Reroll

def main():
    """run-time code"""

    # create two cheater objects
    cheater1 = Cheat_Swapper() # ability is to change 3rd dice roll to 6
    cheater2 = Cheat_Loaded_Dice() # increase all rolls by +1 provided they are < 6
    cheater3 = Cheat_Force_Reroll() # forces other players to reroll their 6's
    
    # all players take turns
    cheater1.roll()
    cheater2.roll()
    cheater3.roll()

    # all players use their cheat methods
    cheater1.cheat()
    cheater2.cheat()
    cheater3.cheat(cheater1)
    cheater3.cheat(cheater2)

    print(f"Cheater 1 rolled {cheater1.get_dice()}")
    print(f"Cheater 2 rolled {cheater2.get_dice()}")
    print(f"Cheater 3 rolled {cheater3.get_dice()}")

    if sum(cheater1.get_dice()) == sum(cheater2.get_dice()) and sum(cheater2.get_dice()) ==sum(cheater3.get_dice() ):
        print("Draw!")

    elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()) and sum(cheater1.get_dice()) > sum(cheater3.get_dice()):
        print("Cheater 1 wins!")

    elif sum(cheater2.get_dice()) > sum(cheater1.get_dice()) and sum(cheater2.get_dice()) > sum(cheater3.get_dice()):
        print("Cheater 2 wins!")

    elif sum(cheater3.get_dice()) > sum(cheater1.get_dice()) and sum(cheater3.get_dice()) > sum(cheater2.get_dice()):
        print("Cheater 3 wins!")

if __name__ == "__main__":
    main()
