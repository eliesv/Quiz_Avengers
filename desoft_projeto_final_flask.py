# -*- coding: utf-8 -*-
"""
@authors: elies, freddyd, michelh
"""

from flask import Flask, request, render_template, redirect
import funcao as f
import maxkey as m
import idade as anos
import img_mail as mail
import Photos as p
import cv2
from base64 import b64decode
import codecs

app = Flask(__name__,static_url_path="")

dicionario = {}
vencedor = "aaa"
Nome = ""

@app.route("/")
def introdução():
    return render_template("intro.html")

@app.route("/adeus", methods=['POST','GET'])
def adeus():
    return render_template('adeus.html')

@app.route("/quiz", methods=['POST','GET'])
def quiz():
      
    if request.method == "GET":
        #Nome = request.form["nome"]
        return render_template('quiz.html')
    
    if request.method == "POST":
        print("test")
        lista = ["Captain America","Iron Man","Hulk","Thor","Spider Man", "Doctor Strange", "Black Panther", "Peter Quill", "Vision", "Scarlet Witch", "Ant Man", "Rocket"]
        for i in lista:
            dicionario[i] = 0
        
        with open('nome.txt','w') as nn:
            nn.write(request.form["nome"])

        idade = anos.idade()
        for i in idade:
            dicionario[i] += 1
        
        lisperg = ["cidade","animal","planeta","esporte","olho","musica","camisa","filme","pedra","cor","comida","serie"]
        for i in lisperg:
            for a in f.multiplaescolha(i):
                dicionario[a] += 1
        
        vencedor = m.maxkey(dicionario)
        print(dicionario)
        print(vencedor)
        print(request.form)
        
        with open('vencedor.txt','w') as vv:
            vv.write(vencedor)

    return redirect("/camera")

@app.route('/camera', methods=['GET', 'POST'])
def camera():
    
    if request.method == "GET":
        with open('nome.txt','r') as nn:
            Nome = nn.read()
        return render_template("camera.html", n = Nome)
    
    if request.method == 'POST':
        imgData = str(request.get_data()) #vem como bytes --> .decode() transforma em string e .encode(), de string de volta em bytes
        print('Imagem enviada...')
        
        imgData = imgData.partition(",")[2] #corta o texto q vem antes
        pad = len(imgData)%4 #checa se len(imgData) é divisiver por 4 (pro base64 funcionar tem q ser aparentemente)
        imgData += "="*pad # adiciona = até ficar divisivel por 4 pq por algum motivo isso funcionay        
        imgData = codecs.decode(imgData.encode().strip(),'base64') #decodifica base64

        with open("vingador.png", 'wb') as foto: #write bytes
            foto.write(imgData)

    return redirect("/resultado")

@app.route("/resultado", methods=['POST','GET'])
def resultado():
    
    if request.method == "GET":
        #p.overlay("Iron man")
        with open('vencedor.txt','r') as vv:
            vencedor = vv.read()
        return render_template("resultado.html", v = vencedor)

    if request.method == "POST":
        return redirect("/email")

@app.route("/email", methods=['POST','GET'])
def email():
    
    if request.method == "GET":
        return render_template("email.html")
    
    if request.method == "POST":
        emailto = request.form['email']
        mail.send(emailto)
    return render_template('emailsent.html', x = emailto)

@app.route("/thanos", methods=['GET'])
def thanos():
    return render_template('thanos.html')