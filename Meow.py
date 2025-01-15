

import cv2
import numpy as np
import face_recognition as fr

imgLebron = fr.load_image_file('Lebron_tests/Lebron_James.jpg')
imgLebron = cv2.cvtColor(imgLebron,cv2.COLOR_BGR2RGB)
imgTest = fr.load_image_file('Lebron_tests/Lebron_test1.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

cv2.imshow('My Pookie Lebron1', imgLebron)
cv2.imshow('My Pookie Lebron2', imgTest)
cv2.waitKey(0)