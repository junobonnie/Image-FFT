# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:46:36 2023

@author: replica
"""

import numpy as np
import matplotlib.pyplot as plt

def sin_wave(amp, freq, time):
    return amp * np.sin(2*np.pi*freq*time)

time = np.arange(0, 5, 0.001)
sin1 = sin_wave(1, 10, time)
sin2 = sin_wave(2, 5, time)
sin3 = sin_wave(4, 1, time)

sin_sum = sin1 + sin2 + sin3

plt.figure(figsize=(12,5))
plt.plot(time, sin1, label=r"$\sin {20\pi} t$", color='red')
plt.plot(time, sin2, label=r"$2\sin {10\pi} t$", color='blue')
plt.plot(time, sin3, label=r"$4\sin {2\pi} t$", color='green')
plt.plot(time, sin_sum, label=r"total", color='black')
plt.legend()
plt.grid()
plt.show()

n = len(sin_sum) 
k = np.arange(n)
Fs = 1/0.001
T = n/Fs
freq = k/T 
freq = freq[range(int(n/2)+1)]

Y = 2*np.fft.rfft(sin_sum)/n
#Y = 2*Y[range(int(n/2))]

fig, ax = plt.subplots(2, 1, figsize=(12,8))
ax[0].plot(time, sin_sum)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude'); ax[0].grid(True)
ax[1].plot(freq, abs(Y), 'r', linestyle=' ', marker='^') 
ax[1].set_xlabel('Freq (Hz)')
ax[1].set_ylabel('|Y(freq)|')
ax[1].vlines(freq, [0], abs(Y))
ax[1].set_xlim([0, Fs]); ax[1].grid(True)
plt.show()

#plt.figure(figsize=(12,5))
result = np.zeros(n)
for i, amp in enumerate(Y):
    result += (amp*np.exp(2j*np.pi*i/T*time)).real
    # if i > n/2*0.0375:
    #     break
    #plt.plot(time, (amp*np.exp(2j*np.pi*i/T*time)).real)
    
#plt.show()

#result = np.fft.irfft(Y)

plt.figure(figsize=(12,5))
plt.plot(time, sin_sum, label=r"total", color='black')
plt.plot(time, result, label=r"predict", color='red')
plt.legend()
plt.grid()
plt.show()