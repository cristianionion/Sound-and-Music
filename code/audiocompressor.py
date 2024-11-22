import numpy as np
import scipy
from pydub import AudioSegment
from pydub.playback import play
import os
from pydub.utils import which
from scipy.io import wavfile
import normalize
import soundfile as sf

# lossy audio compressor
# .mp3 -> .wav

# https://cs.stanford.edu/people/eroberts/courses/soco/projects/data-compression/lossy/mp3/concept.htm


# load mp3 file and play it
"""
file_path = "./code/mp3/sample1.mp3"
if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    print("File found!")
"""

# attempting with mp3 currently gives permission error
"""
AudioSegment.converter = which("C:/ffmpeg/bin/ffmpeg.exe")
AudioSegment.ffprobe = which("C:/ffmpeg/bin/ffprobe.exe")

os.environ['TMP'] = 'C:/temp'
os.environ['TEMP'] = 'C:/temp'

try:
    sample = AudioSegment.from_mp3(file_path)
    play(sample)
except PermissionError as e:
    print(f"PermissionError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
sample = AudioSegment.from_mp3("./code/mp3/sample1.mp3")
#play(sample)

### play sample gives permission error
"""



### mu-law 

rate,samples = wavfile.read("./code/wav/sample.wav")

#print(rate,samples)

# normalize
signal = normalize.normalize(samples)


# mu-law compression
# https://en.wikipedia.org/wiki/%CE%9C-law_algorithm
mu = 255

compressed = np.sign(signal)*np.log(1+mu*np.abs(signal))/np.log(1+mu)

signal = np.clip(compressed,-1,1)

# scale back to 16 bit PCM
compressed = np.int16(compressed*32767)


wavfile.write("./code/wav/mu_compressed.wav",rate,compressed)



### A-law 

rate,samples = wavfile.read("./code/wav/sample.wav")

#print(rate,samples)

# normalize
samples = normalize.normalize(samples)


# A-law compression
# https://en.wikipedia.org/wiki/A-law_algorithm
a = 87.6

compressed = np.zeros_like(samples)

for i in range(len(samples)):

    # compute left and right separately

    left = np.abs(samples[i,0])
    right = np.abs(samples[i,1])


    abs = max(left,right)
    #print(abs)
    if abs < 1/a:
        compressed[i,0] = np.sign(samples[i,0])*(a*left)/(1+np.log(a))
        compressed[i,1] = np.sign(samples[i,1])*(a*right)/(1+np.log(a))

    else:# add small number to avoid log(0)
        compressed[i,0] = np.sign(samples[i,0])*(1+np.log(a*left+0.00001))/(1+np.log(a))
        compressed[i,1] = np.sign(samples[i,1])*(1+np.log(a*right+0.00001))/(1+np.log(a))

#samples = np.sign(samples)*(np.log1p(a*np.abs(samples))/ np.log1p(a))

signal = np.clip(samples,-1,1)



# scale back to 16 bit PCM
compressed = np.int16(signal*32767)


wavfile.write("./code/wav/a_compressed.wav",rate,compressed)

print("success")