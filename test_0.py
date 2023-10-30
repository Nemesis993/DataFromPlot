# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 19:19:25 2023

@author: Baumann
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import copy
 
# Save image in set directory
# Read RGB image
img_original = cv2.imread('images/test_image_0.png')

img_original_c = copy.deepcopy(img_original)

# converting image into grayscale image
img = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)#/255
img_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)


img = cv2.adaptiveThreshold(img_original,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
 cv2.THRESH_BINARY_INV,21,2)

img_original = cv2.adaptiveThreshold(img_original,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
 cv2.THRESH_BINARY_INV,21,2)

# Output img with window name as 'image'

cv2.imshow('image', img)
#plt.imshow(img)

#plt.xticks([]), plt.yticks([])
#plt.show()

#define the events for the
# mouse_click.

click = (-1, -1)
release = (-1, -1)

def mouse_click(event, x, y, 
                flags, param):
    
    global click, release
    # to check if left mouse 
    # button was clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        
        click = (x, y) 
          
    if event == cv2.EVENT_LBUTTONUP:
        
        release = (x, y) 
        cv2.rectangle(img, click, release, (0,255,255), 2)
        cv2.imshow('image', img)
  
cv2.setMouseCallback('image', mouse_click)
   
cv2.waitKey(0)

cv2.destroyAllWindows()

print(click)
print(release)


img_slct = img[min(click[1],release[1]):max(click[1],release[1]), min(click[0],release[0]):max(click[0], release[0])]
#print(img_slct)
#['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
res = cv2.matchTemplate(img_original, img_slct, 1)

def find_n_min(res, n=5, shift=(0, 0), delta=0):
    x_list, y_list = [], []
    def find_min(res):
        y, x = np.where(res==np.min(res))
        return x[0], y[0]
    def fill_delta(res, x, y, shift, delta):
        
        res[max(0, y-shift[1]-delta):min(len(res), shift[1]+y+delta), max(0, x-shift[0]-delta):min(len(res[0]), shift[0]+x+delta)] = 10
        return res
    
    for i in range(n):
        x0, y0 = find_min(res)
        x0 += shift[0]
        y0 += shift[1]
        
        x_list.append(x0)
        y_list.append(y0)
        res = fill_delta(res, x0, y0, shift, delta)
    return x_list, y_list

res_test = copy.deepcopy(res)
shift = (len(img_slct[0])//2, len(img_slct)//2)
x, y = find_n_min(res_test, 7, shift=shift, delta=10)

print(x)
print(y)
for x0, y0 in zip(x, y):
    cv2.circle(img_original_c, (x0, y0), 2, (0,0,255), 2)

cv2.imshow('res', img_original_c)

#cv2.imshow('selected', res)

cv2.waitKey(0)
  
# close all the opened windows.
cv2.destroyAllWindows()



