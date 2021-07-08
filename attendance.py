import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime



#step 1 same: import images and convert to rgb

path='Resources/attendance1'
images=[]
classNames=[]
myList=os.listdir(path)
print(myList)
for cls in myList:
    curImg=cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
print(classNames)

#now we'll start the encoding of images

def FindEncoding(images):
    encodelist=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

encodelistknown=FindEncoding(images)
#print(encodelistknown)
print("encoding complete")
#step 3 find matches between encodings

cap=cv2.VideoCapture(0)

while True:
    success,img=cap.read()
    imgS=cv2.resize(img,(0,0),None,0.25,0.25)
    imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    facCurframe=face_recognition.face_locations(imgS)
    encodecurframe=face_recognition.face_encodings(imgS,facCurframe)

    for encodeFace,faceLoc in zip(encodecurframe,facCurframe):
        matches=face_recognition.compare_faces(encodelistknown,encodeFace)
        facedist=face_recognition.face_distance(encodelistknown,encodeFace)
        print(matches)
        matchindex=np.argmin(facedist)


        if matches[matchindex]:
            name=classNames[matchindex].upper()
            print(name)
    cv2.imshow("match",img)
    cv2.waitKey(1)



#faceLoc=face_recognition.face_locations(imgelon)[0]
#encodeElon=face_recognition.face_encodings(imgelon)[0]
#cv2.rectangle(imgelon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,255,0),2)

#faceLoctest=face_recognition.face_locations(imgtest)[0]
#encodeElontest=face_recognition.face_encodings(imgtest)[0]
#cv2.rectangle(imgtest,(faceLoctest[3],faceLoctest[0]),(faceLoctest[1],faceLoctest[2]),(255,255,0),2)

#results=face_recognition.compare_faces([encodeElon],encodeElontest)
#facedis=face_recognition.face_distance([encodeElon],encodeElontest)