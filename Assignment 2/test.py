import numpy as np
import soundfile as sf
import unittest
from func_filter import *

#%% unit test
class TestFilterMethods(unittest.TestCase):
    
    def testMedianFilter(self):
        from scipy.signal import medfilt
        filterLength = 15
        degrade, fs = sf.read('degraded_d.wav')
        detect, _ = sf.read('detectionfile_d.wav')
        output_scipy = medfilt(degrade, filterLength)
        output_scipy[detect < 0.5] = degrade[detect < 0.5]
        
        medianFilter('degraded_d.wav', 'detectionfile_d.wav', filterLength, 'output_median.wav')
        output_median, fs = sf.read('output_median.wav')

        assert np.mean(np.abs(output_median - output_scipy)) < 1e-8
        
    
    def testCubicFilter(self):
        from scipy.interpolate import CubicSpline
        degrade, fs = sf.read('degraded_d.wav')
        detect, _ = sf.read('detectionfile_d.wav')
        index = np.arange(len(degrade))/fs
        cs = CubicSpline(index[detect < 0.5], degrade[detect < 0.5])
        output_scipy = cs(index)
        
        cubicSplineFilter('degraded_d.wav', 'detectionfile_d.wav', 20, 'output_cubic.wav')
        output_cubic, fs = sf.read('output_cubic.wav')
        
        assert np.mean(np.abs(output_cubic - output_scipy)) < 1e-8
        








unittest.main()
