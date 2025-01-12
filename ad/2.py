import cv2
import numpy as np
base = np.zeros((600,900,3),np.uint8)
img1 = cv2.imread('img1.png')
img2 = cv2.imread('img2.png')
img3 = cv2.imread('img3.png')
img4 = cv2.imread('img4.png')
img5 = cv2.imread('img5.png')
img6 = cv2.imread('img6.png')
img7 = cv2.imread('img7.png')
img8 = cv2.imread('img8.png')
img9 = cv2.imread('img9.png')

img1 = cv2.resize(img1, (300,200))
base[0:200, 0:300] = img1
img2 = cv2.resize(img2, (300,200))
base[200:400,0:300] = img2
img3 = cv2.resize(img3, (300,200))
base[400:600,0:300] = img3
img4 = cv2.resize(img4, (300,200))
base[0:200,300:600] = img4
img5 = cv2.resize(img5, (300,200))
base[200:400,300:600] = img5
img6 = cv2.resize(img6, (300,200))
base[400:600,300:600] = img6
img7 = cv2.resize(img7, (300,200))
base[0:200,600:900] = img7
img8 = cv2.resize(img8, (300,200))
base[200:400,600:900] = img8
img9 = cv2.resize(img9, (300,200))
base[400:600,600:900] = img9

cv2.imshow('base', base)

cv2.waitKey(0)