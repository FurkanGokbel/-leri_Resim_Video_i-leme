# -*- coding: utf-8 -*-
# @Author : Muhammed Furkan GÖKBEL
# @File : Köse_Bulma.py
# @Software: PyCharm
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('kose-bulma.jpg')
def corner(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    kose = cv2.goodFeaturesToTrack(gray, 200, 0.01, 10)
    kose = np.int0(kose)
    for i in kose:
        x, y = i.ravel()
        print("x : ", x, "y: ", y)
        cv2.circle(img, (x, y), 3, 255, -1)
    print(len(kose))
    cv2.imshow('koseler', img)





while True:
    corner(img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

