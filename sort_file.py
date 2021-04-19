#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Select file and sort files"""

import sys
import os
import glob
import shutil

def main():

    """Select file and sort files"""

    directory_name = sys.argv[1]

    vid = ['.mov','.mp4','.avi']
    img = ['.jpeg','.jpg','.png']
    dirs = ['images', 'videos']

    for dr in dirs:
        if not os.path.exists(dr):
            os.makedirs(dr)

    listfile = glob.glob(directory_name+"/*")

    for file, dr in listfile:
        if os.path.splitext(file)[1] in img:
            shutil.move(file, dirs[0])
        if os.path.splitext(file)[1] in vid:
            shutil.move(file, dirs[1])

if __name__ == "__main__":
    main()