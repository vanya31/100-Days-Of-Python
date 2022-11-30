import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image= cv2.imread('1.png')

img = cv2.resize(image,None,fx=0.3,fy=0.3)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)

for (x,y,w,h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

cv2.imshow('img', img)
cv2.waitKey()
