import scipy.io.wavfile as wav
import numpy as np
import sounddevice as REC
from playsound import playsound
from pydub import AudioSegment
# https://pydub.com/ 

# link to note-frequency chart for reference
# https://muted.io/note-frequencies/


# create a note
def create_note(note,frequency):

    amplitude = 32767/4
    sample_rate = 48000
    duration = 2

    # how to write a wav file using scipy
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.write.html

    t = np.linspace(0.,duration,int(sample_rate*duration))
    sine_wave = amplitude*np.sin(2.*np.pi*frequency*t)

    wav.write("./code/notes/"+str(note)+".wav",sample_rate,sine_wave.astype(np.int16))



create_note("A4",440)
create_note("C4",261.63)
create_note("E4",329.63)
create_note("G4",392)

#playsound('./code/A4.wav')
#playsound('./code/C4.wav')
#playsound('./code/E4.wav')
#playsound('./code/G4.wav')



# adding wav files, learned about Jiaaro's pydub from this post
# https://stackoverflow.com/questions/2890703/how-to-join-two-wav-files-using-python

C4 = AudioSegment.from_wav("./code/notes/C4.wav")
E4 = AudioSegment.from_wav("./code/notes/E4.wav")
G4 = AudioSegment.from_wav("./code/notes/G4.wav")

C4E4G4 = C4+E4+G4
C4E4G4.export("./code/notes/C4E4G4.wav", format="wav")


playsound('./code/notes/C4E4G4.wav')

C4CHORD = C4.overlay(E4,position=0)
C4CHORD = C4CHORD.overlay(G4,position=0)

C4CHORD.export("./code/notes/C4CHORD.wav",format="wav")

playsound('./code/notes/C4CHORD.wav')