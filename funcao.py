# -*- coding: utf-8 -*-
"""
Created on Wed May 16 13:42:19 2018

@author: elies
"""

from flask import request

def multiplaescolha(pergunta):
    x = ''
    lista = []
    x = int(request.form[pergunta])
        
    if pergunta == "cidade":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]
        elif x == 4:
            lista = ["Black Panther"]
        elif x == 5:
            lista = ["Spider Man"]
            
    elif pergunta == "animal":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]
        elif x == 4:
            lista = ["Black Panther"]
        elif x == 5:
            lista = ["Spider Man"]

    elif pergunta == "planeta":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]
        elif x == 4:
            lista = ["Black Panther"]
        elif x == 5:
            lista = ["Spider Man"]

    elif pergunta == "esporte":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]
        elif x == 4:
            lista = ["Black Panther"]
        elif x == 5:
            lista = ["Spider Man"]

    elif pergunta == "olho":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]
        elif x == 4:
            lista = ["Black Panther"]
        elif x == 5:
            lista = ["Spider Man"]

    elif pergunta == "musica":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]
        elif x == 4:
            lista = ["Black Panther"]
        elif x == 5:
            lista = ["Spider Man"]
            
    elif pergunta == "camisa":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]
        elif x == 4:
            lista = ["Black Panther"]
        elif x == 5:
            lista = ["Spider Man"]
            
    elif pergunta == "filme":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]
        elif x == 4:
            lista = ["Black Panther"]
        elif x == 5:
            lista = ["Spider Man"]
            
    elif pergunta == "pedra":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]
        elif x == 4:
            lista = ["Black Panther"]
        elif x == 5:
            lista = ["Spider Man"]
            
    elif pergunta == "cor":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]
        elif x == 4:
            lista = ["Black Panther"]
        elif x == 5:
            lista = ["Spider Man"]
            
    elif pergunta == "comida":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]
        elif x == 4:
            lista = ["Black Panther"]
        elif x == 5:
            lista = ["Spider Man"]
            
    elif pergunta == "numero":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]
        elif x == 4:
            lista = ["Black Panther"]
        elif x == 5:
            lista = ["Spider Man"]

    return lista

