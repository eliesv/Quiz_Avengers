# -*- coding: utf-8 -*-
"""
Created on Fri May 18 00:39:09 2018

@author: elies
"""

def maxkey(dictionary):
    maxv = max(dictionary.values())
    maxk = ''
    for key in dictionary:
        if dictionary[key] == maxv:
            maxk = key
            break
    return maxk