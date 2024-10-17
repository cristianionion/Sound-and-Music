import scipy.io.wavfile as wav
import numpy as np
import sounddevice as REC


## PART 1

# amplitude
amplitude = 1/4

# duration (seconds)
duration = 1

# frequency (Hz)
frequency = 440

# sample rate (per second)
sample_rate = 48000

# how to write a wav file using scipy
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.write.html

t = np.linspace(0.,1.,sample_rate)
sine_wave = amplitude*np.sin(2.*np.pi*frequency*t)

wav.write("./code/sine.wav",sample_rate,sine_wave.astype(np.int16))


## PART 2
