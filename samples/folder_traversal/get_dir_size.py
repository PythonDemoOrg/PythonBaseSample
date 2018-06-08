# -*- coding: UTF-8 -*-

# Filename : get_dir_size.py
# author by : WeiQi

import os

def getDirSize(dir):
    for (root, dirs, files) in os.walk(dir, False):
        size = 0

    for filename in files:
        size += os.path.getsize(os.path.join(root, filename))
        print (root, size / 1024)

path = "/Users/huangweiqi/iOSProjects/"
getDirSize(path)
