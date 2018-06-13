from flask import request
def multiplaescolha(pergunta):
	lista=[]
	x = request.form[pergunta]
	if pergunta=="1": 
		if x=="0":
			lista=['thor']
		if x=="1":
			lista=['iron man']
		if x=="2":
			lista=['spider man']
	if pergunta=="2": 
		if x=="0":
			lista=['thor', ' iron man']
		if x=="1":
			lista=['spider man']
		if x=="2":
			lista=['black panther']
	return lista
