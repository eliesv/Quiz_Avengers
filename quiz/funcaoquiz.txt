from flask import request
def multiplaescolha(pergunta):
	lista=[]
	x = request.form[pergunta]
	if pergunta=="abajour": 
		if x=="0":
			lista=['a']
		if x=="1":
			lista=['b']
	if pergunta=="paodquie": 
		if x=="0":
			lista=['a']
		if x=="1":
			lista=['b']
	return lista
