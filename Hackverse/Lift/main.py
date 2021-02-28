#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.models import load_model
import numpy as np
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
model=load_model("Liftmodel")


# In[2]:


Char="0123456789DOU$"

font        = cv2.FONT_HERSHEY_SIMPLEX
location    = (100,50)
fontScale   = 1
fontColor   = (255,255,255)
lineType    = 2


# For webcam input:
hands = mp_hands.Hands(
    min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

  # Flip the image horizontally for a later selfie-view display, and convert
  # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
  # To improve performance, optionally mark the image as not writeable to
  # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

  # Draw the hand annotations on the image.
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
        text=Char[fi]
        cv2.putText(image,text, (0,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3, cv2.LINE_AA)
    else:
        cv2.putText(image,'No Hands!', location, font, fontScale,fontColor,lineType)
    
    cv2.imshow('MediaPipe Hands', image)
    key = cv2.waitKey(1)
    if key == 27:
        break
hands.close()
cap.release()
cv2.destroyAllWindows()


# In[ ]:




