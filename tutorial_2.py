#Resizing Image
import cv2
import os

img = cv2.imread(os.path.join('.','assets','images.jpg'))
print(img.shape)

#changing image size
resize_image = cv2.resize(img, (320,512))
print(resize_image.shape)

#visualizing Image
cv2.imshow('image 1', img)
cv2.imshow('image 2', resize_image)

cv2.waitKey(0)