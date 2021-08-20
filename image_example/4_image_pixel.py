import numpy as np
import cv2

img = cv2.imread('images/hallstatt.jpg')
cv2.imshow('original', img)

subimg = img[300:400, 350:750]
cv2.imshow('cutting', subimg)
