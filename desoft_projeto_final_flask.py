# -*- coding: utf-8 -*-
"""
@authors: elies, freddyd, michelh
"""

from flask import Flask, request, render_template, redirect
import funcao as f
import maxkey as m
import idade as anos
import img_mail as mail
import cv2
import json
from random import randint
import os
from shutil import copyfile
from copy_file import copy_file, copy_file2
from delete_file import delete_file
import subprocess

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

        with open('variaveis.json','r') as variaveis:
            dicjson = json.loads(variaveis.read())
            dicjson["nome"] = request.form["nome"]
            dicjson["vencedor"] = vencedor
            dicjson["Qperg"]=0
            dicjson["Qopc"]=0
            dicjson["contador"]=dicjson["contador"]
        with open('variaveis.json','w') as variaveis:
            variaveis.write(json.dumps(dicjson))

    return redirect("/camera")

@app.route('/camera', methods=['GET', 'POST'])
def camera():

    if request.method == "GET":
        with open('variaveis.json','r') as variaveis:
            dicjson = json.loads(variaveis.read())
            Nome = dicjson["nome"]

        pathSelfie=os.path.join(os.path.expanduser("~"), "Downloads/selfie.png")
        if os.path.isfile(pathSelfie):
            delete_file(pathSelfie)

        return render_template("camera.html", n = Nome)

    if request.method == 'POST':

        with open('variaveis.json','r') as variaveis:
            dicjson = json.loads(variaveis.read())
            contador = dicjson["contador"]

        pathSelfie=os.path.join(os.path.expanduser("~"), "Downloads/selfie.png")
        if os.path.isfile(pathSelfie):
            copy_file(contador)
            copy_file2()

        dicjson["contador"] += 1
        with open('variaveis.json','w') as variaveis:
            variaveis.write(json.dumps(dicjson))

        subprocess.Popen("Photos.py 1", shell=True)
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

    if request.method == "GET":
        return render_template("email.html")

    if request.method == "POST":

        if request.form['email'] != '':
            emailto = request.form['email']
        else:
            with open('email.txt', 'r') as bb:
                emailto = bb.read()

        mail.send(emailto)
        print(emailto)

        return redirect("/sent")

@app.route("/sent", methods=['POST','GET'])
def sent():
    if request.method == "GET":
        with open('email.txt','r') as bb:
             emailto = bb.read()
        return render_template("emailsent.html", x = emailto)

    # if request.method == "POST":
    #     return render_template('emailsent.html')

@app.route("/criar", methods=['POST','GET'])
def criar():
    if request.method == "GET":
        return render_template("criar.html")

    if request.method == "POST":
        with open('variaveis.json','r') as variaveis:
            dicjson = json.loads(variaveis.read())
        dicjson["Qperg"] = int(request.form['perguntas'])
        dicjson["Qopc"] = int(request.form['opcoes'])
        with open('variaveis.json','w') as variaveis:
            variaveis.write(json.dumps(dicjson))



        with open('criar.txt','w') as cr:
            cr.write('<html> <head><link rel="stylesheet" type="text/css" href="style/style.css"><link href="https://fonts.googleapis.com/css?family=Marvel" rel="stylesheet"></head>\n')
            cr.write('<center><br><body bgcolor="#091C4B"><font color="white"><h1>Criar meu Quiz</h1>\n')
            cr.write('<form name="send-form" class="send-form" method="POST" action="/criar2">\n')
            cr.write('\n')
            for i in range(0,dicjson["Qperg"]):
                cr.write('<input type="text" name="pergunta{}" placeholder="Pergunta {}" required/><br> \n'.format(i,i))
                for a in range(0,dicjson["Qopc"]):
                    cr.write('<input type="text" name="opcao{}_{}" placeholder="Opcao {}_{}" required/>\n  '.format(i,a,i,a))
                    cr.write('<input type="text" name="resposta{}_{}" placeholder="Resposta {}_{}" required/><br> \n  '.format(i,a,i,a))
                cr.write('<br>\n')
            cr.write('<button class="a" type="submit">OK</button> \n')
            cr.write('</form>')
            cr.write('</body>')
            cr.write('</html>')



        pathHTML=os.path.join(os.path.expanduser("~"), "Documents/GitHub/Quiz_Avengers/templates/criar2.html")
        contents = open("criar.txt","r")
        with open(pathHTML, "w") as e:
            for line in contents.readlines():
                e.write(line)
    return redirect("/criar2")

@app.route("/criar2", methods=['POST','GET'])
def criar2():
    if request.method == "GET":
        return render_template("criar2.html")

    if request.method == "POST":

        with open('variaveis.json','r') as variaveis:
            dicjson = json.loads(variaveis.read())

        listafinal=[]
        dict_respostas={}
        for i in range(0,dicjson["Qperg"]):
            for a in range(0,dicjson["Qopc"]):
                resp=request.form['resposta{}_{}'.format(i,a)]
                lista=resp.split(",")
                for j in lista:
                    if j not in listafinal:
                        listafinal.append(j)
        for h in listafinal:
            dict_respostas[h]=0
        with open('Respostas.json','w') as r:
            r.write(json.dumps(dict_respostas))



        with open('Quizfinal.txt','w') as cri:
            cri.write('<html> <head><link rel="stylesheet" type="text/css" href="style/style.css"><link href="https://fonts.googleapis.com/css?family=Marvel" rel="stylesheet"></head>\n')
            cri.write('<center><br><body bgcolor="#091C4B"><font color="white"><h1>Quiz</h1>\n')
            cri.write('<form name="send-form" class="send-form" method="GET" action="/seuquiz">')
            for i in range(0,dicjson["Qperg"]):
                re_form=request.form['pergunta{}'.format(i)]
                cri.write('<label><font color="white">{}</label><br><br> \n'.format(re_form))
                for a in range(0,dicjson["Qopc"]):
                    re_form2=request.form['opcao{}_{}'.format(i,a)]
                    cri.write('<label class="container">{}<input type="radio" name="{}" value="{}" required><span class="checkmark"/></label><br> \n  '.format(re_form2,re_form,a))
                    cri.write('<br>\n')
            #cri.write('<button class="a" type="sumbit">OK</button></form>')
            cri.write('</body>')
            cri.write('</html>')

        pathHTMLFinal=os.path.join(os.path.expanduser("~"), "Documents/GitHub/Quiz_Avengers/templates/QuizFinal.html")
        contents = open("Quizfinal.txt","r")
        with open(pathHTMLFinal, "w") as e:
            for lines in contents.readlines():
                e.write(lines)

        return redirect("/seuquiz")

@app.route("/seuquiz", methods=["GET","POST"])
def seuquiz():
    if request.method == "GET":
        return render_template("QuizFinal.html")


@app.route("/thanos", methods=['GET'])
def thanos():
    return render_template('thanos.html')
