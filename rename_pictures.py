#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Rename file in directory"""

import sys
import os
import dlib
import numpy as np
from cv2 import cv2
from skimage.transform import resize

directoryname = sys.argv[1]
x = 0

listing = os.listdir(directoryname)

for dir_file in listing:
    x = x + 1
    old_file = os.path.join(directoryname, dir_file)
    new_file = os.path.join(directoryname, str(x)+'.jpg')
    os.rename(old_file,new_file)
    print(new_file)