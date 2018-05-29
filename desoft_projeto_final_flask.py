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
import json

app = Flask(__name__,static_url_path="")

dicionario = {}
vencedor = ""

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
        with open('variaveis.json','w') as variaveis:
            variaveis.write(json.dumps(dicjson))

    return redirect("/camera")

@app.route('/camera', methods=['GET', 'POST'])
def camera():

    if request.method == "GET":
        with open('variaveis.json','r') as variaveis:
            dicjson = json.loads(variaveis.read())
            Nome = dicjson["nome"]
        return render_template("camera.html", n = Nome)

    if request.method == 'POST':
        # path = r'C:/Users/{}/'.format(User)
        return redirect("/resultado")

@app.route("/resultado", methods=['POST','GET'])
def resultado():

    if request.method == "GET":
        #p.overlay("Iron man")
        with open('variaveis.json','r') as variaveis:
            dicjson = json.loads(variaveis.read())
            vencedor = dicjson["vencedor"]

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
