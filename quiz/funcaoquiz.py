from flask import request
def multiplaescolha(pergunta):
	lista=[]
	x = request.form[pergunta]
	if pergunta=="qual seu nome": 
		if x=="0":
			lista=['frita']
		if x=="1":
			lista=['enrolada']
		if x=="2":
			lista=['rustica']
	if pergunta=="qual seu nome": 
		if x=="0":
			lista=['frita']
		if x=="1":
			lista=['enrolada']
		if x=="2":
			lista=['rustica']
	if pergunta=="manto diamantino": 
		if x=="0":
			lista=['frita']
		if x=="1":
			lista=['enrolada']
		if x=="2":
			lista=['rustica']
	return lista
