import cv2 as cv
from pathlib import Path

#Read images and display from local files
path = Path("../images/traffic_newyork.webp")
img = cv.imread(path)               #image will be loaded as a numpy array
cv.imshow('Traffic', img)
cv.waitKey(0)
cv.destroyAllWindows()

#Read videos
path = Path("../videos/daschcam_video.webm")
capture = cv.VideoCapture(path)
while True:
    isTrue, frame = capture.read()   #isTrue - a bolean value indicating if a frame was read, frame - read frame(numpy array)
    ##show frame
    cv.imshow('Video', frame)
    ##break if 'd' key is pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()