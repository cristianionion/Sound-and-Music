# Sound-and-Music
## Cristian Ion

### Contents:
- clipped.py : generates a sine wave and clipped sine wave, and then plays them
- chord.py : creates A4,C4,E4,G4 notes, C4 chord, and plays C4,E4,G4, and C4 Chord
- adaptive_tone_control.py : creates D1D6D8.wav, and uses Bart Massey's fft to adjust it, will look at other ffts next.\
WARNING: adaptive_tone_control.py when ran plays a very unpleasant sound
- audiocompressor.py : does Mu-Law and A-Law companding of a sample .wav
- audiodecompressor.py : does Mu-Law and A-Law decompanding of a sample .wav
- create_note.py : creates note, takes note name and frequency as parameters, outputs a wav file
- popgen2.py : took popgen.py from class repo, and added triangle, square, and saw wave methods and parameters: run with flags --tri True or --sqr True or --saw True
- Project folder:
    - piano.py : implementation of 88 key keyboard, with smaller C4-C5 option for playing
    - keyfreq.py : creates dictionary of notes and their frequencies
    - note_gen.py : creates all 88 notes in wav files that I need, stored in Note folder


