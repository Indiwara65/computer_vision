import cv2 as cv 
from pathlib import Path

#Resacling and resizing of images and videos to reduce computational strain.
#ReScaling - scales the images hieght and width by the same factor, by rescaling the images aspect ratio remains constant.
#ReSizing - chaging the images hieght and width to a specified size


#ReScaling
def rescale(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimentions = (width, height)
    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)          #interpolation - algorithm 

##Image Re Scaling
#load image
path = Path("../images/traffic_newyork.webp")
img = cv.imread(path)            
img_resized = rescale(img, 0.5)
cv.imshow('Traffic', img)
cv.imshow('Traffic Rescaled', img_resized)
cv.waitKey(0)
cv.destroyAllWindows()

##Video Rescaling (Method-1)
#load video 
path = Path("../videos/daschcam_video.webm")
capture = cv.VideoCapture(path)

#paly video
while True:
    isTrue, frame = capture.read()
    frame_resized = rescale(frame, 0.5)
    cv.imshow('Video', frame)
    cv.imshow('Video Re-Scaled', frame_resized)
    
    #print(frame.shape)
    #print(frame_resized.shape)
    #print('\n')

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

##Video Rescaling (Method-2)
#this method only works for Live Video
#capture.set(3, WIDTH)
#capture.set(4, HEIGHT)
