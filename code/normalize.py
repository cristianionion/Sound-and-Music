import numpy as np

def normalize(sound):

    max = np.max(np.abs(sound))
    if max ==0:
        return sound # div/0
    else:
        return np.int16((sound/max)*32767)
    