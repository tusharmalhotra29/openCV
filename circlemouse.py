import cv2
import numpy as np

cap=cv2.VideoCapture(0)
color=(255,0,0)
line_width=2
radius=100
point=(0,0)

def Click(event, x, y, flags, param):
    global point,pressed
    if(event==cv2.EVENT_LBUTTONDOWN):
        print("button pressed",x,y)
        point(x,y)

cv2.setMouseCallback("Button",Click)

while(True):
    res,frame=cap.read()
    cv2.circle(frame,point,radius,color,line_width)

    cv2.imshow("Frame",frame)

    if cv2.waitKey(10) & 0xFF==ord('q'):
        break