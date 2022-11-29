#$$
import numpy as np
import soundfile as sf
import unittest
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


#%% parameter for MSE
LENGTH = np.arange(5, 31, 2)
MSEs = np.zeros(len(LENGTH))
for i in range(len(LENGTH)):
    medianFilter('degraded_d.wav', 'detectionfile_d.wav', LENGTH[i], 'output_median.wav')
    clean, fs = sf.read('clean_d.wav')
    output_median, fs = sf.read('output_median.wav')
    MSEs[i] = np.mean((clean - output_median)**2)



import matplotlib.pyplot as plt
plt.figure()
plt.plot(LENGTH, MSEs, '-*')
plt.xlabel('Filter length')
plt.ylabel('MSE')
plt.grid('on')
plt.show()

