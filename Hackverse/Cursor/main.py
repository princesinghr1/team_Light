#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from keras.models import load_model
import numpy as np
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
model=load_model("curmodel")
import pyautogui
pyautogui.FAILSAFE= False


# In[ ]:


Char="0123456789DOU$"

font        = cv2.FONT_HERSHEY_SIMPLEX
location    = (100,50)
fontScale   = 1
fontColor   = (255,255,255)
lineType    = 2


hands = mp_hands.Hands(
    min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)
ccount=20
while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        L=[]
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            land = hand_landmarks
            val = land.landmark
            first=val[0];
            for j in val:
                L.append(j.x-first.x);
                L.append(j.y-first.y);
                L.append(j.z-first.z);
            break
        L=L[3::]
        L=np.array(L)
        x = np.expand_dims(L,0)
        x = np.expand_dims(x,-1)
        fi=int(np.argmax(model.predict(x)))
        if fi==1:
                for hand_landmarks in results.multi_hand_landmarks:
                    land = hand_landmarks
                    val = land.landmark
                    x=val[8].x*l1[0]+l1[1]
                    if(x<0):
                        x=0
                    if(x>1920):
                        x=1920
                    y=val[8].y*l2[0]+l2[1]
                    if(y<0):
                        y=0
                    if(y>1080):
                        y=1080
                    pyautogui.moveTo(x, y)
        if fi==6:
            ccount-=1
            for hand_landmarks in results.multi_hand_landmarks:
                land = hand_landmarks
                val = land.landmark
                x=val[8].x*l1[0]+l1[1]
                if(x<0):
                    x=0
                if(x>1920):
                    x=1920
                y=val[8].y*l2[0]+l2[1]
                if(y<0):
                    y=0
                if(y>1080):
                    y=1080
                if(ccount==0):
                    ccount=20
                    print("clicked")
                    pyautogui.click(x, y)
        if fi==2:
            ccount-=1
            for hand_landmarks in results.multi_hand_landmarks:
                land = hand_landmarks
                val = land.landmark
                x=val[8].x*l1[0]+l1[1]
                if(x<0):
                    x=0
                if(x>1920):
                    x=1920
                y=val[8].y*l2[0]+l2[1]
                if(y<0):
                    y=0
                if(y>1080):
                    y=1080
                if(ccount==0):
                    ccount=20
                    print("clicked")
                    pyautogui.click(x, y,clicks=2)
    else:
        cv2.putText(image,'No Hands!', location, font, fontScale,fontColor,lineType)
    
    cv2.imshow('MediaPipe Hands', image)
    key = cv2.waitKey(1)
    if key == 27:
        break
hands.close()
cap.release()
cv2.destroyAllWindows()

