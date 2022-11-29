#%%
import numpy as np
import soundfile as sf
import unittest
from scipy.io import wavfile
from func_filter import *


#%% Compare MSE
medianFilter('degraded_d.wav', 'detectionfile_d.wav', 15, 'output_median.wav')
clean, fs = sf.read('clean_d.wav')
output_median, fs = sf.read('output_median.wav')
mse_median = np.mean((clean - output_median)**2)


cubicSplineFilter('degraded_d.wav', 'detectionfile_d.wav',
                  20, 'output_cubic.wav')
clean, fs = sf.read('clean_d.wav')
output_cubic, fs = sf.read('output_cubic.wav')
mse_cubic = np.mean((clean - output_cubic)**2)

print('MSE of median filter {:e}'.format(mse_median))
print('MSE of cubic spline filter {:e}'.format(mse_cubic))

t, degraded = wavfile.read("degraded_d.wav")
t, detection = wavfile.read("detectionfile_d.wav")
t, output_median = wavfile.read("output_median.wav")
t, output_cubic = wavfile.read("output_cubic.wav")


#%% parameter for MSE
LENGTH = np.arange(5, 31, 2)
MSEs = np.zeros(len(LENGTH))
for i in range(len(LENGTH)):
    medianFilter('degraded_d.wav', 'detectionfile_d.wav', LENGTH[i], 'output_median.wav')
    clean, fs = sf.read('clean_d.wav')
    output_median, fs = sf.read('output_median.wav')
    MSEs[i] = np.mean((clean - output_median)**2)


plt.figure(1)
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
plt.subplot(4,1,1)
plt.plot(degraded[0:])
plt.subplot(4,1,2)
plt.plot(detection[0:])
plt.subplot(4,1,3)
plt.plot(output_median[0:])
plt.subplot(4,1,4)
plt.plot(output_cubic[0:])
plt.ylabel("Amplitude")
plt.xlabel("Time")



import matplotlib.pyplot as plt
plt.figure()
plt.plot(LENGTH, MSEs, '-*')
plt.xlabel('Filter length')
plt.ylabel('MSE')
plt.grid('on')
plt.show()


