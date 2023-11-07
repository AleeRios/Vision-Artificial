#Rios Campusano Beckham Alejandro
#Vazquez Bravo Emmanuel
#Garduño Sanchez Bladimir Axley

import cv2
import matplotlib.pyplot as plt
from tabulate import tabulate as tb

def cargarImg(ruta):
    imagen=cv2.imread(ruta,0)
    return imagen

def mostrar(imagen,titulo): #funcion para mostrar imagenes
    #cv2.imshow(titulo,imagen)
    #cv2.waitKey(0)
    plt.title(titulo)
    plt.imshow(cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB))
    plt.show()
    
def binarizar(img): #funcion para binarizar imagenes
    ret1, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return img

def contornos(img): #funcion para contornos
    gauss=cv2.GaussianBlur(img,(3,3),0)
    canny=cv2.Canny(gauss,127,255)
    return canny

def momentos(img):
    cont,jera=cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    m=cv2.moments(cont[0])
    tabla.append([m['m00'],m['m10'],m['m01'],m['m11']])
    return tb(tabla,headers=['m00','m10','m01','m11'],showindex=True)
    
    
img=cargarImg("C:/Users/alebe/Documents/Python Scripts/Vision/Hojas/1001.jpg")
mostrar(img,"Original")

imgbinaria=binarizar(img)
mostrar(imgbinaria,"Binaria")
imgcontornos=contornos(img)
mostrar(imgcontornos,"Bordes")
tabla=[]

momentos(imgbinaria)
tbl=momentos(imgcontornos)
print(tbl)
