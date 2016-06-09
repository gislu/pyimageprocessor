#coding=utf-8
import cv2
import numpy as np

img = cv2.imread('D:/MY Paper/moon.jpg')
median = cv2.medianBlur(img, 5)
cv2.imshow("First", img)
cv2.imshow("Median", median)
cv2.waitKey(0)
cv2.imwrite('D:/MY Paper/midfinal.jpg',median)
