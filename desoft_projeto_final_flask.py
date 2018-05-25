# -*- coding: utf-8 -*-
"""
@authors: elies, freddyd, michelh
"""

from flask import Flask, request, render_template, redirect
import funcao as f
import maxkey as m
import idade as anos
import img_mail as mail
#from photos.Photos import camera
#import cv2

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
            
        #Nome = request.method["nome"]

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

    return redirect("/red")

@app.route("/red", methods=['GET', 'POST'])
def redi():
    return redirect("/camera")

@app.route('/camera', methods=['GET', 'POST'])
def camera():
    
    if request.method == "GET":
        return render_template("camera.html", n = Nome)
    
    if request.method == 'POST':
        print('Uploading...')
        print(request.method)
        print(request.mimetype)
        #print(request.get_json())

        #imgData = request.form.get('pic')
        #imgData = request.form
        #imgData = request.get_json(force=True, silent=False)
        imgData = request.get_data()

        #imgData = request.content

        #print(imgData)
        
        print('Gravando...')
        
        arquivo = open('fotinho.png','wb') #write binary
        #arquivo.write(base64.decodestring(imgData)) 
        #arquivo.write(base64.b64decode(imgData)) 
        arquivo.write(imgData) 


        arquivo.close()
        
        #script q abre a camera no flask
        #camera("Iron man","rr.jpg")
    
    return redirect("/resultado")

@app.route("/resultado", methods=['POST','GET'])
def resultado():
    
    if request.method == "GET":
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