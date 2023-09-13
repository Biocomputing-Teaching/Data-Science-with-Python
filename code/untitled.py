#!/usr/local/bin/python

# Python File and Directory Manipulator 1.0
# Author: Douglas Palovick
# License: GPL http://www.gnu.org/licenses/gpl.txt

import os, glob, shutil

file_ext = raw_input("enter the file ext, ex jpg:\n")
file_count = raw_input("enter in the file\
 count for each new dir:\n")
file_count = int(file_count)
dir_base_name = raw_input("enter the base name\
 for each new dir:\n")

filenames = glob.glob(('*.' + file_ext))
filenames.sort()
dir_number = 0

while filenames:
    dir_number += 1
    new_dir = dir_base_name + str(dir_number)
    os.mkdir(new_dir)
    for n in range(min(file_count, len(filenames))):
        src_file = filenames.pop(0)
        shutil.copy(src_file, new_dir)
        os.unlink(src_file)
