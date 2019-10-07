import cv2
import numpy as np

a=0
a=int(input('Enter 1 for Video Cam else 0 '))

if a==1:
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret,frame=cap.read()
    else:
        ret=False
else:
    frame=cv2.imread('color_circle.jpg')
    frame=cv2.resize(frame,(512,512))

def func(x):
    pass

cv2.namedWindow('image')
lh,ls,lv,hh,hs,hv=100,50,50,40,205,205


cv2.createTrackbar('LH','image',100,179,func)
cv2.createTrackbar('LS','image',50,255,func)
cv2.createTrackbar('LV','image',50,255,func)
cv2.createTrackbar('HH','image',40,179,func)
cv2.createTrackbar('HS','image',205,255,func)
cv2.createTrackbar('HV','image',205,255,func)

while True:
    if a==1:
        ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lh=cv2.getTrackbarPos('LH','image')
    ls=cv2.getTrackbarPos('LS','image')
    lv=cv2.getTrackbarPos('LV','image')
    hh=cv2.getTrackbarPos('HH','image')
    hs=cv2.getTrackbarPos('HS','image')
    hv=cv2.getTrackbarPos('HV','image')

    lower=np.array([lh,ls,lv])
    higher=np.array([lh+hh,ls+hs,lv+hv])

    mask=cv2.inRange(frame,lower,higher)
    inv_mask=cv2.bitwise_not(mask)

    color=cv2.bitwise_and(frame,frame,mask=mask)
    remaining=cv2.bitwise_and(frame,frame,mask=inv_mask)
    cv2.imshow('image',mask)
    cv2.imshow('original',frame)
    cv2.imshow('color',color)
    cv2.imshow('remaining',remaining)
    if cv2.waitKey(1)==27:
        break
    if cv2.waitKey(1)==ord('p'):
        print('lower : ({},{},{})'.format(lh,ls,lv))
        print('higher : ({},{},{})'.format(lh+hh,ls+hs,lv+hv))
cv2.destroyAllWindows()
if a==1:
    cap.release()
    
