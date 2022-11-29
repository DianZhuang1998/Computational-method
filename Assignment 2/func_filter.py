import numpy as np
import soundfile as sf
from tqdm import tqdm
import matplotlib.pyplot as plt
from playsound import playsound

plt.close('all')


# %%
def medianFilter(degraded, detectionfile, filterlength, outputfile, play=False):
    """
    restore audio from degraded audio via median filter.
    Parameters
    ----------
    degraded : the audio file you corrupted from a clean audio.
    detectionfile : parameter values b_k for the median filter.
    filterlength : median filter length.
    outputfile : restored audio file.
    play: bool. whether play the degraded and restored audio.

    Returns
    -------
    None.

    """
    # check input
    assert filterlength % 2 == 1, 'filter length is not ODD'
    audio_degraded, fs = sf.read(degraded)
    detection, _ = sf.read(detectionfile)
    assert len(audio_degraded) == len(
        detection), 'degrade wav and detection have different length'

    # filter
    output = audio_degraded * 1.0
    pbar = tqdm(range(len(audio_degraded)), 'Median filter', ncols=100)
    for i in pbar:
        if detection[i] < 0.5:
            continue
        else:
            stdIndex = np.max([0, i - filterlength // 2])
            endIndex = np.min([i - filterlength // 2 + filterlength, len(audio_degraded)])
            seg = audio_degraded[stdIndex:endIndex]
            seg = np.sort(seg)
            output[i] = seg[len(seg) // 2]
    # save
    sf.write(outputfile, output, fs)
    pbar.close()
    print('Done.')

    if play:
        # play audio
        print('Playing degraded audio...')
        playsound(degraded)
        print('Playing restored  audio...')
        playsound(outputfile)


def cubicSplineFilter(degraded, detectionfile, numOfKnots, outputfile, play=False):
    """
    restore audio from degraded audio via cubic spline filter.
    Parameters
    ----------
    degraded : the audio file you corrupted from a clean audio.
    detectionfile : parameter values b_k for the median filter.
    numOfKnots : number of knots.
    outputfile : restored audio file.
    play: bool. whether play the degraded and restored audio.

    Returns
    -------
    None.

    """
    # check input
    audio_degraded, fs = sf.read(degraded)
    detection, _ = sf.read(detectionfile)
    assert len(audio_degraded) == len(
        detection), 'degrade wav and detection have different length'

    # filter
    output = audio_degraded * 1.0
    pbar = tqdm(range(len(audio_degraded)), 'Cubic spline filter', ncols=100)
    for i in pbar:
        if detection[i] < 0.5:
            continue
        else:
            index = []
            j = i
            while len(index) < numOfKnots//2:
                if detection[j] < 0.5:
                    index = [j] + index
                j -= 1
            j = i
            while len(index) < numOfKnots:
                if detection[j] < 0.5:
                    index = index + [j]
                j += 1

            x = index - np.min(index)
            y = audio_degraded[index]
            cs = CubicSpline(x, y)
            output[i] = cs.calc(i - np.min(index))
    # save
    sf.write(outputfile, output, fs)
    pbar.close()
    print('Done.')

    if play:
        # play audio
        print('Playing degraded audio...')
        playsound(degraded)
        print('Playing restored  audio...')
        playsound(outputfile)


class CubicSpline:

    """
    Cubic Spline class
    usage:
        spline=Spline(x,y)
        rx=np.arange(0,4,0.1)
        ry=[spline.calc(i) for i in rx]
    """

    def __init__(self, x, y):
        self.b, self.c, self.d, self.w = [], [], [], []

        self.x = x
        self.y = y

        self.nx = len(x)  # dimension of x
        h = np.diff(x)

        # calc coefficient c
        self.a = [iy for iy in y]

        # calc coefficient c
        A = self.__calc__A(h)
        B = self.__calc__B(h)
        self.c = np.linalg.solve(A, B)
        #  print(self.c1)

        # calc spline coefficient b and d
        for i in range(self.nx - 1):
            self.d.append((self.c[i + 1] - self.c[i]) / (3.0 * h[i]))
            tb = (self.a[i + 1] - self.a[i]) / h[i] - h[i] * \
                (self.c[i + 1] + 2.0 * self.c[i]) / 3.0
            self.b.append(tb)

    def calc(self, t):
        """
        Calc position
        if t is outside of the input x, return None
        """

        if t < self.x[0]:
            return None
        elif t > self.x[-1]:
            return None

        i = self.__search_index(t)
        dx = t - self.x[i]
        result = self.a[i] + self.b[i] * dx + \
            self.c[i] * dx ** 2.0 + self.d[i] * dx ** 3.0

        return result

    def __search_index(self, x):
        """
        search data segment index
        """

        for i in range(self.nx):
            if self.x[i] - x > 0:
                return i - 1

    def __calc__A(self, h):
        """
        calc matrix A for spline coefficient c
        """
        A = np.zeros((self.nx, self.nx))
        A[0, 0] = 1.0
        for i in range(self.nx - 1):
            if i is not self.nx - 2:
                A[i + 1, i + 1] = 2.0 * (h[i] + h[i + 1])
            A[i + 1, i] = h[i]
            A[i, i + 1] = h[i]

        A[0, 1] = 0.0
        A[self.nx - 1, self.nx - 2] = 0.0
        A[self.nx - 1, self.nx - 1] = 1.0
        return A

    def __calc__B(self, h):
        """
        calc matrix B for spline coefficient c
        """
        B = np.zeros(self.nx)
        for i in range(self.nx - 2):
            B[i + 1] = 3.0 * (self.a[i + 2] - self.a[i + 1]) / \
                h[i + 1] - 3.0 * (self.a[i + 1] - self.a[i]) / h[i]

        return B


