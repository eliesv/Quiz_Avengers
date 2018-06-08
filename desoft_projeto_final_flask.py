# -*- coding: utf-8 -*-
"""
@authors: elies, freddyd, michelh
"""

from flask import Flask, request, render_template, redirect
import funcao as f
import maxkey as m
import idade as anos
import img_mail as mail
#import Photos as p
import cv2
import json
from random import randint
import os
from shutil import copyfile
from copy_file import copy_file, copy_file2
from delete_file import delete_file


app = Flask(__name__,static_url_path="")

dicionario = {}

@app.route("/")
def introdução():
    return render_template("intro.html")

@app.route("/adeus", methods=['GET'])
def adeus():
    return render_template('adeus.html')

@app.route("/quiz", methods=['POST','GET'])
def quiz():

    if request.method == "GET":
        return render_template('quiz.html')

    if request.method == "POST":
        print("test")
        lista = ["Captain America","Iron Man","Hulk","Thor","Spider Man", "Doctor Strange", "Black Panther", "Peter Quill", "Vision", "Scarlet Witch", "Ant Man", "Rocket"]
        for i in lista:
            dicionario[i] = 0

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

        dicjson = {}
        dicjson["nome"] = request.form["nome"]
        dicjson["vencedor"] = vencedor
        dicjson["contador"] = 0
        with open('variaveis.json','w') as variaveis:
            variaveis.write(json.dumps(dicjson))

    return redirect("/camera")

@app.route('/camera', methods=['GET', 'POST'])
def camera():

    if request.method == "GET":
        with open('variaveis.json','r') as variaveis:
            dicjson = json.loads(variaveis.read())
            Nome = dicjson["nome"]
            contador = dicjson["contador"]


        pathSelfie=os.path.join(os.path.expanduser("~"), "Downloads\\selfie.png")
        pathSelfie=pathSelfie.replace("\\","/")
        if os.path.isfile(pathSelfie):
            copy_file(contador)
            copy_file2()
            delete_file(pathSelfie)

        dicjson["contador"] += 1
        with open('variaveis.json','w') as variaveis:
            variaveis.write(json.dumps(dicjson))

        return render_template("camera.html", n = Nome)

    if request.method == 'POST':
        #p.overlay()
        return redirect("/loading")

@app.route("/loading", methods=['GET'])
def loading():
    return render_template('loading.html', x = randint(0,4)) #tela de loading aleatoria

@app.route("/resultado", methods=['POST','GET'])
def resultado():

    if request.method == "GET":
        with open('variaveis.json','r') as variaveis:
            dicjson = json.loads(variaveis.read())
            vencedor = dicjson["vencedor"]

        return render_template("resultado.html", v = vencedor)

    if request.method == "POST":
        return redirect("/email")

@app.route("/email", methods=['POST','GET'])
def email():
    with open('email.txt','w') as bb:
        bb.write("jogoavengers@gmail.com")
    if request.method == "GET":
        return render_template("email.html")

    if request.method == "POST":
        with open('email.txt','w') as bb:
             if request.form['email'] !='':
                bb.write(request.form['email'])
        with open('email.txt','r') as bb:
                 emailto = bb.read()
                 mail.send(emailto)
                 print(emailto)
            # with open("maillist.txt", 'a') as maillist: #Salva os emails
            #     maillist.write(emailto)
            #     maillist.write("\n")
        return redirect("/sent")

@app.route("/sent", methods=['POST','GET'])
def sent():
    if request.method == "GET":
        with open('email.txt','r') as bb:
             emailto = bb.read()
        return render_template("emailsent.html", x = emailto)

    # if request.method == "POST":
    #     return render_template('emailsent.html')

@app.route("/thanos", methods=['GET'])
def thanos():
    return render_template('thanos.html')
