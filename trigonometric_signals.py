import numpy as np

def sine_wave(A, f, phi, t):
    """
    Generate sine wave: A * sin(2πft + φ)
    """
    return A * np.sin(2 * np.pi * f * t + phi)

def cosine_wave(A, f, phi, t):
    """
    Generate cosine wave: A * cos(2πft + φ)
    """
    return A * np.cos(2 * np.pi * f * t + phi)

def exponential_signal(A, a, t):
    """
    Generate exponential signal: A * e^(a*t)
    """
    return A * np.exp(a * t)
