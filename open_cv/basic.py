import cv2 as cv 
from pathlib import Path

#load image
path = Path("../images/traffic_newyork.webp")
img = cv.imread(path)
cv.imshow('Original',img)

#GRAY SCALE
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

#blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
#cv.imshow('Blur',blur)

#EDGE CASCADE
#edge detection - edge detection is a technique used to identify and locate sharp discontinuities in an image
#edge detection algorithms are applied in itrative manner where each iteration refines the output
canny = cv.Canny(blur, 125, 175)
#cv.imshow('Canny Edge', canny)

#DIALATING IMAGES
#Dilation is a morphological operation used in image processing that typically enlarges the boundaries of objects in an image.
#Dilating an image means making the objects in the image appear thicker or more prominent.
#It is particularly useful for filling in small holes and gaps in an object, connecting disjoint objects, and expanding the features in binary or grayscale images.
dilated = cv.dilate(img, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

#ERODED
eroded = cv.erode(dilated, (3,3), iterations=1)
#cv.imshow('Eroded', eroded)

#Resize
resize = cv.resize(img, (256,256), interpolation=cv.INTER_AREA)
#cv.imshow('Resized',resize)
#cv.INTER_AREA - used in cases of redusing size
#cv.INTER_LINEAR - used in cases of incresing size
#cv.INTER_CUBIC - gives high quality but slow

#Cropping
croped = img[50:200, 200:400]
#cv.imshow('Cropped', croped)

cv.waitKey(0)
cv.destroyAllWindows()