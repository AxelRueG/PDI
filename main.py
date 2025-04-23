import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
from skimage.draw import line

image = io.imread('./imagenes/ezeiza1.jpg', as_gray=True)

def click_rectangle(event, x, y, flags, param):
    global pt
    if event == cv2.EVENT_LBUTTONDOWN:
        pt = [x,y]
    elif event == cv2.EVENT_LBUTTONUP:
        pt.append(x)
        pt.append(y)
        # linea arbitraria
        yy, xx = line(pt[1],pt[0],pt[3],pt[2])
        perfil = image.copy()[yy,xx]

        # dibujamos
        cv2.line(image, pt[0:2], pt[2:], (0,0,0), 2)
        cv2.imshow('draw rectangle', image)
        
        plt.plot(perfil)
        plt.show()


cv2.namedWindow('draw rectangle')
cv2.setMouseCallback('draw rectangle', click_rectangle)

while True:
    cv2.imshow('draw rectangle', image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        break
