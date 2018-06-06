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
    if idade <= 1:
        lista = ["Captain America","Black Panther"]
    elif idade == 2:
        lista = ["Hulk","Iron Man"]
    elif idade == 3:
        lista = ["Vision","Scarlet Witch"]
    elif idade == 4:
        lista = ["Thor","Ant Man"]
    elif idade == 5:
        lista = ["Doctor Strange","Spider Man"]
    elif idade >= 6:
        lista = ["Peter Quill","Rocket"]
    return lista
