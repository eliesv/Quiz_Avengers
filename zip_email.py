# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 21:47:00 2018

@author: elies
"""

# -*- coding: utf-8 -*-
"""
@authors: elies, freddyd, michelh
"""

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib
from email import encoders


def send(emailto):
    with open('conteudonadasigiloso.txt','r') as p:
        password = p.read()

    msg = MIMEMultipart()
    msg['From'] = 'jogoavengers@gmail.com'
    msg['Subject'] = "Quiz dos Vingadores - Seu Quiz"

    msg.attach(MIMEText("Obrigado por jogar!!! Seu jogo:"))

    msg2 = MIMEBase('application', 'zip')
    with open("seu_quiz.zip",'rb') as zf:
        msg2.set_payload(zf.read())
    encoders.encode_base64(msg2)
    msg2.add_header('Content-Disposition', 'attachment', filename="seu_quiz.zip")
    msg.attach(msg2)



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
