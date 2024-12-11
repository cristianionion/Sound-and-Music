import numpy as np
import scipy.io.wavfile as wav
from keyfreq import key_freq


def create_note(note,frequency):

    amplitude = 32767/4
    sample_rate = 48000
    duration = 5

    # how to write a wav file using scipy
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.write.html

    t = np.linspace(0.,duration,int(sample_rate*duration))
    frequency = float(frequency)
    sine_wave = amplitude*np.sin(2.*np.pi*frequency*t)

    wav.write("./project/notes/"+str(note)+".wav",sample_rate,sine_wave.astype(np.int16))

for key,freq in key_freq.items():
    create_note(key,freq)