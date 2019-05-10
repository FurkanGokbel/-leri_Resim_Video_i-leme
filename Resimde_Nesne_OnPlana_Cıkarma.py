# -*- coding: utf-8 -*-
# @Author : Muhammed Furkan Gökbel
# @File : Resimde_Nesne_OnPlana_Cıkarma.py
# @Software: PyCharm
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('buyuk-resim.jpg')
mask = np.zeros(img.shape[:2],np.uint8)
bgModel = np.zeros((1,65),np.float64)
fgModel = np.zeros((1,65),np.float64)
dikdortgen = (250,125,150,250)


cv2.grabCut(img,mask,dikdortgen,bgModel,fgModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0),0,1).astype('uint8')
img = img * mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()



















