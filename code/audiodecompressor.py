import numpy as np
import scipy
from pydub import AudioSegment
from pydub.playback import play
import os
from pydub.utils import which
from scipy.io import wavfile
import normalize
import soundfile as sf



### mu-law 

rate,compressed = wavfile.read("./code/wav/mu_compressed.wav")

#print(rate,compressed)

# normalize
compressed = normalize.normalize(compressed)


# mu-law compression
# https://en.wikipedia.org/wiki/%CE%9C-law_algorithm
mu = 255

decompressed = np.sign(compressed)* (np.expm1(np.abs(compressed)*np.log1p(mu))/mu)
#compressed = np.sign(signal)*np.log1p(mu*np.abs(signal))/np.log1p(mu)

decompressed = np.clip(decompressed,-1,1)

# scale back to 16 bit PCM
decompressed = np.int16(decompressed*32767)


wavfile.write("./code/wav/mu_decompressed.wav",rate,decompressed)



### A-law 

rate,samples = wavfile.read("./code/wav/a_compressed.wav")

#print(rate,samples)

# normalize
samples = normalize.normalize(samples)


# A-law compression
# https://en.wikipedia.org/wiki/A-law_algorithm
a = 87.6

decompressed = np.zeros_like(compressed)

# expansion depends on value of y from algorithm on wikipedia
for i in range(len(compressed)):

    left = np.abs(compressed[i,0])
    right = np.abs(compressed[i,1])

    abs = max(left,right)

    if abs < 1/(1+np.log(a)):

        decompressed[i,0] = np.sign(compressed[i,0])*(left*(1+np.log(a))/a)
        decompressed[i,1] = np.sign(compressed[i,1])*(right*(1+np.log(a))/a)

    else:

        decompressed[i,0] = np.sign(compressed[i,0])*(np.exp(1+np.log(a))/a)
        decompressed[i,1] = np.sign(compressed[i,1])*(np.exp(1+np.log(a))/a)



#samples = np.sign(samples)*(np.log1p(a*np.abs(samples))/ np.log1p(a))

decompressed = np.clip(decompressed,-1,1)



# scale back to 16 bit PCM
decompressed = np.int16(decompressed*32767)


wavfile.write("./code/wav/a_decompressed.wav",rate,decompressed)

print("success")