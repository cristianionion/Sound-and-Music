import scipy.io.wavfile as wav
from scipy.fft import fft, rfft, irfft
import numpy as np
import sounddevice as REC
from playsound import playsound
from pydub import AudioSegment
from scipy import signal
from scipy.io import wavfile



def create_note(note,frequency, amplitude):

    #amplitude = 32767/4
    sample_rate = 48000
    duration = 2

    # how to write a wav file using scipy
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.write.html

    t = np.linspace(0.,duration,int(sample_rate*duration))
    sine_wave = amplitude*np.sin(2.*np.pi*frequency*t)

    wav.write("./code/notes/"+str(note)+".wav",sample_rate,sine_wave.astype(np.int16))



# low volume low frequency and mid range frequency, high volume high frequency
soft_low = create_note("D1",36.7,32767/100)
soft_mid = create_note("D6", 1174.66,32767/200)
loud_high = create_note("D8",4698.63,32767/4)

#playsound('./code/notes/D1.wav')
#playsound('./code/notes/D6.wav')
#playsound('./code/notes/D8.wav')


D1 = AudioSegment.from_wav("./code/notes/D1.wav")
D6 = AudioSegment.from_wav("./code/notes/D6.wav")
D8 = AudioSegment.from_wav("./code/notes/D8.wav")

Ds = D1.overlay(D6,position=0)
Ds = Ds.overlay(D8,position=0)
Ds.export("./code/notes/D1D6D8.wav",format="wav")

#playsound("./code/notes/D1D6D8.wav")

#print(len(D1)) # 2000
#print(len(D6)) # 2000
#print(len(D8)) # 2000
#print(len(Ds)) # 2000


# convert AudioSegment to np.array

Ds = np.array(Ds.get_array_of_samples())


### Using Code From Bart Massey https://github.com/pdx-cs-sound/fft-band-demo/blob/main/fft.py
# Just to visualize in Audacity how that code adjusts my D1D6D8 file


length = 2000
blocks = np.array_split(Ds,len(Ds)//length)


window = signal.windows.blackmanharris(length,sym=False)
freqs = np.array([rfft(window * b) for b in blocks])

# Convert FFT freqs to bands.
bin_width = 48000 / 32.0 / 2.0
bin_mid = round(300 / bin_width)
bin_hi = round(2000 / bin_width)
bands = np.array(np.array([
    np.sum(np.abs(fs[:bin_mid])),
    np.sum(np.abs(fs[bin_mid:bin_hi])),
    np.sum(np.abs(fs[bin_hi:])),
]) for fs in freqs)

# Play the output of inverse FFT of freqs.
ifs = np.concatenate([irfft(fs) for fs in freqs])
wavfile.write("./code/notes/output.wav", 48000, ifs)

#playsound("./code/notes/output.wav")

playsound("./code/notes/D1D6D8.wav")

rate,data = wavfile.read("./code/notes/output.wav")

REC.play(data,rate)
REC.wait()