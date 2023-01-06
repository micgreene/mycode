#!/usr/bin/env python3
"""A simple script to move two files into ceph_storage/
   Alta3 Research | rzfeeser@alta3.com"""

import shutil
import os

def main():
    """Script moves two files into the ceph_storage directory, renaming one"""
    # file will always run from this dir no mater where it is called from
    os.chdir('/home/student/mycode/')
    
    # moves a file to a new path destination, if just given a folder it will keep its filename
    # returns a string of the absolute path of the new location
    shutil.move('raynor.obj', 'ceph_storage/')

    # query user for new filename
    xname = input('What is the new name for kerrigan.obj? ')
    
    # move file to new folder using the new filename from user
    # returns a string of the absolute path of the new location
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

if __name__ == "__main__":
    main()

