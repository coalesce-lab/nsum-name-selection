import numpy as np
import warnings

warnings.filterwarnings('ignore')

def kldiv(p, q):
    return np.sum(p * np.nan_to_num(np.log(p / q)))

def jsdiv(p, q):
    m = (p + q) / 2
    return (kldiv(p, m) + kldiv(q, m)) / 2

def l2(p, q):
    return np.sum((p - q)**2)

def l1(p, q):
    return np.sum(np.abs(p - q))
