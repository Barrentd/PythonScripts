#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Select file and sort files"""

import sys
import os
import glob
import shutil

def main():

    """Select file and sort files"""

    directory_name = sys.argv[1]

    vid=['.mov','.mp4','.avi']
    img=['.jpeg','.jpg','.png']

    if not os.path.exists('images'):
        os.makedirs('images')

    if not os.path.exists('slides'):
        os.makedirs('videos')

    listfile = glob.glob(directory_name+"/*")

    for file in listfile:
        if os.path.splitext(file)[1] in vid:
            shutil.move(file, 'slides')
        if os.path.splitext(file)[1] in img:
            shutil.move(file, 'images')

if __name__ == "__main__":
    main()