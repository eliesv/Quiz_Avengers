# -*- coding: utf-8 -*-
"""
Created on Tue May 15 13:17:23 2018

@author: elies
"""

from flask import Flask, request, render_template
import funcao as f
import maxkey as m
import idade as anos
import img_mail as mail
#from photos.Photos import camera
#import cv2

app = Flask(__name__,static_url_path="")

dicionario = {}
vencedor = ""

@app.route("/")
def introdução():
    return render_template("intro.html")

@app.route("/adeus", methods=['POST','GET'])
def adeus():
    return render_template('adeus.html')

@app.route("/quiz", methods=['POST','GET'])
def quiz():
      
    if request.method == "GET":
        return render_template('quiz.html')
    
    if request.method == "POST":
        
        lista = ["Captain America","Iron Man","Hulk","Thor","Spider Man", "Doctor Strange", "Black Panther", "Peter Quill", "Vision", "Scarlet Witch", "Falcon", "Rocket"]
        for i in lista:
            dicionario[i] = 0

        idade = anos.idade()
        for i in idade:
            dicionario[i] += 1
        
        lisperg = ["city","animal","planeta","esporte","olho","musica","cor","filme"]
        for i in lisperg:
            for a in f.multiplaescolha(i):
                dicionario[a] += 1
        
        vencedor = m.maxkey(dicionario)
        print(dicionario)

    return render_template("resultado.html", x = vencedor)

@app.route("/resultado", methods=['POST','GET'])
def resultado():
#    camera("Iron man","rr.jpg") 
    return render_template('email.html')

@app.route("/email", methods=['POST','GET'])
def email():
    emailto = request.form['email']
    mail.send(emailto)
    return render_template('emailsent.html', x = emailto)