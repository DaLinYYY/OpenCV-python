#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   read_images.py 
@author  :   dalin  
@Contact :   dalin.strive@gmail.com
@Date     :  2020/3/19 
"""


import cv2

# 1.灰度图加载一张彩色图
img = cv2.imread('..\img\imgtest.jpg', 0)


# 2.显示图片
cv2.imshow('Img', img)
cv2.waitKey(0)

# 先定义窗口，后显示图片
cv2.namedWindow('..\img\imgtest2', cv2.WINDOW_NORMAL)
cv2.imshow('..\img\imgtest2', img)
cv2.waitKey(0)


# 3.保存图片
cv2.imwrite('img\imgtest_gray.jpg', img)
