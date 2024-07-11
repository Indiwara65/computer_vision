import cv2 as cv
import numpy as np

#create blank image
blank = np.zeros((512,512,3), dtype='uint8')
cv.imshow('Blank',blank)

#1. Fill the image  with a color
filled_blank = blank.copy()
filled_blank[:]= 0,255,0
cv.imshow('Filled',filled_blank)

#2. Fill a part of the image
filled_blank = blank.copy()
filled_blank[255:511, 255:511] = 0,255,255
cv.imshow('Partially Filled',filled_blank)

#3.Draw rectangles
rect = blank.copy()
cv.rectangle(rect,(205,205),(305,305),(0,255,0),thickness=2)
cv.imshow('Rectangle',rect)

#4.Draw rectagles filled
rect = blank.copy()
cv.rectangle(rect,(205,205),(305,305),(0,255,0),thickness=-1)
cv.imshow('Filled Rectangle',rect)

#5. Draw circle
circle = blank.copy()
cv.circle(circle,(256,256), 50,(0,255,0),thickness=2) #by setting thickness to -1 
cv.imshow('circle',circle)

#6. Draw line
line = blank.copy()
cv.line(line, (200,200),(400,400),(0,255,255),thickness=2)
cv.imshow('line',line)

#7. Text
text = blank.copy()
cv.putText(text, 'Hello', (230,230), cv.FONT_HERSHEY_COMPLEX, 0.1, (0,0,255))
cv.imshow('Text',text)

cv.waitKey(0)
cv.destroyAllWindows()