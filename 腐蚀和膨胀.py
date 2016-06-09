#coding=utf-8
import cv2
import numpy as np
 
img = cv2.imread('D:/MY Paper/moon.jpg',0)
#OpenCV定义的结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))

#腐蚀图像
eroded = cv2.erode(img,kernel)
#显示腐蚀后的图像
cv2.imshow("Eroded Image",eroded);

#膨胀图像
dilated = cv2.dilate(img,kernel)
#显示膨胀后的图像
cv2.imshow("Dilated Image",dilated);
#原图像
cv2.imshow("Origin", img)


cv2.waitKey(0)
cv2.destroyAllWindows()
