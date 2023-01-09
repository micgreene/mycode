#!/usr/bin/env python3
"""Alta3 Research || Author RZFeeser@alta3.com
Learning how to use functions"""

## Installs the crayons package.
## python3 -m pip install crayons
## import statements ALWAYS go up top
import crayons


def main():
    """run time code. Always indent under function"""

    # print 'red string' in red
    print("We can only conclude the ",crayons.red('murder'), " took place in this very room...")
    # print bold letters
    print("What?! You're ", crayons.blue('quite'), " sure? The implications of a ", crayons.red('murder', bold=True), " are nothing to jest about.")
    
    crayons.disable() # disables the crayons package

    crayons.DISABLE_COLOR = False # enable the crayons package

if __name__ == "__main__":
    main()

