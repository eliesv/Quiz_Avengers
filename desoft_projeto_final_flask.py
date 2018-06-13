# -*- coding: utf-8 -*-
"""
@authors: elies, freddyd, michelh
"""

from flask import *
import funcao as f
import maxkey as m
import idade as anos
import img_mail as mail
import cv2
import json
from random import randint
import os
from shutil import copyfile
from copy_file import *
from delete_file import delete_file
import subprocess
from zip_file import zip_file

app = Flask(__name__,static_url_path="")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 5


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
            copy_file1(contador)
            copy_file2()
        dicjson["contador"] += 1
        with open('variaveis.json','w') as variaveis:
            variaveis.write(json.dumps(dicjson))

        pathDelete=os.path.join(os.path.expanduser("~"), "Documents/GitHub/Quiz_Avengers/static/img/vingador.png")
        delete_file(pathDelete)

        subprocess.Popen("Photos.py", shell=True)
        return redirect("/loading")

@app.route("/loading", methods=['GET'])
def loading():
    return render_template('loading.html', x = randint(0,4)) #tela de loading aleatoria

@app.route("/resultado", methods=['POST','GET'])
def resultado():

    if request.method == "GET":

        copy_file3()

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

        try:
            mail.send(emailto)
            print("Enviado")
        except:
            print("ERROR")

        return redirect("/sent")

@app.route("/sent", methods=['POST','GET'])
def sent():
    if request.method == "GET":
        with open('email.txt','r') as bb:
             emailto = bb.read()
        return render_template("emailsent.html", x = emailto)

@app.route("/thanos", methods=['GET'])
def thanos():
    return render_template('thanos.html')

#---------------------------------------------CRIE SEU QUIZ---------------------------------------------------------------
pathquiz = os.path.join(os.path.expanduser("~"), "Documents/GitHub/Quiz_Avengers/quiz/")
pathtemplates = os.path.join(os.path.expanduser("~"), "Documents/GitHub/Quiz_Avengers/templates/")
pathjogo = os.path.join(os.path.expanduser("~"), "Documents/GitHub/Quiz_Avengers/")


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


        #Cria HTML para Criar quiz a partir do numero de perguntas e opcoes
        with open('{}criar2.html'.format(pathtemplates),'w') as cr:
            cr.write('<html><head><link rel="stylesheet" type="text/css" href="style/style.css"><link href="https://fonts.googleapis.com/css?family=Marvel" rel="stylesheet"><style>input[type=text] {width: 20%;padding: 12px 20px;margin: 8px 0;box-sizing: border-box;}</style></head>\n')
            cr.write('<center><br><body bgcolor="#091C4B"><font color="white"><h1>Criar meu Quiz</h1><br>Escreva as perguntas, suas opcoes e qual(is) resultados serao afetados por cada opcao.<br> Cada opcao da um ponto para cada resultado escolhido.<br> Para pontuar mais de um resultado por opcao, separe-os por virgulas.<br> Tome cuidado para escrever o mesmo resutado sempre exatamente da mesma forma!<br>Nao use caracteres como ce cedilha ou acentos!<br><br>\n')
            cr.write('<form name="send-form" class="send-form" method="POST" action="/criar2">\n')
            cr.write('\n')
            for i in range(0,dicjson["Qperg"]):
                cr.write('<input type="text" name="pergunta{}" placeholder="Pergunta {}" required/><br>\n'.format(i,i))
                for a in range(0,dicjson["Qopc"]):
                    cr.write('<input type="text" name="opcao{}_{}" placeholder="Opcao {}_{}" required/>\n  '.format(i,a,i,a))
                    cr.write('<input type="text" name="resposta{}_{}" placeholder="Resposta {}_{}" required/><br>\n  '.format(i,a,i,a))
                cr.write('<br>\n')
            cr.write('<button class="a" type="submit">OK</button> \n')
            cr.write('</form></body></html>')

    return redirect("/criar2")

@app.route("/criar2", methods=['POST','GET'])
def criar2():
    if request.method == "GET":
        return render_template("criar2.html")

    if request.method == "POST":

        with open('variaveis.json','r') as variaveis:
            dicjson = json.loads(variaveis.read())

        #cria um JSON e TXT com as perguntas e respostas
        listaresp=[]
        dict_respostas={}
        for i in range(0,dicjson["Qperg"]):
            for a in range(0,dicjson["Qopc"]):
                resp=request.form['resposta{}_{}'.format(i,a)]
                lista=resp.split(",")
                for j in lista:
                    if j not in listaresp:
                        listaresp.append(j)
        for h in listaresp:
            dict_respostas[h]=0
        with open('{}Respostas.json'.format(pathquiz),'w') as r:
            r.write(json.dumps(dict_respostas))

        listaperguntas=[]
        for i in range(0,dicjson["Qperg"]):
                resp=request.form['pergunta{}'.format(i)]
                lista=resp.split(",")
                for j in lista:
                    if j not in listaperguntas:
                        listaperguntas.append(j)

        with open('{}Perguntas.txt'.format(pathquiz),'w') as r:
            for i in range(0,len(listaperguntas)):
                if i < len(listaperguntas)-1:
                    r.write("{}".format(listaperguntas[i]))
                    r.write(',')
                else:
                    r.write("{}".format(listaperguntas[len(listaperguntas)-1]))

        #cria o HTML do quiz final
        with open('{}/templates/Quizfinal.html'.format(pathquiz),'w') as cri:
            cri.write('<html>\n')
            cri.write('<head><link rel="stylesheet" type="text/css" href="/style/stylequiz.css"></head>\n')
            cri.write('<body bgcolor="#091C4B"><font color="white" size="6"><center><h1>Quiz</h1></center>\n')
            cri.write('<form name="send-form" class="send-form" method="POST" action="/quiz">\n')
            for i in range(0,dicjson["Qperg"]):
                re_form=request.form['pergunta{}'.format(i)]
                cri.write('<label><font color="white">{}</label><br><br> \n'.format(re_form))
                for a in range(0,dicjson["Qopc"]):
                    re_form2=request.form['opcao{}_{}'.format(i,a)]
                    cri.write('<label class="container">{}<input type="radio" name="{}" value="{}" required><span class="checkmark"/></label><br>\n '.format(re_form2,re_form,a))
                cri.write('<br><br>\n')
            cri.write('<center><button class="a" type="sumbit">OK</button></center></form>\n')
            cri.write('</body>\n')
            cri.write('</html>\n')

        #cria a funcao para rodar o quiz no flask
        with open('{}funcaoquiz.txt'.format(pathquiz),'w') as f:
            f.write("from flask import request\n")
            f.write("def multiplaescolha(pergunta):\n")
            f.write("\tlista=[]\n")
            f.write("\tx = request.form[pergunta]\n")
            for i in range(0,dicjson["Qperg"]):
                re_form=request.form['pergunta{}'.format(i)]
                f.write('\tif pergunta=="{}": \n'.format(re_form))
                for a in range(0,dicjson["Qopc"]):
                    f.write('\t\tif x=="{}":\n'.format(a))
                    re_form3=request.form['resposta{}_{}'.format(i,a)]
                    lista=re_form3.split(",")
                    f.write('\t\t\tlista={}\n'.format(lista))
            f.write("\treturn lista\n")
        subprocess.Popen("Copyfuncao.py", shell=True)

        return redirect("/fim")

@app.route("/fim", methods=["GET","POST"])
def fim():
    pathdesktop = os.path.join(os.path.expanduser("~"), "Desktop/")
    zip_file("seu_quiz","{}".format(pathquiz))
    copy_file_mor("{}seu_quiz.zip".format(pathjogo), "{}seu_quiz.zip".format(pathdesktop))
    return render_template("fim.html")
