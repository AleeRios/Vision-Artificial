# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: REDES NEURONALES
Tema: PRÁCTICA 02
Alumno: Rios Campusano Beckham Alejandro
Profesor: Dr. Asdrúbal López Chau
Descripción: Detección de líneas y círculos transformada de Houg 

Created on Tue Sep  7 00:43:03 2021

@author: alebe
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

def cargarImg(ruta,n):
    "Carga una imagen n=1=Color, n=0=B/N"
    imagen=cv2.imread(ruta,n)
    return imagen

def mostrar(imagen,titulo): #funcion para mostrar imagenes
    "Muestra una imagen, el titulo=String"
    #cv2.imshow(titulo,imagen)
    #cv2.waitKey(0)
    plt.title(titulo)
    plt.imshow(cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB))
    plt.show()
    
def binarizar(img): #funcion para binarizar imagenes
    "Binariza imagen con el metodo OTSU"
    ret1, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return img

def bordes(img): #funcion para bordes
    "Encuentra los borde con Canny"
    gauss=cv2.GaussianBlur(img,(3,3),0)
    canny=cv2.Canny(gauss,127,255)
    return canny

def lineas(img,img2):
    "Detecta lineas de una imagen img=Imagen bordes, img2= Imagen original"
    line=cv2.HoughLines(img,1,np.pi/180,200)
    
    for i in line:
        rho,teta=i[0]
        a=np.cos(teta)
        b=np.sin(teta)
        x0=a*rho
        y0=b*rho
        x1=int(x0 + 1000*(-b))
        y1=int(y0 + 1000*(a))
        x2=int(x0 - 1000*(-b))
        y2=int(y0 - 1000*(a))
        cv2.line(img2,(x1,y1),(x2,y2),(255,0,0),1,cv2.LINE_AA)
    return img2

def circulos(img,img2):
    "Detecta circulos de una imagen img=Imagen bordes, img2=Imagen original"
    #img=cv2.medianBlur(img,5)
    #img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    circulo=cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
    circulo=np.uint16(np.around(circulo))
    
    for i in circulo[0,:]:
        cv2.circle(img2,(i[0],i[1]),i[2],(0,255,0),2)
        cv2.circle(img2,(i[0],i[1]),2,(0,0,255),3)
    return img2

def mainLineas():
    img=cargarImg("sudoku.jpg",0)
    mostrar(img,"Original")
    borde=bordes(binarizar(img))
    img=cargarImg("sudoku.jpg",1)
    mostrar(lineas(borde,img),"Lineas")

def mainCirculos():
    img=cargarImg("circulos.jpg",0)
    mostrar(img,"Original")
    borde=bordes(binarizar(img))
    img2=cargarImg("circulos.jpg",1)
    mostrar(circulos(borde,img2),"Circulos")

mainLineas()
mainCirculos()