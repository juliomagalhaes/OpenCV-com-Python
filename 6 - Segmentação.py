import cv2
import numpy as np


##Em visão computacional, segmentação se refere ao processo de dividir
##uma imagem digital em múltiplas regiões (conjunto de pixels) ou objetos,
##com o objetivo de simplificar e/ou mudar a representação de uma imagem
##para facilitar a sua análise.

img = cv2.imread('bookpage.jpg')
cv2.imshow('original',img)

retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold',threshold)


grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold',threshold)

th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('Adaptive threshold',th)

retval2,threshold2 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Otsu threshold',threshold2)

cv2.waitKey(0)
cv2.destroyAllWindows()
