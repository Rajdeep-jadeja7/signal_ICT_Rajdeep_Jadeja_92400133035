import numpy as np
import matplotlib.pyplot as plt


# Import the modules from the folder
from signal_ICT_Rajdeep_Jadeja_92400133035 import unitary_signals
from signal_ICT_Rajdeep_Jadeja_92400133035 import trigonometric_signals as trig_signals
from signal_ICT_Rajdeep_Jadeja_92400133035 import operations as ops


# 1. Unit Step & Unit Impulse (length 20)
n = np.arange(0, 20)
u = unitary_signals.unit_step(n)
d = unitary_signals.unit_impulse(n)
r = unitary_signals.ramp_signal(n)

# 2. Sine wave (Amplitude=2, Freq=5Hz, Phase=0)
t = np.linspace(0, 1, 500)
sine = trig_signals.sine_wave(2, 5, 0, t)
cosine = trig_signals.cosine_wave(2, 5, 0, t)

# 3. Time shift sine wave by +5 units
shifted_sine = ops.time_shift_continuous(trig_signals.sine_wave, t, 0.1, 2, 5, 0)

# 4. Addition of Unit Step + Ramp
sum_signal = ops.signal_addition(u, r)

# 5. Multiply Sine × Cosine
product = ops.signal_multiplication(sine, cosine)

# Plotting
plt.figure(figsize=(12, 10))

plt.subplot(3, 2, 1)
plt.stem(n, u, basefmt=" ")
plt.title("Unit Step (Length 20)")

plt.subplot(3, 2, 2)
plt.stem(n, d, basefmt=" ")
plt.title("Unit Impulse (Length 20)")

plt.subplot(3, 2, 3)
plt.plot(t, sine)
plt.title("Sine Wave (Amplitude=2, Freq=5Hz, Phase=0)")

plt.subplot(3, 2, 4)
plt.plot(t, shifted_sine, 'orange', linewidth=2, label="Shifted +0.1")
plt.title("Time Shift of Sine Wave")
plt.legend()

plt.subplot(3, 2, 5)
plt.stem(n, sum_signal, basefmt=" ")
plt.title("Unit Step + Ramp Signal")

plt.subplot(3, 2, 6)
plt.plot(t, product)
plt.title("Sine × Cosine (Amplitude=2, Freq=5Hz)")

plt.tight_layout()
plt.show()