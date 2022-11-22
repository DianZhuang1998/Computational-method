
# create Median function
import numpy as np


def getMedian(list, w):
    n = int((w - 1) / 2)
    if len(list) % 2 != 0:
        # list has an odd number of elements
        for i in range(n):
            list = [0] + list + [0]
        list = np.array(list)
        n_list = len(list) - w + 1
        for i in range(n_list):
            list_filter = list[i: i + 2 * n + 1]
            list_new = np.sort(list_filter)
            list[i + n] = list_new[n]
        return (list)
    else:
        print("list has an even number of elements")


# try to use Median function to test a list
# creat a list
ls = [3, 1, 4, 9, 2, 5, 3, 6]
print(np.median(ls))


# extra work without meaning
# define 1D median filter

def medfilt(x, w):
    # Apply a length-k median filter to a 1D array x.
    # Boundaries are extended by repeating endpoints.

    assert w % 2 == 1
    # Median filter length must be odd.
    assert x.ndim == 1
    # Input must be one-dimensional
    w2 = (w - 1) // 2
    y = np.zeros((len(x), w), dtype=x.dtype)
    y[:, w2] = x
    for i in range(w2):
        j = w2 - i
        y[j:, i] = x[:-j]
        y[:j, i] = x[0]
        y[:-j, -(i+1)] = x[j:]
        y[-j:, -(i+1)] = x[-1]
    return np.median(y, axis=1)
