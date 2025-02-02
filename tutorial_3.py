
import cv2
import os

img = cv2.imread(os.path.join('.','assets','images.jpg'))


#Cropping Image
cropped_img = img[30:640, 250:700]
#print(img.shape)
# cv2.imshow('image 1', img)
# cv2.imshow('image 2', cropped_img)
# print(cropped_img.shape)
# cv2.waitKey(0)


# ColorSpaces of Images

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# cv2.imshow('image 1', img)
# cv2.imshow('image 2', img_gray)
# cv2.imshow('image 3', img_rgb)
# cv2.imshow('image 4', img_hsv)
# cv2.waitKey(0)


# Blurring Images

k_size = 7
class_blur = cv2.blur(img, (k_size,k_size))
gaussian_blur = cv2.GaussianBlur(img , (k_size,k_size), 3)
median_blur = cv2.medianBlur(img, k_size)

# cv2.imshow('image 1', img)
# cv2.imshow('image 2', class_blur)
# cv2.imshow('image 3', gaussian_blur)
# cv2.imshow('image 4', median_blur)
# cv2.waitKey(0)


# Thresholding