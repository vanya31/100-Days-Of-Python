import cv2

#image_detection

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

image= cv2.imread('1.png')

img = cv2.resize(image,None,fx=0.3,fy=0.3)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)

for (x,y,w,h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

cv2.imshow('img', img)
cv2.waitKey()


#love_calculator

from tkinter import *
import random
root = Tk()
root.geometry('400x240')
root.title('Love Calculator????')


def calculate_love():
	st = '0123456789'
	digit = 2
	temp = "".join(random.sample(st, digit))
	result.config(text=temp)


# Heading on Top
heading = Label(root, text='Love Calculator - How much is he/she into you')
heading.pack()

# Slot/input for the first name
slot1 = Label(root, text="Enter Your Name:")
slot1.pack()
name1 = Entry(root, border=5)
name1.pack()

# Slot/input for the partner name
slot2 = Label(root, text="Enter Your Partner Name:")
slot2.pack()
name2 = Entry(root, border=5)
name2.pack()

bt = Button(root, text="Calculate", height=1,
			width=7, command=calculate_love)
bt.pack()

result = Label(root, text='Love Percentage between both of You:')
result.pack()

# Starting the GUI
root.mainloop()
