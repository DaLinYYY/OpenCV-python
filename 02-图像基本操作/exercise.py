#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   exercise.py 
@author  :   dalin  
@Contact :   dalin.strive@gmail.com
@Date     :  2020/3/25 
"""

import cv2

img = cv2.imread('img\imgtest.jpg')
# print(img)
# px = img[100, 100]
# print(px)
# px_blue = img[100, 100, 0]
# print(px_blue)
# print(img.shape)
# height, width, channels = img.shape
# print(height)
# print(img.dtype)
# print(img.size)

# 截取脸部ROI
# face = img[80:280, 75:230]
# cv2.imshow('face', face)
# cv2.waitKey(0)

# 通道分割与合并
# b, g, r = cv2.split(img)
# img = cv2.merge((b, g, r))
# cv2.imshow('img', img)
# cv2.waitKey(0)

b = img[:, :, 2]
cv2.imshow('blue', b)
cv2.waitKey(0)