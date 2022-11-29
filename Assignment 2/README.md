# Filter
Use median filter and cubic spline filter to detect clicks and restore in auido.

# Project Description
This assignment builds on Assignment I. We assume that we have successfully detected the clicks and we are applying different interpolation methods to restore the audio, such as
- median filtering
- cubic splines


# How to Install and Run the Project
##  Required libraries
- matplotlib==3.6.2
- numpy==1.23.4
- playsound==1.2.2
- scipy==1.9.3
- soundfile==0.11.0
- tqdm==4.64.1


## Files
test.py - include unit test 
eval.py - evaluate the reuslt and calculate the correspond MSE
func_filter.py - include two method for filter

## Usage

```python
from func_filter import *
medianFilter('degraded_d.wav', 'detectionfile_d.wav', 15, 'output_median.wav')

cubicSplineFilter('degraded_d.wav', 'detectionfile_d.wav', 20, 'output_cubic.wav')
```