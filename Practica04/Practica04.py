# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: VISIÓN ARTIFICIAL
Tema: Práctica 04
Alumno: Rios Campusano Beckham Alejandro
Profesor: M. en C. Rafael Rojas Hernandez
Descripción: Realizar la detección de rostros para imágenes fijas o imágenes de
vídeo.

Created on Tue Sep 28 18:08:42 2021

@author: alebe
"""

import cv2
import mediapipe as mp

def imgFija():
    deteccion = mp.solutions.face_detection
    dibujar = mp.solutions.drawing_utils
    
    with deteccion.FaceDetection(min_detection_confidence=0.5) as face_detection:
        imagen = cv2.imread("Rostro1.jpg")
        h, w, _ = imagen.shape
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        r = face_detection.process(gris)
        #print("Deteccion: ",r.detections)
        
        if r.detections is not None:
            for i in r.detections:
                dibujar.draw_detection(imagen, i, dibujar.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=1),dibujar.DrawingSpec(color=(0,255,0), thickness=2))
        
        cv2.imshow("Imagen", imagen)
        cv2.waitKey(0)
    cv2.destroyAllWindows()

def imgVideo():
    deteccion = mp.solutions.face_detection
    dibujar = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    
    with deteccion.FaceDetection(min_detection_confidence=0.5) as face_detection:
        while True:
            ret, frame = cap.read()
            if ret == False:
                break
            
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            r = face_detection.process(frame_rgb)
            
            if r.detections is not None:
                for i in r.detections:
                    dibujar.draw_detection(frame, i, dibujar.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=1),dibujar.DrawingSpec(color=(0,255,0), thickness=2))
            
            cv2.imshow("Frame", frame)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
    cap.release()
    cv2.destroyAllWindows()

def segundaParte():
    deteccion = mp.solutions.face_detection
    dibujar = mp.solutions.drawing_utils
    
    with deteccion.FaceDetection(min_detection_confidence=0.5) as face_detection:
        imagen = cv2.imread("Rostro2.jpg")
        h, w, _ = imagen.shape
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        r = face_detection.process(gris)
        print("Deteccion: ",r.detections)
        
        if r.detections is not None:
            for i in r.detections:
                dibujar.draw_detection(imagen, i, dibujar.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=1),dibujar.DrawingSpec(color=(0,255,0), thickness=2))
                #Tamaño del cuadrado
                #xmin = int(i.location_data.relative_bounding_box.xmin * w)
                #ymin = int(i.location_data.relative_bounding_box.xmin * h)
                #wi = int(i.location_data.relative_bounding_box.width * w)
                #he = int(i.location_data.relative_bounding_box.height * h)
                #cv2.rectangle(imagen, (xmin, ymin), (xmin+wi, ymin+he), (0,255,0),2)
                
                #Ojos
                ojoDx = int(i.location_data.relative_keypoints[0].x * w)
                ojoDy = int(i.location_data.relative_keypoints[0].y * h)
                cv2.circle(imagen,(ojoDx,ojoDy),20,(0,0,255),2)
                ojoIx = int(i.location_data.relative_keypoints[1].x * w)
                ojoIy = int(i.location_data.relative_keypoints[1].y * h)
                cv2.circle(imagen,(ojoIx,ojoIy),20,(0,0,255),2)
                
                #Boca
                bocaX = int(deteccion.get_key_point(i, deteccion.FaceKeyPoint.MOUTH_CENTER).x * w)
                bocaY = int(deteccion.get_key_point(i, deteccion.FaceKeyPoint.MOUTH_CENTER).y * h)
                cv2.rectangle(imagen, (bocaX-40, bocaY-20), (bocaX+40,bocaY+10), (255,0,0),2)
                
                #Nariz
                narizX = int(deteccion.get_key_point(i, deteccion.FaceKeyPoint.NOSE_TIP).x * w)
                narizY = int(deteccion.get_key_point(i, deteccion.FaceKeyPoint.RIGHT_EAR_TRAGION).y * h)
                cv2.ellipse(imagen, (narizX-3, narizY+10),(20,30),0,0,360,(255,255,0),2)
                
                #Orejas
                oreDX = int(deteccion.get_key_point(i, deteccion.FaceKeyPoint.RIGHT_EAR_TRAGION).x * w)
                oreDY = int(deteccion.get_key_point(i, deteccion.FaceKeyPoint.RIGHT_EAR_TRAGION).y * h)
                cv2.line(imagen,(oreDX-20, oreDY-10), (oreDX, oreDY),(0,255,150),2)
                oreIX = int(deteccion.get_key_point(i, deteccion.FaceKeyPoint.LEFT_EAR_TRAGION).x * w)
                oreIY = int(deteccion.get_key_point(i, deteccion.FaceKeyPoint.LEFT_EAR_TRAGION).y * h)
                cv2.line(imagen,(oreIX+20, oreIY+10), (oreIX, oreIY),(0,255,150),2)
        
        cv2.imshow("Imagen", imagen)
        #cv2.imshow("Imagen", emoji)
        cv2.waitKey(0)
    cv2.destroyAllWindows()

def imgVideo2():
    deteccion = mp.solutions.face_detection
    dibujar = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    
    with deteccion.FaceDetection(min_detection_confidence=0.5) as face_detection:
        while True:
            ret, frame = cap.read()
            if ret == False:
                break
            
            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            r = face_detection.process(frame_rgb)
            h, w, _ = frame.shape
            
            if r.detections is not None:
                for i in r.detections:
                    dibujar.draw_detection(frame, i, dibujar.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=1),dibujar.DrawingSpec(color=(0,255,0), thickness=2))
                    #Ojos
                    ojoDx = int(i.location_data.relative_keypoints[0].x * w)
                    ojoDy = int(i.location_data.relative_keypoints[0].y * h)
                    cv2.circle(frame, (ojoDx,ojoDy), 20, (0,0,255), 2)
                    ojoIx = int(i.location_data.relative_keypoints[1].x * w)
                    ojoIy = int(i.location_data.relative_keypoints[1].y * h)
                    cv2.circle(frame, (ojoIx,ojoIy), 20, (0,0,255), 2)
                    
                    #Boca
                    bocaX = int(deteccion.get_key_point(i, deteccion.FaceKeyPoint.MOUTH_CENTER).x * w)
                    bocaY = int(deteccion.get_key_point(i, deteccion.FaceKeyPoint.MOUTH_CENTER).y * h)
                    cv2.rectangle(frame, (bocaX-40, bocaY-20), (bocaX+40,bocaY+10), (255,0,0),2)
                    
                    #Nariz
                    narizX = int(deteccion.get_key_point(i, deteccion.FaceKeyPoint.NOSE_TIP).x * w)
                    narizY = int(deteccion.get_key_point(i, deteccion.FaceKeyPoint.RIGHT_EAR_TRAGION).y * h)
                    cv2.ellipse(frame, (narizX-3, narizY+10),(20,30),0,0,360,(255,255,0),2)
                    
                    #Orejas
                    oreDX = int(deteccion.get_key_point(i, deteccion.FaceKeyPoint.RIGHT_EAR_TRAGION).x * w)
                    oreDY = int(deteccion.get_key_point(i, deteccion.FaceKeyPoint.RIGHT_EAR_TRAGION).y * h)
                    cv2.line(frame,(oreDX-20, oreDY-10), (oreDX, oreDY),(0,255,150),2)
                    oreIX = int(deteccion.get_key_point(i, deteccion.FaceKeyPoint.LEFT_EAR_TRAGION).x * w)
                    oreIY = int(deteccion.get_key_point(i, deteccion.FaceKeyPoint.LEFT_EAR_TRAGION).y * h)
                    cv2.line(frame,(oreIX+20, oreIY+10), (oreIX, oreIY),(0,255,150),2)
            
            cv2.imshow("Frame", frame)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
    cap.release()
    cv2.destroyAllWindows()

def emoji():
    face = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

    face_mask = cv2.imread("Emoji1.png")

    h_mask, w_mask = face_mask.shape[:2]

    cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)
    escala=0.5

    while True:
        ret,frame=cap.read()
        frame=cv2.resize(frame,None,fx=escala,fy=escala,interpolation=cv2.INTER_AREA)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #frame = cv2.flip(frame, 1)

        face_rects=face.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in face_rects:
            if h>0 and w>0:
                h,w=int(1.35*h),int(1.35*w)
                y-=int(0.1*h)
                x+=int(-0.15*w)

                frame_roi=frame[y:y+h,x:x+w]
                face_mask_small=cv2.resize(face_mask,(w,h),interpolation=cv2.INTER_AREA)

                gray_mask=cv2.cvtColor(face_mask_small,cv2.COLOR_BGR2GRAY)
                ret,mask=cv2.threshold(gray_mask,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
				#ret,mask=cv2.threshold(gray_mask,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

                mask_inv=cv2.bitwise_not(mask)

                masked_face=cv2.bitwise_and(face_mask_small,face_mask_small,mask=mask_inv)

                masked_frame=cv2.bitwise_and(frame_roi,frame_roi,mask=mask_inv)

                frame[y:y+h,x:x+w]=cv2.add(masked_face,masked_frame)

        cv2.imshow("Detector de rostro",frame)
		
        c=cv2.waitKey(1)
        if c==27:
            break

    cap.release()
    cv2.destroyAllWindows()

imgFija()
#imgVideo()
#imgVideo2()
#segundaParte()
#emoji()