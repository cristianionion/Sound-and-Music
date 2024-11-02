import scipy.io.wavfile as wav
from scipy.fft import fft
import numpy as np
import sounddevice as REC
from playsound import playsound
from pydub import AudioSegment



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


length = 2000
blocks = np.array_split(Ds,len(Ds)//length)



"""
D1 = AudioSegment.from_wav("./code/notes/D1.wav")
D6 = AudioSegment.from_wav("./code/notes/D6.wav")
D8 = AudioSegment.from_wav("./code/notes/D8.wav")


C4E4G4 = C4+E4+G4
C4E4G4.export("./code/notes/C4E4G4.wav", format="wav")


playsound('./code/notes/C4E4G4.wav')

C4CHORD = C4.overlay(E4,position=0)
C4CHORD = C4CHORD.overlay(G4,position=0)

C4CHORD.export("./code/notes/C4CHORD.wav",format="wav")

playsound('./code/notes/C4CHORD.wav')"""