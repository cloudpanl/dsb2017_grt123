#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 11:51:00 2018

@author: ly
"""

import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt
import pandas as pd

import os
import dicom

from skimage import measure, morphology,data,color
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


#convex hull
#img=color.rgb2gray(data.horse())
#img=(img<0.5)*1
#
#chull = morphology.convex_hull_image(img)
#
#plt.imshow(chull, cmap=plt.cm.gray)



#gauss filter
#img=data.astronaut()
#img2=scipy.ndimage.gaussian_filter(img,sigma=5,cval=0)
#
#plt.figure('gaussian',figsize=(8,8))
#plt.subplot(121)
#plt.imshow(img2)  
#
#plt.subplot(122)
#plt.imshow(img)



def microstructure(l=256):
    n = 5
    x, y = np.ogrid[0:l, 0:l]  #生成网络
    mask = np.zeros((l, l))
    generator = np.random.RandomState(1)  #随机数种子
    points = l * generator.rand(2, n**2)
    mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
    mask = scipy.ndimage.gaussian_filter(mask, sigma=l/(4.*n)) #高斯滤波
    return mask > mask.mean()

data = microstructure(l=128)*1 #生成测试图片

labels=measure.label(data,connectivity=2)  #8连通区域标记
properties = measure.regionprops(labels)
dst=color.label2rgb(labels)  #根据不同的标记显示不同的颜色
print('regions number:',labels.max()+1)  #显示连通区域块数(从0开始标记)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(data, plt.cm.gray, interpolation='nearest')
ax1.axis('off')
ax2.imshow(dst,interpolation='nearest')
ax2.axis('off')

fig.tight_layout()
plt.show()







