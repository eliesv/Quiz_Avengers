# -*- coding: utf-8 -*-
"""
@authors: elies, freddyd, michelh
"""
import cv2
import os
import json


with open('variaveis.json','r') as variaveis:
    dicjson = json.loads(variaveis.read())
    vingador = dicjson["vencedor"]

    cascadePath = os.path.join(os.path.expanduser("~"), "Downloads/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml")
    vingadorPath = os.path.join(os.path.expanduser("~"), 'Documents/GitHub/Quiz_Avengers/photos/{}.png'.format(vingador))

    face_cascade = cv2.CascadeClassifier(cascadePath)
    f_image = cv2.imread(vingadorPath, -1)

    f_mask = f_image[:, :, 3]
    b_mask = cv2.bitwise_not(f_mask)
    f_image = f_image[:, :, 0:3]

    f_size = 570
    f_ratio = float(f_size)

    b_size = 2000

    padding_top = ((b_size - f_size) / 3) * 2
    padding_bottom = b_size - padding_top
    padding_left = (b_size - f_size) / 2
    padding_right = (b_size - f_size) / 2


    selfiePath = os.path.join(os.path.expanduser("~"), 'Documents/GitHub/Quiz_Avengers/photos/selfie.png')
    cv_image = cv2.imread(selfiePath)

    faces = face_cascade.detectMultiScale(
                    cv_image,
                    scaleFactor=1.1,
                    minNeighbors=3,
                    minSize=(30, 30),
                    flags=cv2.CASCADE_SCALE_IMAGE)
    for (x1, y1, w, h) in faces:

        x2 = x1 + w
        y2 = y1 + h
        face_roi = cv_image[y1:y2, x1:x2]

        ratio = f_ratio / face_roi.shape[1]
        dimension = (f_size, int(face_roi.shape[0] * ratio))
        face = cv2.resize(face_roi, dimension, interpolation = cv2.INTER_AREA)

        b_image = cv2.copyMakeBorder(face, int(padding_top), int(padding_bottom), int(padding_left), int(padding_right), cv2.BORDER_CONSTANT)

        b_src = b_image[0:b_size, 0:b_size]
        roi_bg = cv2.bitwise_and(b_src,  b_src, mask=b_mask)
        roi_fg = cv2.bitwise_and(f_image, f_image, mask=f_mask)
        dst = cv2.add(roi_bg, roi_fg)

        finalPath = os.path.join(os.path.expanduser("~"), 'Documents/GitHub/Quiz_Avengers/photos/vingador.png')
        cv2.imwrite(finalPath, dst)
        cv2.waitKey()
        cv2.destroyAllWindows()
        break

        #return None
