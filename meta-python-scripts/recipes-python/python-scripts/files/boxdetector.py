import cv2
import numpy as np
import math


def sobel_edge_detection(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.sqrt(sobelx**2 + sobely**2)
    edged = cv2.convertScaleAbs(sobel_combined)
    _, edged = cv2.threshold(edged, 80, 255, cv2.THRESH_BINARY)
    _, thresholded = cv2.threshold(edged, 30, 255, cv2.THRESH_BINARY)
    return thresholded



def draw_boxes(frame, edged) -> cv2.Mat:
    contours, _ = cv2.findContours(
        edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0.0
    max_area_index = -1
    for i, contour in enumerate(contours):
        hull = cv2.convexHull(contour)
        area = cv2.contourArea(hull)
        if area < 400:
            continue
        if max_area < area:
            max_area = area
            max_area_index = i

    if max_area_index != -1:
        contour = contours[max_area_index]
        x, y, w, h = cv2.boundingRect(contour)
        rect = cv2.minAreaRect(contour)
        x, y = rect[0]
        w, h = rect[1]
        w = max(w, h)
        h = min(w, h)
        ang = rect[2]

    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 1000:
            continue

        hull = cv2.convexHull(contour)
        x, y, w, h = cv2.boundingRect(hull)
        x = int(x)
        y = int(y)
        w = int(w)
        h = int(h)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame


cap = cv2.VideoCapture('test.mp4')

# Crear VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS) or 30     # FPS (si la cámara no lo da, usamos 30)
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Escala de grises y desenfoque

    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    edges = sobel_edge_detection(frame)

    mask = np.zeros(frame.shape, np.uint8)

    cv2.imshow('Deteccion de bordes', edges)

    # Encontrar contornos en la imagen de bordes
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for contour in contours:
            hull = cv2.convexHull(contour)
            cv2.drawContours(mask, [hull], -1, (255, 255, 255), -1)

    edged_out = cv2.bitwise_and(frame, mask)


    result_frame = draw_boxes(frame, edges)
    out.write(result_frame) 


    # Mostrar imagen
    cv2.imshow('Deteccion de cajas', result_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()