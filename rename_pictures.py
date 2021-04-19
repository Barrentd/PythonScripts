#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Rename file in directory"""

import sys
import os

def main():

    """Select file and rename element in the file"""

    directory_name = sys.argv[1]
    num_img = 0

    listing = os.listdir(directory_name)

    for dir_file in listing:
        num_img = num_img + 1
        old_file = os.path.join(directory_name, dir_file)
        new_file = os.path.join(directory_name, str(num_img)+'.jpg')
        os.rename(old_file, new_file)
        print(new_file)

if __name__ == "__main__":
    main()
