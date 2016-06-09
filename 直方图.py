#coding=utf-8
import cv2
import numpy as np  

img = cv2.imread('D:/MY Paper/a.jpg', 0)
equ = cv2.equalizeHist(img)  
cv2.imshow('eq',equ)
cv2.waitKey(0)
cv2.imwrite('D:/MY Paper/aaaaaaa.jpg', equ) 
