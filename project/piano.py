import pygame
from keyfreq import key_freq #key frequency dictionary
import os
import argparse
import librosa
import sys

# if ran : python piano.py
#   middle octave + higher c that is playable off laptop/pc keyboard

# if ran : python ./project/piano.py --full True
#   get full 88 key keyboard, next add a way to take song input,


ap = argparse.ArgumentParser()
ap.add_argument('--full', type=bool, default=False)
ap.add_argument('--song', default=None)
args = ap.parse_args()

# full-keyboard option
full = bool(args.full)

# if there is song input to full-piano
# https://librosa.org/doc/main/generated/librosa.load.html
"""
TODO:
song = args.song
if full and type(song) == str:
    y, sr = librosa.load("./project/"+song)
    print("HELLLOOO")
    print(y,sr)
    sys.exit(0)
"""

# https://www.geeksforgeeks.org/pygame-tutorial/


pygame.init()

#print(pygame.init())

# display size

if not full:
    width,height = 800,500
    surface = pygame.display.set_mode((width,height))
else:
    width,height = 1900,400
    surface = pygame.display.set_mode((width,height))

# background color
color = (220,220,220)
surface.fill(color)
pygame.display.flip()


# app title
pygame.display.set_caption('Keyboard :)')


# logo for app, free stock image from pexels
# https://www.pexels.com/search/piano%20keyboard/
image = pygame.image.load('./project/keyboard.jpg')
pygame.display.set_icon(image)


# load sounds from key_freq
# pygame sound functions
# https://www.pygame.org/docs/ref/mixer.html
sounds = {}
for note,freq in key_freq.items():
    path = os.path.join('./project/notes/',f"{note}.wav")
    sounds[note] = pygame.mixer.Sound(path)

#print(sounds)



# have two versions of keyboard, one for an octave, one for all of it
def octave():


    # 7+1  white keys, 5 black keys
    key_width = width/8
    key_height = 200

    # black outline of keys
    ### make a variable for keywidth , have as little ints around
    # pygame keyboard binding for rects
    # https://www.pygame.org/docs/ref/key.html
    c1outline = pygame.draw.rect(surface,(0,0,0),(0*key_width,key_height,key_width,key_height),0)
    doutline = pygame.draw.rect(surface,(0,0,0),(1*key_width,key_height,key_width,key_height),0)
    eoutline = pygame.draw.rect(surface,(0,0,0),(2*key_width,key_height,key_width,key_height),0)
    foutline = pygame.draw.rect(surface,(0,0,0),(3*key_width,key_height,key_width,key_height),0)
    goutline = pygame.draw.rect(surface,(0,0,0),(4*key_width,key_height,key_width,key_height),0)
    aoutline = pygame.draw.rect(surface,(0,0,0),(5*key_width,key_height,key_width,key_height),0)
    boutline = pygame.draw.rect(surface,(0,0,0),(6*key_width,key_height,key_width,key_height),0)
    c2outline = pygame.draw.rect(surface,(0,0,0),(7*key_width,key_height,key_width,key_height),0)

    # white keys
    c1 = pygame.draw.rect(surface,(255,255,255),(0*key_width+1,key_height+1,key_width-2,key_height-2),0)
    d = pygame.draw.rect(surface,(255,255,255),(1*key_width+1,key_height+1,key_width-2,key_height-2),0)
    e = pygame.draw.rect(surface,(255,255,255),(2*key_width+1,key_height+1,key_width-2,key_height-2),0)
    f = pygame.draw.rect(surface,(255,255,255),(3*key_width+1,key_height+1,key_width-2,key_height-2),0)
    g = pygame.draw.rect(surface,(255,255,255),(4*key_width+1,key_height+1,key_width-2,key_height-2),0)
    a = pygame.draw.rect(surface,(255,255,255),(5*key_width+1,key_height+1,key_width-2,key_height-2),0)
    b = pygame.draw.rect(surface,(255,255,255),(6*key_width+1,key_height+1,key_width-2,key_height-2),0)
    c2 = pygame.draw.rect(surface,(255,255,255),(7*key_width+1,key_height+1,key_width-2,key_height-2),0)
    
    # black keys
    cs = pygame.draw.rect(surface,(0,0,0),(key_width*.8,key_height,key_width*.4,key_height*.6),0)
    ds = pygame.draw.rect(surface,(0,0,0),(key_width+key_width*.8,key_height,key_width*.4,key_height*.6),0)
    fs = pygame.draw.rect(surface,(0,0,0),(3*key_width+key_width*.8,key_height,key_width*.4,key_height*.6),0)
    gs = pygame.draw.rect(surface,(0,0,0),(4*key_width+key_width*.8,key_height,key_width*.4,key_height*.6),0)
    aas = pygame.draw.rect(surface,(0,0,0),(5*key_width+key_width*.8,key_height,key_width*.4,key_height*.6),0)
    



    keys = [
        {"note": "c4", "key": pygame.K_SPACE, "rectangle": c1, "sound": sounds.get("c4"), "pressed": False, "playing": False},
        {"note": "c#4", "key": pygame.K_y, "rectangle": cs, "sound": sounds.get("c#4"), "pressed": False, "playing": False},
        {"note": "d4", "key": pygame.K_h, "rectangle": d, "sound": sounds.get("d4"), "pressed": False, "playing": False},
        {"note": "d#4", "key": pygame.K_u, "rectangle": ds, "sound": sounds.get("d#4"), "pressed": False, "playing": False},
        {"note": "e4", "key": pygame.K_j, "rectangle": e, "sound": sounds.get("e4"), "pressed": False, "playing": False},
        {"note": "f4", "key": pygame.K_k, "rectangle": f, "sound": sounds.get("f4"), "pressed": False, "playing": False},
        {"note": "f#4", "key": pygame.K_i, "rectangle": fs, "sound": sounds.get("f#4"), "pressed": False, "playing": False},
        {"note": "g4", "key": pygame.K_l, "rectangle": g, "sound": sounds.get("g4"), "pressed": False, "playing": False},
        {"note": "g#4", "key": pygame.K_o, "rectangle": gs, "sound": sounds.get("g#4"), "pressed": False, "playing": False},
        {"note": "a4", "key": pygame.K_SEMICOLON, "rectangle": a, "sound": sounds.get("a4"), "pressed": False, "playing": False},
        {"note": "a#4", "key": pygame.K_p, "rectangle": aas, "sound": sounds.get("a#4"), "pressed": False, "playing": False},
        {"note": "b4", "key": pygame.K_QUOTE, "rectangle": b, "sound": sounds.get("b4"), "pressed": False, "playing": False},
        {"note": "c5", "key": pygame.K_RETURN, "rectangle": c2, "sound": sounds.get("c5"), "pressed": False, "playing": False}
    ]

    pygame.display.update()

    return keys


### for displaying full keyboard, find a way to make it iteratively
#   for each key, we need
#       key name
#       is it being pressed
#       pygame object
#       map to sound 

def full_keyboard():

    # 52 white keys, 36 black keys
    key_width = width/52
    key_height = 150

    keys = []

    white_keys=[]
    for i in range(52):
        # white key outlines
        pygame.draw.rect(surface,(0,0,0),(i*key_width,key_height,key_width,key_height),0)
        # white keys
        k = pygame.draw.rect(surface,(255,255,255),(i*key_width+1,key_height+1,key_width-2,key_height-2),0)
        white_keys.append(k)


    
    black_keys=[]
    # first one before we start an octave from c
    black_keys.append(pygame.draw.rect(surface,(0,0,0),(key_width*.8,key_height,key_width*.4,key_height*.6),0))

    for i in range(7): # 7 full octaves
        offset = i*7*key_width +2*key_width # each octave + first two white keys before octave starting with c
        
        black_keys.append(pygame.draw.rect(surface,(0,0,0),(offset+key_width*.8,key_height,key_width*.4,key_height*.6),0))
        black_keys.append(pygame.draw.rect(surface,(0,0,0),(offset+key_width+key_width*.8,key_height,key_width*.4,key_height*.6),0))
        black_keys.append(pygame.draw.rect(surface,(0,0,0),(offset+3*key_width+key_width*.8,key_height,key_width*.4,key_height*.6),0))
        black_keys.append(pygame.draw.rect(surface,(0,0,0),(offset+4*key_width+key_width*.8,key_height,key_width*.4,key_height*.6),0))
        black_keys.append(pygame.draw.rect(surface,(0,0,0),(offset+5*key_width+key_width*.8,key_height,key_width*.4,key_height*.6),0))
    

    # combine all keys in one list
    # start with the three before octave that starts on c1

    keys.append({"note": "a0", "key": None, "rectangle": white_keys[0], "sound": sounds.get("a0"), "pressed": False, "playing": False})    
    keys.append({"note": "a#0", "key": None, "rectangle": black_keys[0], "sound": sounds.get("a#0"), "pressed": False, "playing": False})    
    keys.append({"note": "b0", "key": None, "rectangle": white_keys[1], "sound": sounds.get("b0"), "pressed": False, "playing": False})    
    
    
    for i in range(7): # 7 full octaves
        oct = i+1

        keys.append({"note": "c"+str(oct), "key": None, "rectangle": white_keys[i*7+2], "sound": sounds.get("c"+str(oct)), "pressed": False, "playing": False})
        keys.append({"note": "c#"+str(oct), "key": None, "rectangle": black_keys[i*5+1], "sound": sounds.get("c#"+str(oct)), "pressed": False, "playing": False})
        keys.append({"note": "d"+str(oct), "key": None, "rectangle": white_keys[i*7+3], "sound": sounds.get("d"+str(oct)), "pressed": False, "playing": False})
        keys.append({"note": "d#"+str(oct), "key": None, "rectangle": black_keys[i*5+2], "sound": sounds.get("d#"+str(oct)), "pressed": False, "playing": False})
        keys.append({"note": "e"+str(oct), "key": None, "rectangle": white_keys[i*7+4], "sound": sounds.get("e"+str(oct)), "pressed": False, "playing": False})
        keys.append({"note": "f"+str(oct), "key": None, "rectangle": white_keys[i*7+5], "sound": sounds.get("f"+str(oct)), "pressed": False, "playing": False})
        keys.append({"note": "f#"+str(oct), "key": None, "rectangle": black_keys[i*5+3], "sound": sounds.get("f#"+str(oct)), "pressed": False, "playing": False})
        keys.append({"note": "g"+str(oct), "key": None, "rectangle": white_keys[i*7+6], "sound": sounds.get("g"+str(oct)), "pressed": False, "playing": False})
        keys.append({"note": "g#"+str(oct), "key": None, "rectangle": black_keys[i*5+4], "sound": sounds.get("g#"+str(oct)), "pressed": False, "playing": False})
        keys.append({"note": "a"+str(oct), "key": None, "rectangle": white_keys[i*7+7], "sound": sounds.get("a"+str(oct)), "pressed": False, "playing": False})
        keys.append({"note": "a#"+str(oct), "key": None, "rectangle": black_keys[i*5+5], "sound": sounds.get("a#"+str(oct)), "pressed": False, "playing": False})
        keys.append({"note": "b"+str(oct), "key": None, "rectangle": white_keys[i*7+8], "sound": sounds.get("b"+str(oct)), "pressed": False, "playing": False})
    #{"note": "c4", "key": pygame.K_SPACE, "rectangle": c1, "sound": sounds.get("c4"), "pressed": False, "playing": False},

    keys.append({"note": "c8", "key": None, "rectangle": white_keys[-1], "sound": sounds.get("c8"), "pressed": False, "playing": False})


    ### default key bindings for my personal usage
    for key in keys:
        # right hand, treble, c4-c5
        if key["note"] == 'c4':
            key["key"] = pygame.K_SPACE
        elif key["note"] == 'c#4':
            key["key"] = pygame.K_y
        elif key["note"] == 'd4':
            key["key"] = pygame.K_h
        elif key["note"] == 'd#4':
            key["key"] = pygame.K_u
        elif key["note"] == 'e4':
            key["key"] = pygame.K_j
        elif key["note"] == 'f4':
            key["key"] = pygame.K_k
        elif key["note"] == 'f#4':
            key["key"] = pygame.K_i
        elif key["note"] == 'g4':
            key["key"] = pygame.K_l
        elif key["note"] == 'g#4':
            key["key"] = pygame.K_o
        elif key["note"] == 'a4':
            key["key"] = pygame.K_SEMICOLON
        elif key["note"] == 'a#4':
            key["key"] = pygame.K_p
        elif key["note"] == 'b4':
            key["key"] = pygame.K_QUOTE
        elif key["note"] == 'c5':
            key["key"] = pygame.K_RETURN
        
        # left hand, bass, c3-b3
        elif key["note"] == 'c3':
            key["key"] = pygame.K_q
        elif key["note"] == 'c#3':
            key["key"] = pygame.K_1
        elif key["note"] == 'd3':
            key["key"] = pygame.K_w
        elif key["note"] == 'd#3':
            key["key"] = pygame.K_2
        elif key["note"] == 'e3':
            key["key"] = pygame.K_e
        elif key["note"] == 'f3':
            key["key"] = pygame.K_r
        elif key["note"] == 'f#3':
            key["key"] = pygame.K_4
        elif key["note"] == 'g3':
            key["key"] = pygame.K_t
        elif key["note"] == 'g#3':
            key["key"] = pygame.K_5
        elif key["note"] == 'a3':
            key["key"] = pygame.K_v
        elif key["note"] == 'a#3':
            key["key"] = pygame.K_g
        elif key["note"] == 'b3':
            key["key"] = pygame.K_b


    

    return keys
    #cs = pygame.draw.rect(surface,(0,0,0),(key_width*.8,key_height,key_width*.4,key_height*.6),0)


# highlight keys while they are being played, or until end of wav (5s)
def highlight():

    for key in keys:
        
        if key["pressed"]:
            color = (200,50,50)
        else:
            if len(key["note"]) == 2:
                color = (255,255,255)
            else:
                color = (0,0,0)

        pygame.draw.rect(surface,color,key["rectangle"])

    # need to redraw black keys, right half gets cut off

    for key in keys:

        if len(key["note"])==3:    
            if key["pressed"]:
                color = (200,50,50)
            else:
                color = (0,0,0)
            pygame.draw.rect(surface,color,key["rectangle"])

"""
TODO: finish implementing this, customizes user keybinds to their liking
#https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
rect = pygame.Rect(10,0,150,50)
r = pygame.draw.rect(surface,(0,200,250),rect)
font = pygame.font.get_default_font()
writing = pygame.font.SysFont(font,20)
writing = writing.render("Customize KeyBinds",True,(0,0,0))
text_r = writing.get_rect()
text_r.center = r.center
surface.blit(writing,text_r)
"""



# run it
running = True
if not full: # if we just want the middle octave
    keys = octave()

    while running == True:
        
        for event in pygame.event.get():



            if event.type == pygame.QUIT:
                running = False


            # play sound when a key is pressed
            if event.type == pygame.KEYDOWN:
                for key in keys:
                    if event.key == key["key"] and not key["pressed"]:
                        key["pressed"] = True
                        if key["playing"] == False:
                            key["sound"].play()
                            key["playing"] = True 
                            highlight()



            # play sound when a key is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check black keys first, both black and white are playing, give black keys priority
                key_pressed = False
                for key in keys:
                    if len(key["note"]) == 3:  # black keys have a note name length of 3 c#3 vs c6
                        if key["rectangle"].collidepoint(event.pos):
                            if not key["pressed"]:
                                key["pressed"] = True
                                if not key["playing"]:
                                    key["sound"].play()
                                    key["playing"] = True
                                    highlight()
                            key_pressed = True
                            break  # top checking other keys if a black key is pressed

                # check white keys only if no black key was pressed
                if not key_pressed:
                    for key in keys:
                        if len(key["note"]) == 2:  
                            if key["rectangle"].collidepoint(event.pos):
                                if not key["pressed"]:
                                    key["pressed"] = True
                                    if not key["playing"]:
                                        key["sound"].play()
                                        key["playing"] = True
                                        highlight()
                                break


            # stop sound if mouse is released off key
            if event.type == pygame.MOUSEBUTTONUP:
                for key in keys:
                    if key["pressed"]:
                        key["pressed"] = False
                        if key["playing"]:
                            key["sound"].stop()
                            key["playing"] = False
                            highlight()


            # if key is released, stop playing key
            if event.type == pygame.KEYUP:
                #print("KEY RELEASED")
                #print(keys[0])
                for key in keys:

                    # check which key(s) are pressed, which are released
                    if event.key == key["key"] and key["pressed"]:
                        key["pressed"]=False
                        if key["playing"]:

                            # stop playing since it was released
                            key["sound"].stop() 
                            
                            key["playing"] = False
                            highlight()
        pygame.display.update()


if full: # if user wants full 88 key keyboard
    keys = full_keyboard()


    while running == True:
        
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False


            if event.type == pygame.KEYDOWN:
                for key in keys:
                    if event.key == key["key"] and not key["pressed"]:
                        key["pressed"] = True
                        if key["playing"] == False:
                            key["sound"].play()
                            key["playing"] = True 
                            highlight()

            if event.type == pygame.MOUSEBUTTONDOWN:
    # Check black keys first
                key_pressed = False
                for key in keys:
                    if len(key["note"]) == 3:  
                        if key["rectangle"].collidepoint(event.pos):
                            if not key["pressed"]:
                                key["pressed"] = True
                                if not key["playing"]:
                                    key["sound"].play()
                                    key["playing"] = True
                                    highlight()
                            key_pressed = True
                            break  


                if not key_pressed:
                    for key in keys:
                        if len(key["note"]) == 2:  
                            if key["rectangle"].collidepoint(event.pos):
                                if not key["pressed"]:
                                    key["pressed"] = True
                                    if not key["playing"]:
                                        key["sound"].play()
                                        key["playing"] = True
                                        highlight()
                                break



            if event.type == pygame.MOUSEBUTTONUP:
                for key in keys:
                    if key["pressed"]:
                        key["pressed"] = False
                        if key["playing"]:
                            key["sound"].stop()
                            key["playing"] = False
                            highlight()


            # if key is released
            if event.type == pygame.KEYUP:
                #print("KEY RELEASED")
                #print(keys[0])
                for key in keys:

                    # check which key(s) are pressed, which are released
                    if event.key == key["key"] and key["pressed"]:
                        key["pressed"]=False
                        if key["playing"]:

                            # stop playing since it was released
                            key["sound"].stop() 
                            
                            key["playing"] = False
                            highlight()
        pygame.display.update()




#print(full)

#print(keys[-1], len(keys))


#print(song, type(song))
