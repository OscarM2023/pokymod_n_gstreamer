import cv2
import numpy as np

cap = cv2.VideoCapture('test4.webm')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Escala de grises y desenfoque
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(frame, (11,11), 0)

    # Detección de bordes
    edges = cv2.Canny(blur, 100, 200)

    # Encontrar contornos en la imagen de bordes
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow('Detector de bordes',edges)
    
    for cnt in contours:

        area = cv2.contourArea(cnt)
        if area < 100: 
            continue    # Descartar contornos con areas pequeños 
        
        epsilon = 0.05 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True) # Aproxima contorno a un poligono
        # Verificar que tenga cuatro lados y sea convexo
        if len(approx) == 4 and cv2.isContourConvex(approx):
            cv2.drawContours(frame, [approx], 0, (0,255,0), 3)

    # Mostrar imagen
    cv2.imshow('Deteccion de cajas', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()