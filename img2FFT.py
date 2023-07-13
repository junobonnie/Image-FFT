# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 00:07:02 2023

@author: replica
"""

import matplotlib.pyplot as plt
import numpy as np
    
def fft_2d(array):
    fft_array = np.fft.fft(array)
    fft_array = np.fft.fft(fft_array, axis=0)
    return fft_array

def ifft_2d(array):
    ifft_array = np.fft.ifft(array, axis=0)
    ifft_array = np.fft.ifft(ifft_array)
    return ifft_array

def fft_image(img):
    x, y, z = img.shape
    fft_img = np.zeros((x,y,0))
    for i in range(3):
         fft_img = np.append(fft_img, fft_2d(img[:,:,i]).reshape((x,y,1)), axis=-1)
    return fft_img

def ifft_image(img):
    x, y, z = img.shape
    ifft_img = np.zeros((x,y,0))
    for i in range(3):
        ifft_img = np.append(ifft_img, ifft_2d(img[:,:,i]).reshape((x,y,1)), axis=-1)
    return np.array(ifft_img.real, dtype=np.int16)

def reshape_image(img):
    x, y, z = img.shape
    half_x = int(x/2)
    half_y = int(y/2)

    return np.vstack([np.hstack([img[half_x:, half_y:, :], img[half_x:, :half_y, :]]),
                      np.hstack([img[:half_x, half_y:, :], img[:half_x, :half_y, :]])])

def show_fft_image(fft_img):
    fft_img = reshape_image(fft_img)
    abs_ = abs(fft_img)
    max_ = np.max(abs_)
    plt.imshow(abs_/max_*255)
    plt.show()

img = plt.imread(r"D:\Media\사진\게임 스샷\KSP\20210517225512_1.jpg")

plt.imshow(img)
plt.show()

fft_img = fft_image(img)

show_fft_image(fft_img)

value = 100
fft_img[value:-value,:] = 0
fft_img[:,value:-value] = 0

show_fft_image(fft_img)

ifft_img = ifft_image(fft_img)

plt.imshow(ifft_img)
plt.show()