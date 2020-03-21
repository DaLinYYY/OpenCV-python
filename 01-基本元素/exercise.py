#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   exercise.py 
@author  :   dalin  
@Contact :   dalin.strive@gmail.com
@Date     :  2020/3/19 
"""

import cv2

img = cv2.imread('img\imgtest.jpg')
cv2.imshow('img\imgtest', img)

k = cv2.waitKey(0)
# ord()用来获取某个字符的编码
if k == ord('s'):
    cv2.imwrite('img\imgtest_save.bmp', img)