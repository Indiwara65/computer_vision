import cv2 as cv
import numpy as np
from pathlib import Path

#load image
path = Path("../images/traffic_newyork.webp")
img = cv.imread(path)
cv.imshow('Original',img)

# TRANSLATION
# The process of moving an image from one location to another
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimentions = (img.shape[1], img.shape[0])       #(width, height)
    return cv.warpAffine(img, transMat, dimentions)

#-x --> Left
#-y --> Up
#+x --> Right
#+y --> Down

img_tra = translate(img, 200, 200)
#cv.imshow('Translated', img_tra)

#ROTATION
#Rotate aroung a point by a certain angle
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint == None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(center=rotPoint, angle=angle, scale=1.0)
    dimentions = (width,height)
    return cv.warpAffine(img, rotMat, dimentions)

rot_img = rotate(img, 90)
#cv.imshow('Rotated', rot_img)

#RESIZE
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resized)

#FLIPPING
flip = cv.flip(img, 1)        #flip horizontally
flip = cv.flip(img, 0)        #flip vertically
flip = cv.flip(img, -1)       #flip both horizontally and vertically
#cv.imshow('Flipped', flip)

#CROPPING
cropped = img[200:400,200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
cv.destroyAllWindows()