import cv2
import numpy as np

lowThreshold = 0
max_lowThreshold = 200
ratio = 3
kernel_size = 3

detected_edges = cv2.GaussianBlur(gray,(3,3),0)
detected_edges = cv2.Canny(detected_edges,50,200)

img = cv2.imread('D:/MY Paper/Result/zhifang.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Canny',detected_edges)
cv2.waitKey(0)
cv2.imwrite('D:/MY Paper/Result/canny1.jpg',detected_edges)
