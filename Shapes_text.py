import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)

blank[:]=0,255,0
cv.imshow('Green',blank)

blank[:]=0,0,40
cv.imshow('Green_',blank)

# Draw a rectangle

cv.rectangle(blank,(0,0),(250,250),(0,250,0),thickness=cv.FILLED)
cv.imshow('rectangle',blank)


cv.circle(blank,(250,250),40,(250,250,250),thickness=cv.FILLED)
cv.imshow('circle',blank)

cv.line(blank,(0,0),(250,250),(0,250,0),thickness=3)
cv.imshow('line',blank)

# Write text
cv.putText(blank,'Hello',(50,50),cv.FONT_HERSHEY_PLAIN,5.0,(10,10,10))
cv.imshow('Text',blank)
cv.waitKey(0)
