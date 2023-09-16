import numpy as np
import matplotlib.pyplot as plt
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=plt.imread("./img/biden.jpg")
# plt.imshow(img)

img1=img.copy()
face=face_cascade.detectMultiScale(img)[0]

f_x, f_y,f_w, f_h= face
img = cv2.rectangle(img, (f_x, f_y), (f_x + f_w, f_y + f_h), (255,255,255), 5 ) 
# print(f_x, f_y,f_w, f_h)
# plt.plot(f_x + (f_w // 2),f_y,'ro')
# plt.imshow(img)

helmet=plt.imread("img/spacehelmet2.png")
helmet=cv2.resize(helmet,(f_x + 150,f_y+400))
# print(helmet.shape)

for i in range(helmet.shape[0]):
  for j in range(helmet.shape[1]):
    if (helmet[i,j,3]>0):
      img1[f_y+i-(f_h // 2),f_x+j-110, :]=helmet[i,j,:-1]

plt.imshow(img1)