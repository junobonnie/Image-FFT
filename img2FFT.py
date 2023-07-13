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
    max_ = np.max(ifft_img.real)
    return np.array(ifft_img.real/max_*255, dtype=np.int16)

def reshape_image(img):
    x, y, z = img.shape
    half_x = x//2
    half_y = y//2
    return np.vstack([np.hstack([img[half_x:, half_y:, :], img[half_x:, :half_y, :]]),
                      np.hstack([img[:half_x, half_y:, :], img[:half_x, :half_y, :]])])

def show_fft_image(fft_img):
    fft_img = reshape_image(fft_img)
    abs_ = abs(fft_img)
    max_ = np.max(abs_)
    x, y, z = img.shape
    half_x = x//2
    half_y = y//2
    plt.imshow(abs_/max_*255, extent=[-half_y, y-half_y, -half_x, x-half_x])
    plt.show()

def remove_frequency(fft_img, min_f, max_f):
    if not min_f == 0:
        fft_img[:min_f,:min_f] = 0
        fft_img[:min_f,-min_f:] = 0
        fft_img[-min_f:,:min_f] = 0
        fft_img[-min_f:,-min_f:] = 0
    
    if not max_f == -1:
        fft_img[max_f:-max_f,:] = 0
        fft_img[:,max_f:-max_f] = 0

img = plt.imread(r"D:\Media\사진\게임 스샷\KSP\20210517225512_1.jpg")

plt.imshow(img)
plt.show()

fft_img = fft_image(img)

show_fft_image(fft_img)

remove_frequency(fft_img, 0, 100)

show_fft_image(fft_img)

ifft_img = ifft_image(fft_img)
plt.imshow(ifft_img)
plt.show()
