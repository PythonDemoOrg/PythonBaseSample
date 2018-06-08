# -*- coding: UTF-8 -*-

# Filename : walk_to_delete_dir.py
# author by : WeiQi

import os
import shutil

def walkDir(str):
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            # print ("fileIs :: "+fullpath)

        for dir in dirnames:
            print ("dir is :: "+dir)
            if (dir == str):
                fullpath = os.path.join(dirpath, dir)
                print('fullpath='+fullpath)
                shutil.rmtree(fullpath)
                print("deleteit="+fullpath)

# path = "/Users/huangweiqi/StudioProjects/"
path = "/Users/huangweiqi/Documents/Work/workspace"
# walkDir('build')
# walkDir('gen')
walkDir('bin')