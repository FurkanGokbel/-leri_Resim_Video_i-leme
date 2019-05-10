# -*- coding: utf-8 -*-
# @Time : 18.09.2018 13:56
# @Author : Raşit EVDÜZEN
# @File : Resimden_Metin_okuma.py
# @Software: PyCharm


import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

kaynak_yolu = ""

def metinOku(img_yolu):
    img = cv2.imread(img_yolu)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1,1),np.uint8)
    img = cv2.erode(img,kernel,iterations = 1)

    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,2)
    cv2.imwrite(kaynak_yolu+'gurultusuz.png',img)

    sonuc = pytesseract.image_to_string(Image.open(kaynak_yolu+'gurultusuz.png'))  # lang='tur'
    return sonuc


print("******************")
print("Metin Okuma")
print("******************")

print(metinOku('b.png'))

#a = pytesseract.image_to_string(Image.open('b.png'),lang='tur')
#print(a)


















