# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 21:52:21 2018

@author: elies
"""

import shutil

def zip_file(file_name,directory_path):
    shutil.make_archive(file_name, 'zip', directory_path)
    return None

#file_name = r'C:/users/elies/Desktop/teste'
#Directory_path = r'C:/Users/elies/Desktop/teste'
