import cv2 
import numpy as np
from keras.models import load_model
model = load_model("Artificial-Intelligence/Computer Vision projects/Mask detection/models/model-004.h5")

results = {0:'without_mask',1:'mask'}
color ={0:(0, 0, 255),1:(0, 255, 0)}

rect_size =4
cap = cv2.VideoCapture(0)

cascade = cv2.CascadeClassifier('Artificial-Intelligence/Computer Vision projects/Mask detection/models/haarcascade_frontalface_default.xml')

while True:
  ret,frame =cap.read()
  im =cv2.flip(frame,1,1)
  
  resize_im =cv2.resize(im,(im.shape[1]//rect_size,im.shape[0]//rect_size))
  faces = cascade.detectMultiScale(resize_im)
  for f in faces:
    (x,y,w,h) =[v*rect_size for v in f]
    face_img = im[y:y+h,x:x+w]
    resized = cv2.resize(face_img,(150,150))
    normal = resized/255.0
    reshaped = np.reshape(normal,(1,150,150,3))
    reshaped = np.vstack([reshaped])
    result = model.predict(reshaped)
    
    label = np.argmax(result,axis =1)[0]
    print(result,label)
    cv2.rectangle(im,(x,y),(x+w,y+h),color[label],2)
    cv2.rectangle(im,(x,y-40),(x+w,y),color[label],-1)
    cv2.putText(im,results[label],(x,y+10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255), 2)
  cv2.imshow('LIVE',im)
  key = cv2.waitKey(10)
  if key == 27:
    break

cap.release()
cv2.destroyAllWindows()