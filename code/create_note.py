import numpy as np
import scipy.io.wavfile as wav


def create_note(note,frequency):

    amplitude = 32767/4
    sample_rate = 48000
    duration = 2

    # how to write a wav file using scipy
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.write.html

    t = np.linspace(0.,duration,int(sample_rate*duration))
    sine_wave = amplitude*np.sin(2.*np.pi*frequency*t)

    wav.write("./code/notes/"+str(note)+".wav",sample_rate,sine_wave.astype(np.int16))
