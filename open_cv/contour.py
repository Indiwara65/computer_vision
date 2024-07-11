import cv2 as cv
from pathlib import Path

#Edges vs Contours
#Edge - Edges represent the boundaries between different regions of an image where there is a significant change in intensity or color.
#Contour - Contours are curves that join all the continuous points along a boundary with the same color or intensity.

#load image
path = Path("../images/traffic_light.webp")
img = cv.imread(path)
cv.imshow('Original',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Grayscale',gray)

blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
#cv.imshow('Blured Grayscale', blur)

#CONTOUR DETECTION USING EDGE DETECTION
canny = cv.Canny(gray, 125, 175)    #blur is used to reduce the no of contours
#cv.imshow('Cany Edge', canny)

contours, hierarchies = cv.findContours(canny, mode=cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_SIMPLE)
print(f"# contours = {len(contours)}")
#mode - 
#RETE_EXTERNAL - returns only the external contours
#RETR_HIERARCHIES - returns only hierarchical contours
#RETR_LIST - returns all contours
#method-
#CHAIN_APPROX_NONE - returns all the points of the contour
#CHAIN_APPROX_SIMPLE - returns the endpoints of countor line

img_copy = img.copy()
cv.drawContours(img_copy, contours, contourIdx=-1, color=(0,255,0), thickness=2)
cv.imshow('Contour_Edge', img_copy)

#CONTOUR DETECTION USING THRESHOLD 
ret, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Tresh', thresh)

contours, hierarchies = cv.findContours(thresh, mode=cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_SIMPLE)
print(f"2. # contours = {len(contours)}")

img_copy = img.copy()
cv.drawContours(img_copy, contours, contourIdx=-1, color=(0,255,0), thickness=2)
cv.imshow('Contours_Tresh', img_copy)

cv.waitKey(0)
cv.destroyAllWindows()