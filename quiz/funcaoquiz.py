from flask import request
def multiplaescolha(pergunta):
	lista=[]
	x = request.form[pergunta]
	if pergunta=='perg1':
		if x==0:
			lista=['a']
		if x==1:
			lista=['b']
	if pergunta=='perg2':
		if x==0:
			lista=['a']
		if x==1:
			lista=['b']
	return lista
