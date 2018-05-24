# -*- coding: utf-8 -*-
"""
Created on Wed May 16 13:42:19 2018

@author: elies
"""

from flask import request

def multiplaescolha(pergunta):
    x = ''
    lista = []
    escolha = request.form[pergunta]
    if escolha == "0":
        x = 0
    elif escolha == "1":
        x = 1
    elif escolha == "2":
        x = 2
    elif escolha == "3":
        x = 3
    else:
        lista = 10
        
    if pergunta == "city":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]
            
    elif pergunta == "animal":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]

    elif pergunta == "planeta":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]

    elif pergunta == "esporte":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]

    elif pergunta == "olho":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]

    elif pergunta == "musica":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]
            
    elif pergunta == "cor":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]
            
    elif pergunta == "filme":
        if x == 0:
            lista = ["Captain America"]  
        elif x == 1:
            lista = ["Hulk"]       
        elif x == 2:
            lista = ["Thor"]
        elif x == 3:
            lista = ["Iron Man"]
    
    return lista

