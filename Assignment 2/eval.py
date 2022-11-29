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
