#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   Pushing files around using shutil and os from the standard library"""

import shutil
import os

def main():    
    # no matter where the file is called from, it will execute frm here:
    os.chdir("/home/student/mycode/")

    # copies a files to a new destination folder, or use a filename to rename the copy
    # returns a string of the copied file's path
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # copies the entire directory and its files to a new directory
    # will create the dir if not present
    # returns a string of the copied folder's path
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
