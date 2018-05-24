# -*- coding: utf-8 -*-
"""
Created on Fri May 18 08:32:16 2018

@author: elies
"""
from flask import request 

def idade():
    lista = []
    idade = 0
    idade = int(request.form["idade"])
    idade = int(round(idade/10))
    if  idade <= 1:
        lista == ["Captain America"]
    elif idade == 2:
        lista = ["Hulk"]
    elif idade == 3:
        lista = ["Thor"]
    elif idade >= 4:
        lista = ["Iron Man"]
    return lista