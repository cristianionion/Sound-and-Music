#https://mixbutton.com/mixing-articles/music-note-to-frequency-c
key_freq = {
    'a0' : 27.5,
    'a#0': 29.14,
    'b0' : 30.87
}



def f(): # 88 freq starting at a0 = 27.5 Hz
    notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#','a', 'a#', 'b']
    
    for i in range(7): # 7 octaves

        for j in range(len(notes)): # each note in each octave

            # if we reach 
            note = f"{notes[j]}{i+1}"
            freq = 27.5 * 2 ** ((3+j+i*len(notes))/12)

            key_freq[note]=freq



f()


key_freq['c8'] = 4186.01

print(key_freq, len(key_freq))
