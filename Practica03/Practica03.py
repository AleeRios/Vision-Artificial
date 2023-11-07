# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: REDES NEURONALES
Tema: PRÁCICA 03
Alumno: Rios Campusano Beckham Alejandro
Profesor: Dr. Asdrúbal López Chau
Descripción: Detección de poligonos

Created on Thu Sep  9 19:55:50 2021

@author: alebe
"""

import cv2
from matplotlib import pyplot as plt


def cargarImg(ruta):
    "Carga una imagen en Blanco y Negro"
    imagen = cv2.imread(ruta)
    return imagen

def mostrar(imagen, titulo):
    "Muestra una imagen, el titulo=String"
    #cv2.imshow(titulo,imagen)
    #cv2.waitKey(0)
    plt.title(titulo)
    plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
    plt.show()    

def bordes(img): #funcion para bordes
    "Encuentra los borde con Canny"
    canny = cv2.Canny(img, 10, 150)
    canny = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, (3, 3), iterations=1)
    return canny

def detectarFiguras(img, img2):
    cnts,_ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    #epsilon=0
    for i in cnts:
        epsilon = 0.01 * cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, epsilon, True)
        x, y, w, h = cv2.boundingRect(approx)
        
        #Triangulo
        if len(approx) == 3:
            corte = img2[y-5:y+h+5,x-5:x+w+5]
            cv2.imwrite("Triangulo.png",corte)
            cv2.putText(img2, "Triangulo", (x,y-5), 1, 1.5, (0,255,0), 2)
            print("\n\n\t\tTriangulo")
            print("\nNumero de lados: ",len(approx))
            print("Centro: "+str(int(w/2))+", "+str(int(h/2)))
            print("x Maxima: ",x+w)
            print("x Minima: ",x)
            print("y Maxima: ",y+h)
            print("y Minima: ",y)
            print("Tamaño en pixeles: ",w*h)
            
        # Cuadrado o Rectangulo
        if len(approx) == 4:
            aspect = float(w)/h
            #print("Aspecto = ",aspect)
            if aspect == 1:
                corte = img2[y-5:y+h+5,x-5:x+w+5]
                cv2.imwrite("Cuadrado.png",corte)
                cv2.putText(img2, 'Cuadrado', (x,y-5), 1, 1.5, (0,255,0), 2)
                print("\n\n\t\tCuadrado")
                print("\nNumero de lados: ",len(approx))
                print("Centro: "+str(int(w/2))+", "+str(int(h/2)))
                print("x Maxima: ",x+w)
                print("x Minima: ",x)
                print("y Maxima: ",y+h)
                print("y Minima: ",y)
                print("Tamaño en pixeles: ",w*h)
            else:
                corte = img2[y-5:y+h+5,x-5:x+w+5]
                cv2.imwrite("Rectangulo.png",corte)
                cv2.putText(img2, 'Rectangulo', (x,y-5), 1, 1.5, (0,255,0), 2)
                print("\n\n\t\tRectangulo")
                print("\nNumero de lados: ",len(approx))
                print("Centro: "+str(int(w/2))+", "+str(int(h/2)))
                print("x Maxima: ",x+w)
                print("x Minima: ",x)
                print("y Maxima: ",y+h)
                print("y Minima: ",y)
                print("Tamaño en pixeles: ",w*h)
        
        #Pentágono
        if len(approx) == 5:
            corte = img2[y-5:y+h+5,x-5:x+w+5]
            cv2.imwrite("Pentagono.png",corte)
            cv2.putText(img2, 'Pentagono', (x,y-5), 1, 1.5, (0,255,0), 2)
            print("\n\n\t\tPentangono")
            print("\nNumero de lados: ",len(approx))
            print("Centro: "+str(int(w/2))+", "+str(int(h/2)))
            print("x Maxima: ",x+w)
            print("x Minima: ",x)
            print("y Maxima: ",y+h)
            print("y Minima: ",y)
            print("Tamaño en pixeles: ",w*h)
        
        #Hexagono
        if len(approx) == 6:
            corte = img2[y-5:y+h+5,x-5:x+w+5]
            cv2.imwrite("Hexagono.png",corte)
            cv2.putText(img2, 'Hexagono', (x,y-5), 1, 1.5, (0,255,0), 2)
            print("\n\n\t\tHexagono")
            print("\nNumero de lados: ",len(approx))
            print("Centro: "+str(int(w/2))+", "+str(int(h/2)))
            print("x Maxima: ",x+w)
            print("x Minima: ",x)
            print("y Maxima: ",y+h)
            print("y Minima: ",y)
            print("Tamaño en pixeles: ",w*h)
        
        #Circulo
        if len(approx) > 10:
            corte = img2[y-5:y+h+5,x-5:x+w+5]
            cv2.imwrite("Circulo.png",corte)
            cv2.putText(img2, 'Circulo', (x,y-5), 1, 1.5, (0,255,0), 2)
            print("\n\n\t\tCirculo")
            print("\nNumero de lados: ",len(approx))
            print("Centro: "+str(int(w/2))+", "+str(int(h/2)))
            print("x Maxima: ",x+w)
            print("x Minima: ",x)
            print("y Maxima: ",y+h)
            print("y Minima: ",y)
            print("Tamaño en pixeles: ",w*h)
        
        cv2.drawContours(img2, [approx], 0, (0,255,0), 2)    
    return img2

def main():
    img = cargarImg("poligonos.png")
    mostrar(img, "Original")
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = bordes(gris) # Binarizar y extraer bordes
    fig = detectarFiguras(canny,img) # Detectar figuras
    mostrar(fig, "Contornos")
    
main()