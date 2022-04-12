import cv2
import numpy as np

img = cv2.imread('n2.jpg')
img = cv2.resize(img,(800,480))

median_blur = cv2.medianBlur(img,3)

for i in range(0,3):
    median_blur = cv2.medianBlur(median_blur,3)

cv2.imshow('med',median_blur)

clear_image = cv2.edgePreservingFilter(median_blur,2)
cv2.imshow('clear image',clear_image)

bilateral_blur = cv2.bilateralFilter(clear_image,6,10,10)
for i in range(0,2):
    bilateral_blur = cv2.bilateralFilter(bilateral_blur,6,10,10)
cv2.imshow('bilateral',bilateral_blur)

guassian_blur = cv2.GaussianBlur(bilateral_blur,(3,3),0)
cv2.imshow('Guassian',guassian_blur)

sharped = cv2.addWeighted(clear_image,2.5,guassian_blur,-1.5,0)
sharped = cv2.addWeighted(sharped,1.4,guassian_blur,-0.4,5)
cv2.imshow('sharped',sharped)

final = cv2.medianBlur(sharped,1)
final = cv2.addWeighted(sharped,1,guassian_blur,-0,0)
cv2.imshow('final',final)
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

