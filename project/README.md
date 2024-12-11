# Piano Visualizer

## 88 Key Piano Keyboard
- Allows user to play with two options of keyboard
- piano.py is the file to run to get the keyboards using pygame
- keyfreq.py generates a dictionary key_freq that stores all 88 notes and their frequencies
- note_gen.py uses keyfreq.py to create wav files of all 88 notes
- ./notes is where all of the 88 notes are
- Has two run options:
    - python ./project/piano.py lets user play with a middle octave from C4 to C5. 
        - C4  : spacebar
        - C#4 : y
        - D4 : h
        - D#4 : u
        - E4 : j
        - F4 : k
        - F#4 : i
        - G4 : l
        - G#4 : o
        - A4 : ;
        - A#4 : p
        - B4 : '     quote
        - C5 : RETURN / ENTER

    - python ./project.piano.py --full True lets user play with 88 key piano from A0 to C8. Two octaves have keybinds for ease of play on my laptop keyboard. From C3 to C5. C4 to C5 is the same as above.
        - C3 : q
        - C#3 : 1
        - D3 : w
        - D#3 : 2
        - E3 : 3
        - F3 : r
        - F#3 : 4
        - G3 : t
        - G#3 : 5
        - A3 : v
        - A#3 : g
        - B3 : b