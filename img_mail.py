# -*- coding: utf-8 -*-
"""
Created on Fri May 18 11:18:42 2018

@author: elies
"""

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib


def send(emailto):
    with open('conteudonadasigiloso.txt','r') as p:
        password = p.read()
    msg = MIMEMultipart()
    msg['From'] = 'jogoavengers@gmail.com'
    #msg['To'] =  email
    msg['Subject'] = "teste"
 

    foto=open(r"C:\Users\elies\Desktop\PF\photos\vingador.png", "rb")
    msg.attach(MIMEImage(foto.read()))
    msg.attach(MIMEText("thanks for playing"))
 

    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()
    server.login(msg['From'], password)

    server.sendmail(msg['From'], emailto, msg.as_string())
    server.quit()
    return None


#try:
#    server.sendmail(msg['From'], msg['To'], msg.as_string())
#    print ("sent to {}".format((msg['To'])))
#except:
#    print ('error sending mail')

