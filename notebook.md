# This is Cristian Ion's Engineering Notebook for Computers, Sound and Music

## 10/16/2024
- I introduced myself in the class Zulip.
- I completed part 1 of clipped in python

## 10/24/2024
- Completed clipped in python
- Downloaded Audacity and got more familiar with it and sound libraries in python

## 10/28/2024
- Created chord.py which creates and plays C4,E4,G4 separately and then together as a chord
- Looked into the pydub library
- Started Adaptive Tone Control

## 11/1/2024
- Created adaptive_tone_control.py which adjusts a D1D6D8.wav using Bart Massey's fft code
- Visualized how the compression affected my D1D6D8.wav in Audacity
- Explored more of Audacity
- TODO: create different fft compressions to see what gives better results

## 11/6/2024
- Created normalize.py to normalize audio to avoid clipping
- Created create_note.py to avoid rewriting same code

## 11/8/2024
- Added some changes to adaptive_tone_control.py
- Exploring other signal windows

## 11/14/2024
- Created audiocompressor.py
- Ran into a lot of system errors and trying to debug ffmpeg

## 11/15/2024
- Debugged a lot for ffmpeg, still getting issues with trying to play mp3
- Going to do audiocompression with wav instead, return to mp3 later

## 11/20/2024
- Added mu and a law compression for a sample wav file to compare mu and a
- TODO: do more compression methods and decompression, make them functions 

## 11/21/2024
- Created audiodecompressor.py, did a and mu law decompression of the compressed files
- TODO: add more compression,decompression, make them functions

## 11/25/2024
- Worked on personal project / researched options to accomplish it 

## 11/27/2024
- Restructured personal project

## 12/1/2024
- Worked on popgen, added triangle, square, and saw wave methods
    - to use, run with flag --tri True, or --sqr True, or --saw True

## 12/3/2024
- almost finished small keyboard (13 keys) for project

## 12//4/2024
- finished small piano for project, bound piano keys to laptop keys

## 12/8/2024
- attempted adding a song parameter for full_keyboard in project, many bugs, attempt on a later date
- solved clicking key errors

## 12/9/2024
- completed full_keyboard, bound two octaves to laptop keys that are optimal for me for basic playing. TODO: add option for user to customize keybindings

## 12/10/2024
- cleaned up portfolio, got rid of unneccessary files