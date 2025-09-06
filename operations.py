import numpy as np

def time_shift(signal, k):   # this i have created is for discrete signals
    return np.roll(signal, k)

def time_shift_continuous(signal_func, t, shift, A, f, phi):   # this is specially for signals like sin wave shifting
    return signal_func(A, f, phi, t - shift)

def time_scale(signal, k):
    n = np.arange(len(signal))
    scaled_n = np.arange(0, len(signal), k)
    return np.interp(scaled_n, n, signal)

def signal_addition(signal1, signal2):
    return signal1 + signal2

def signal_multiplication(signal1, signal2):
    return signal1 * signal2