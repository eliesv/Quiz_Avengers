from flask import *
import funcaoquiz
from maxkey import *

app = Flask(__name__,static_url_path="")

@app.route("/", methods=["POST", "GET"])
def intro():
    if request.method == "GET":
        return render_template("intro.html")

    if request.method == "POST":
        return redirect("/quiz")

@app.route("/quiz", methods=["POST", "GET"])
def inicial():
    if request.method == "GET":
        return render_template("Quizfinal.html")

    if request.method == "POST":

        with open("Respostas.json", "r") as r:
            dicfinal = json.load(r)

        with open("Perguntas.txt", "r") as r:
            perguntas=r.read()
            lista_pergs = perguntas.split(",")

        for pergunta in lista_pergs:
            lista_resps = funcaoquiz.multiplaescolha(pergunta)
            for e in lista_resps:
                dicfinal[e] += 1
        print(dicfinal)

        vencedor = maxkey(dicfinal)
        print(vencedor)
        with open('vencedor.txt','w') as v:
            v.write(vencedor)

        return redirect("/resultado")

@app.route("/resultado", methods=["GET","POST"])
def quizresultado():
    if request.method == "GET":
        with open('vencedor.txt','r') as v:
            vencedor = v.read()
        return render_template("Resultado.html", vencedor = vencedor)
    if request.method == "POST":
        return redirect("/")
