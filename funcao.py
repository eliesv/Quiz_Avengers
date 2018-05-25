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
            lista = ["Captain America","Black Panther"]  
        elif x == 1:
            lista = ["Hulk","Iron Man"]       
        elif x == 2:
            lista = ["Vision","Scarlet Witch"]
        elif x == 3:
            lista = ["Thor","Ant Man"]
        elif x == 4:
            lista = ["Doctor Strange","Spider Man"]
        elif x == 5:
            lista = ["Peter Quill","Rocket"]
            
    elif pergunta == "animal":
        if x == 0:
            lista = ["Black Panther", "Iron Man"]  
        elif x == 1:
            lista = ["Rocket", "Vision"]       
        elif x == 2:
            lista = ["Ant Man", "Peter Quill"]
        elif x == 3:
            lista = ["Captain America", "Hulk"]
        elif x == 4:
            lista = ["Thor","Scarlet Witch"]
        elif x == 5:
            lista = ["Spider Man","Doctor Strange"]

    elif pergunta == "planeta":
        if x == 0:
            lista = ["Doctor Strange","Iron Man"]  
        elif x == 1:
            lista = ["Thor","Hulk"]       
        elif x == 2:
            lista = ["Rocket","Scarlet Witch"]
        elif x == 3:
            lista = ["Ant Man","Spider Man"]
        elif x == 4:
            lista = ["Peter Quill","Vision"]
        elif x == 5:
            lista = ["Black Panther","Captain America"]

    elif pergunta == "esporte":
        if x == 0:
            lista = ["Rocket","Scarlet Witch"]  
        elif x == 1:
            lista = ["Doctor Strange","Vision"]       
        elif x == 2:
            lista = ["Thor","Spider Man"]
        elif x == 3:
            lista = ["Iron Man","Hulk"]
        elif x == 4:
            lista = ["Black Panther","Captain America"]
        elif x == 5:
            lista = ["Ant Man","Peter Quill"]

    elif pergunta == "olho":
        if x == 0:
            lista = ["Captain America","Thor"]  
        elif x == 1:
            lista = ["Scarlet Witch","Peter Quill"]       
        elif x == 2:
            lista = ["Doctor Strange","Iron Man"]
        elif x == 3:
            lista = ["Black Panther","Spider Man"]
        elif x == 4:
            lista = ["Ant Man","Rocket"]
        elif x == 5:
            lista = ["Vision","Hulk"]

    elif pergunta == "musica":
        if x == 0:
            lista = ["Vision","Ant Man"]  
        elif x == 1:
            lista = ["Hulk","Captain America"]       
        elif x == 2:
            lista = ["Thor","Doctor Strange"]
        elif x == 3:
            lista = ["Iron Man","Black Panther"]
        elif x == 4:
            lista = ["Peter Quill","Rocket"]
        elif x == 5:
            lista = ["Spider Man","Scarlet Witch"]
            
    elif pergunta == "camisa":
        if x == 0:
            lista = ["Rocket","Scarlet Witch"]  
        elif x == 1:
            lista = ["Peter Quill", "Black Panther"]       
        elif x == 2:
            lista = ["Iron Man","Spider Man"]
        elif x == 3:
            lista = ["Captain America","Thor"]
        elif x == 4:
            lista = ["Hulk","Doctor Strange"]
        elif x == 5:
            lista = ["Vision","Ant Man"]
            
    elif pergunta == "filme":
        if x == 0:
            lista = ["Vision","Thor"]  
        elif x == 1:
            lista = ["Hulk","Ant Man"]       
        elif x == 2:
            lista = ["Peter Quill","Doctor Strange"]
        elif x == 3:
            lista = ["Rocket","Black Panther"]
        elif x == 4:
            lista = ["Spider Man","Captain America"]
        elif x == 5:
            lista = ["Iron Man","Scarlet Witch"]
            
    elif pergunta == "pedra":
        if x == 0:
            lista = ["Hulk","Black Panther"]  
        elif x == 1:
            lista = ["Doctor Strange","Captain America"]       
        elif x == 2:
            lista = ["Scarlet Witch","Spider Man"]
        elif x == 3:
            lista = ["Vision","Rocket"]
        elif x == 4:
            lista = ["Iron Man","Peter Quill"]
        elif x == 5:
            lista = ["Thor","Ant Man"]
            
    elif pergunta == "cor":
        if x == 0:
            lista = ["Spider Man","Peter Quill"]  
        elif x == 1:
            lista = ["Iron Man", "Captain America"]       
        elif x == 2:
            lista = ["Thor","Hulk"]
        elif x == 3:
            lista = ["Black Panther","Doctor Strange"]
        elif x == 4:
            lista = ["Vision","Ant Man"]
        elif x == 5:
            lista = ["Rocket","Scarlet Witch"]
            
    elif pergunta == "comida":
        if x == 0:
            lista = ["Captain America","Scarlet Witch"]  
        elif x == 1:
            lista = ["Hulk","Vision"]       
        elif x == 2:
            lista = ["Thor","Iron Man"]
        elif x == 3:
            lista = ["Visiom","Peter Quill"]
        elif x == 4:
            lista = ["Black Panther","Doctor Strange"]
        elif x == 5:
            lista = ["Spider Man","Rocket"]
            
    elif pergunta == "numero":
        if x == 0:
            lista = ["Doctor Strange","Rocket"]  
        elif x == 1:
            lista = ["Vision","Black Panther"]       
        elif x == 2:
            lista = ["Peter Quill","Scarlet Witch"]
        elif x == 3:
            lista = ["Spider Man","Ant Man"]
        elif x == 4:
            lista = ["Captain America","Thor"]
        elif x == 5:
            lista = ["Iron Man","Hulk"]

    return lista

