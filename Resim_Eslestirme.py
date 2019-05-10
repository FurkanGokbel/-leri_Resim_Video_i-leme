# -*- coding: utf-8 -*-
# @Author : Muhammed Furkan GÖKBEL
# @File : Resim_Eslestirme.py
# @Software: PyCharm
import numpy as np
import cv2
import matplotlib.pyplot as plt

resim_aranacak = cv2.imread('kucuk-resim.jpg')
resim_buyuk = cv2.imread('buyuk-resim.jpg')

orb = cv2.ORB_create()
an1,hedef1 = orb.detectAndCompute(resim_aranacak,None)
an2,hedef2 = orb.detectAndCompute(resim_buyuk,None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck = True)
eslesmeler = bf.match(hedef1,hedef2)
eslesmeler = sorted(eslesmeler,key= lambda x:x.distance)
son_resim = cv2.drawMatches(resim_aranacak,an1,resim_buyuk,an2,eslesmeler[:10],None,flags = 2)
plt.imshow(son_resim)
plt.show()

