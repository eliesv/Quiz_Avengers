# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:30:15 2018
@author: Freddy Dratwa
"""
import cv2

def camera(vingador, imagem):
        
    face_cascade = cv2.CascadeClassifier(r"C:/Users/elies/Desktop/PF/opencv/sources/data/haarcascades_cuda/haarcascade_frontalface_default.xml")
    foreground_image = cv2.imread('{}.png'.format(vingador), -1)
    
    foreground_mask = foreground_image[:, :, 3] 
    background_mask = cv2.bitwise_not(foreground_mask)  
    foreground_image = foreground_image[:, :, 0:3] 
    
    foreground_size = 570
    foreground_ratio = float(foreground_size)  
    
    background_size = 2000 
    
    padding_top = ((background_size - foreground_size) / 3) * 2
    padding_bottom = background_size - padding_top
    padding_left = (background_size - foreground_size) / 2
    padding_right = (background_size - foreground_size) / 2
    
    #nome e local da image com o rosto
    cv_image = cv2.imread("{}".format(imagem)) 
       
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
       
        ratio = foreground_ratio / face_roi.shape[1]
        dimension = (foreground_size, int(face_roi.shape[0] * ratio))
        face = cv2.resize(face_roi, dimension, interpolation = cv2.INTER_AREA)  
          
        background_image = cv2.copyMakeBorder(face, int(padding_top), int(padding_bottom), int(padding_left), int(padding_right), cv2.BORDER_CONSTANT)  
    
        background_src = background_image[0:background_size, 0:background_size]  
        roi_bg = cv2.bitwise_and( background_src,  background_src, mask=background_mask)  
        roi_fg = cv2.bitwise_and(foreground_image, foreground_image, mask=foreground_mask)
        dst = cv2.add(roi_bg, roi_fg) 
        #nome e local do arquivo salvo
        cv2.imwrite("vingador.png", dst) 
        cv2.waitKey()
        cv2.destroyAllWindows()
        break

    return None
camera("Iron man","rr.jpg")     