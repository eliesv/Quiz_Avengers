from flask import request
def multiplaescolha(pergunta):
	lista=[] 
	x = request.form[pergunta] 
	if pergunta=="Isso funciona?": 
		if x==0:
			lista=['s']
		if x==1:
			lista=['n']
	if pergunta=="Se funcionar vai ser fudido?": 
		if x==0:
			lista=['s']
		if x==1:
			lista=['n']
	if pergunta=="Qual a chance de funcionar de primeira?": 
		if x==0:
			lista=['s']
		if x==1:
			lista=['n']
	return lista 
