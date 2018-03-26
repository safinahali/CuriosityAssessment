try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    pass

import pygame, sys, random, time, pygame_textinput
from random import randint
from pygame.locals import*
# import speech_recognition as sr
from os import path

import moviepy
# print(moviepy.__file__)

user_input = input("Participant ID: ")

# try:
#         import android
# except Import:
#         android = None

# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800

#BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLACK = (0, 0, 0)

FPS = 30

# --- classses --- (CamelCase names)

# empty

# --- functions --- (lower_case names)

# empty

# --- main ---

# - init -

pygame.init()
pygame.mixer.init()
# if android:
#         android.init()
#         android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

#screen_rect = screen.get_rect()

pygame.display.set_caption("Curiosity")

# - objects -

#Background
bg = pygame.image.load("assets/bg.png")
# overlay = pygame.image.load("assets/overlay.png")

#!/usr/bin/python3

pygame.init()

# Create TextInput-object
textinput = pygame_textinput.TextInput()

# rectangleA = pygame.rect.Rect(randint(0, SCREEN_WIDTH - 20), randint(0, SCREEN_HEIGHT - 20), 17, 17)
# rectangleB = pygame.rect.Rect(randint(0, SCREEN_WIDTH - 20), randint(0, SCREEN_HEIGHT - 20), 17, 17)
hammerfab_dragging = False
keyfab_dragging = False
wclockfab_dragging = False
chest_visible = True
drum_visible = True
clock_unmoved = True


i = 0
j = 0
number_of_manipulations = 0
objects_manipulated = 0
guesses = 0
sensory_interactions_sound = 0
ambiguous_objects_manipulated = 0
successful_manipulations = 0
hidden = 0

# while j < 12:
#         img[j] = pygame.image.load('present' + str(j) + '.png')
#         presentImage[j] = img[j].get_rect()
#         presentImage[j].x = randint (0, SCREEN_WIDTH - 20)
#         presentImage[j].y = randint (0, SCREEN_HEIGHT - 0)

img0 = pygame.image.load('assets/present0.png')
presentImage0 = img0.get_rect()
presentImage0.x = 538
presentImage0.y = 641

collectedPresentImage0 = img0.get_rect()
collectedPresentImage0.x = 2000
collectedPresentImage0.y = 2000

img1 = pygame.image.load('assets/present1.png')
presentImage1 = img1.get_rect()
presentImage1.x = 818
presentImage1.y = 612

collectedPresentImage1 = img1.get_rect()
collectedPresentImage1.x = 2000
collectedPresentImage1.y = 2000

img2 = pygame.image.load('assets/present2.png')
presentImage2 = img2.get_rect()
presentImage2.x = 916
presentImage2.y = 446

collectedPresentImage2 = img2.get_rect()
collectedPresentImage2.x = 2000
collectedPresentImage2.y = 2000

img3 = pygame.image.load('assets/present3.png')
presentImage3 = img3.get_rect()
presentImage3.x = 1181
presentImage3.y = 339

collectedPresentImage3 = img3.get_rect()
collectedPresentImage3.x = 2000
collectedPresentImage3.y = 2000

img4 = pygame.image.load('assets/present4.png')
presentImage4 = img4.get_rect()
presentImage4.x = 1118
presentImage4.y = 135

collectedPresentImage4 = img4.get_rect()
collectedPresentImage4.x = 2000
collectedPresentImage4.y = 2000

img5 = pygame.image.load('assets/present5.png')
presentImage5 = img5.get_rect()
presentImage5.x = 628
presentImage5.y = 76

collectedPresentImage5 = img5.get_rect()
collectedPresentImage5.x = 2000
collectedPresentImage5.y = 2000

img6 = pygame.image.load('assets/present6.png')
presentImage6 = img6.get_rect()
presentImage6.x = 546
presentImage6.y = 428

collectedPresentImage6 = img6.get_rect()
collectedPresentImage6.x = 2000
collectedPresentImage6.y = 2000

img7 = pygame.image.load('assets/present7.png')
presentImage7 = img7.get_rect()
presentImage7.x = 535
presentImage7.y = 477

collectedPresentImage7 = img7.get_rect()
collectedPresentImage7.x = 2000
collectedPresentImage7.y = 2000

img8 = pygame.image.load('assets/present8.png')
presentImage8 = img8.get_rect()
presentImage8.x = 656
presentImage8.y = 435

collectedPresentImage8 = img8.get_rect()
collectedPresentImage8.x = 2000
collectedPresentImage8.y = 2000

tree = pygame.image.load('assets/tree.png')
treefab = tree.get_rect()
treefab.x = 509
treefab.y = 51

shelf = pygame.image.load('assets/shelf.png')
shelffab = shelf.get_rect()
shelffab.x = 987
shelffab.y = 154

drum = pygame.image.load('assets/drum.png')
drumfab = drum.get_rect()
drumfab.x = 489
drumfab.y = 582

chest = pygame.image.load('assets/chest.png')
chestfab = chest.get_rect()
chestfab.x = 761
chestfab.y = 545

wclock = pygame.image.load('assets/wclock.png')
wclockfab = wclock.get_rect()
wclockfab.x = 786
wclockfab.y = 43

hammer = pygame.image.load('assets/hammer.png')
hammerfab = hammer.get_rect()
hammerfab.x = 1103
hammerfab.y = 583

key = pygame.image.load('assets/key.png')
keyfab = key.get_rect()
keyfab.x = 1030
keyfab.y = 231

done = pygame.image.load('assets/done.png')
donefab = done.get_rect()
donefab.x = 1138
donefab.y = 726

img9 = pygame.image.load('assets/present9.png')
presentImage9 = img9.get_rect()
presentImage9.x = 832
presentImage9.y = 86

collectedPresentImage9 = img9.get_rect()
collectedPresentImage9.x = 2000
collectedPresentImage9.y = 2000

#overlay
overlay = pygame.image.load('assets/overlay.png')
overlayfab = overlay.get_rect()
overlayfab.x = 2000
overlayfab.y = 2000

oguess = pygame.image.load('assets/oguess.png')
overlayguess = oguess.get_rect()
overlayguess.x = 2000
overlayguess.y = 2000

oskip = pygame.image.load('assets/oskip.png')
overlayskip = oskip.get_rect()
overlayskip.x = 2000
overlayskip.y = 2000

oguessdone = pygame.image.load('assets/oguessdone.png')
overlayguessdone = oguessdone.get_rect()
overlayguessdone.x = 2000
overlayguessdone.y = 2000

overlayOn = False

#sounds
blip = pygame.mixer.Sound("assets/blip.wav")
chop = pygame.mixer.Sound("assets/chop.wav")
magic = pygame.mixer.Sound("assets/magic.wav")
empty = pygame.mixer.Sound("assets/Silent.wav")
dog = pygame.mixer.Sound("assets/dog.wav")
ball = pygame.mixer.Sound("assets/ball.wav")
bike = pygame.mixer.Sound("assets/bike.wav")
cloth = pygame.mixer.Sound("assets/cloth.wav")
coins = pygame.mixer.Sound("assets/coins.wav")
cowboy = pygame.mixer.Sound("assets/cowboy.wav")
horn = pygame.mixer.Sound("assets/horn.wav")
pig = pygame.mixer.Sound("assets/pig.wav")
rattle = pygame.mixer.Sound("assets/rattle.wav")
sad = pygame.mixer.Sound("assets/sad.wav")
train = pygame.mixer.Sound("assets/train.wav")


# img10 = pygame.image.load('present10.png')
# presentImage10 = img10.get_rect()
# presentImage10.x = randint (0, SCREEN_WIDTH - 20)
# presentImage10.y = randint (0, SCREEN_HEIGHT - 20)

# img11 = pygame.image.load('present11.png')
# presentImage11 = img11.get_rect()
# presentImage11.x = randint (0, SCREEN_WIDTH - 20)
# presentImage11.y = randint (0, SCREEN_HEIGHT - 20)

# - mainloop -

clock = pygame.time.Clock()

running = True

#start time logging
from datetime import datetime
f = open('log.txt','a')
f.write('\n' + str(datetime.now()) + ' , session start')
f.write('\n' + user_input)
f.close()

while running:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
                

                

                if event.button == 1:


                        f = open('log.txt','a')
                        f.write('\n' + '[Click Record] = ' + str(event.pos))
                        f.close()  

                        # drag the hammer
                        if hammerfab.collidepoint(event.pos) and overlayOn == False:
                                hammerfab_dragging = True
                                mouse_x, mouse_y = event.pos
                                offset_x = hammerfab.x - mouse_x
                                offset_y = hammerfab.y - mouse_y
                                print ('manipulation')
                                number_of_manipulations += 1


                        #drag the keys
                        if keyfab.collidepoint(event.pos) and overlayOn == False:
                                keyfab_dragging = True
                                mouse_x, mouse_y = event.pos
                                offset_x = keyfab.x - mouse_x
                                offset_y = keyfab.y - mouse_y
                                print ('manipulation')
                                number_of_manipulations += 1

                        #drag the wclock
                        if wclockfab.collidepoint(event.pos) and overlayOn == False:
                                wclockfab_dragging = True
                                mouse_x, mouse_y = event.pos
                                offset_x = wclockfab.x - mouse_x
                                offset_y = wclockfab.y - mouse_y
                                print ('manipulation')
                                number_of_manipulations += 1        


                        #Collecting a present
                        if presentImage0.collidepoint(event.pos) and drum_visible == False and overlayOn == False:
                                mouse_x, mouse_y = event.pos
                                #Log present collection
                                f = open('log.txt','a')
                                f.write('\n' + 'Found present' + str(i))
                                f.close()
                                i += 1
                                presentImage0.x = 2000
                                presentImage0.y = 2000
                                print('working')

                                #play sound
                                blip.play()
                                print ('playing')
                                #time.sleep(0.5)

                                time.sleep(0.5)
                                overlayfab.x = 0
                                overlayfab.y = 0
                                
                                collectedPresentImage0.x = 601
                                collectedPresentImage0.y = 312
                                overlayguess.x = 505
                                overlayguess.y = 512
                                overlayskip.x = 689
                                overlayskip.y = 512

                                hidden += 1

                                overlayOn = True

                         #Collecting a present
                        if presentImage1.collidepoint(event.pos) and chest_visible == False and overlayOn == False:
                                mouse_x, mouse_y = event.pos
                                #Log present collection
                                f = open('log.txt','a')
                                f.write('\n' + 'Found present' + str(i))
                                f.close()
                                i += 1

                                #play sound
                                blip.play()
                                print ('playing')
                                #time.sleep(1)

                                #ugly solution to make present disappear
                                presentImage1.x = 2000
                                presentImage1.y = 2000
                                print('working')

                                time.sleep(0.5)
                                overlayfab.x = 0
                                overlayfab.y = 0
                                
                                collectedPresentImage1.x = 601
                                collectedPresentImage1.y = 312
                                overlayguess.x = 505
                                overlayguess.y = 512
                                overlayskip.x = 689
                                overlayskip.y = 512

                                overlayOn = True

                                hidden += 1

                         #Collecting a present
                        if presentImage2.collidepoint(event.pos) and overlayOn == False:
                                mouse_x, mouse_y = event.pos
                                #Log present collection
                                f = open('log.txt','a')
                                f.write('\n' + 'Found present' + str(i))
                                f.close()
                                i += 1
                                presentImage2.x = 2000
                                presentImage2.y = 2000
                                print('working')

                                #play sound
                                blip.play()
                                print ('playing')
                                #time.sleep(0.5)

                                time.sleep(0.5)
                                overlayfab.x = 0
                                overlayfab.y = 0
                                
                                collectedPresentImage2.x = 601
                                collectedPresentImage2.y = 312
                                overlayguess.x = 505
                                overlayguess.y = 512
                                overlayskip.x = 689
                                overlayskip.y = 512

                                overlayOn = True

                         #Collecting a present
                        if presentImage3.collidepoint(event.pos) and overlayOn == False:
                                mouse_x, mouse_y = event.pos
                                #Log present collection
                                f = open('log.txt','a')
                                f.write('\n' + 'Found present' + str(i))
                                f.close()       
                                i += 1
                                presentImage3.x = 2000
                                presentImage3.y = 2000
                                print('working')

                                #play sound
                                blip.play()
                                print ('playing')
                                #time.sleep(0.5)

                                time.sleep(0.5)
                                overlayfab.x = 0
                                overlayfab.y = 0
                                
                                collectedPresentImage3.x = 601
                                collectedPresentImage3.y = 312
                                overlayguess.x = 505
                                overlayguess.y = 512
                                overlayskip.x = 689
                                overlayskip.y = 512

                                overlayOn = True


                         #Collecting a present
                        if presentImage4.collidepoint(event.pos) and overlayOn == False:
                                mouse_x, mouse_y = event.pos
                                #Log present collection
                                f = open('log.txt','a')
                                f.write('\n' + 'Found present' + str(i))
                                f.close()
                                i += 1
                                presentImage4.x = 2000
                                presentImage4.y = 2000
                                print('working')

                                #play sound
                                blip.play()
                                print ('playing')
                                #time.sleep(0.5)

                                time.sleep(0.5)
                                overlayfab.x = 0
                                overlayfab.y = 0
                                
                                collectedPresentImage4.x = 601
                                collectedPresentImage4.y = 312
                                overlayguess.x = 505
                                overlayguess.y = 512
                                overlayskip.x = 689
                                overlayskip.y = 512

                                overlayOn = True

                         #Collecting a present
                        if presentImage5.collidepoint(event.pos) and overlayOn == False:
                                mouse_x, mouse_y = event.pos
                                #Log present collection
                                f = open('log.txt','a')
                                f.write('\n' + 'Found present' + str(i))
                                f.close()
                                i += 1
                                presentImage5.x = 2000
                                presentImage5.y = 2000
                                print('working')

                                #play sound
                                
                                blip.play()
                                print ('playing')

                                time.sleep(0.5)
                                overlayfab.x = 0
                                overlayfab.y = 0
                                
                                collectedPresentImage5.x = 601
                                collectedPresentImage5.y = 312
                                overlayguess.x = 505
                                overlayguess.y = 512
                                overlayskip.x = 689
                                overlayskip.y = 512

                                overlayOn = True
                                

                        #Collecting a present
                        if presentImage6.collidepoint(event.pos) and overlayOn == False:
                                mouse_x, mouse_y = event.pos
                                #Log present collection
                                f = open('log.txt','a')
                                f.write('\n' + 'Found present' + str(i))
                                f.close()
                                i += 1
                                presentImage6.x = 2000
                                presentImage6.y = 2000
                                print('working')

                                #play sound
                                blip.play()
                                print ('playing')

                                time.sleep(0.5)
                                overlayfab.x = 0
                                overlayfab.y = 0
                                
                                collectedPresentImage6.x = 601
                                collectedPresentImage6.y = 312
                                overlayguess.x = 505
                                overlayguess.y = 512
                                overlayskip.x = 689
                                overlayskip.y = 512

                                overlayOn = True

                        #Collecting a present
                        if presentImage7.collidepoint(event.pos) and overlayOn == False:
                                mouse_x, mouse_y = event.pos
                                #Log present collection
                                f = open('log.txt','a')
                                f.write('\n' + 'Found present ' + str(i))
                                f.close()
                                i += 1
                                presentImage7.x = 2000
                                presentImage7.y = 2000
                                print('working')

                                #play sound
                                blip.play()
                                print ('playing')

                                time.sleep(0.5)
                                overlayfab.x = 0
                                overlayfab.y = 0
                                
                                collectedPresentImage7.x = 601
                                collectedPresentImage7.y = 312
                                overlayguess.x = 505
                                overlayguess.y = 512
                                overlayskip.x = 689
                                overlayskip.y = 512

                                overlayOn = True

                        #Collecting a present
                        if presentImage8.collidepoint(event.pos) and overlayOn == False:
                                mouse_x, mouse_y = event.pos
                                #Log present collection
                                f = open('log.txt','a')
                                f.write('\n' + 'Found present ' + str(i))
                                f.close()
                                i += 1
                                presentImage8.x = 2000
                                presentImage8.y = 2000

                                #play sound
                                blip.play()
                                
                                time.sleep(0.5)
                                overlayfab.x = 0
                                overlayfab.y = 0
                                
                                collectedPresentImage8.x = 601
                                collectedPresentImage8.y = 312
                                overlayguess.x = 505
                                overlayguess.y = 512
                                overlayskip.x = 689
                                overlayskip.y = 512

                                overlayOn = True

                        #Skipping the guessing, erasing the overlay
                        if overlayskip.collidepoint(event.pos):
                                mouse_x, mouse_y = event.pos
                                print('skipping')
                                #Log skipping time - incomplete
                                # f = open('log.txt','a')
                                # f.write('\n' + 'Found present' + str(i))
                                # f.close()
                                
                                overlayfab.x = 2000
                                overlayfab.y = 2000
                                collectedPresentImage0.x = collectedPresentImage1.x = collectedPresentImage2.x = collectedPresentImage3.x = collectedPresentImage4.x = collectedPresentImage5.x = collectedPresentImage6.x = collectedPresentImage7.x = collectedPresentImage8.x = collectedPresentImage9.x = 2000
                                collectedPresentImage0.y = collectedPresentImage1.y = collectedPresentImage2.y = collectedPresentImage3.y = collectedPresentImage4.y = collectedPresentImage5.y = collectedPresentImage6.y = collectedPresentImage7.y = collectedPresentImage8.y = collectedPresentImage9.y = 2000
                                overlayguess.x = 2000
                                overlayguess.y = 2000
                                overlayskip.x = 2000
                                overlayskip.y = 2000

                                overlayOn = False

                        if overlayguess.collidepoint(event.pos):
                                mouse_x, mouse_y = event.pos
                                print('guessing')
                                #Log skipping time - incomplete
                                # f = open('log.txt','a')
                                # f.write('\n' + 'Found present' + str(i))
                                # f.close()
                                guesses += 1

                                overlayskip.x = 2000
                                overlayskip.y = 2000
                                overlayguessdone.x = 689
                                overlayguessdone.y = 512

                        if overlayguessdone.collidepoint(event.pos):
                                mouse_x, mouse_y = event.pos
                                print('done guessing')
                                #Log skipping time - incomplete
                                # f = open('log.txt','a')
                                # f.write('\n' + 'Found present' + str(i))
                                # f.close()
                                
                                overlayfab.x = 2000
                                overlayfab.y = 2000
                                collectedPresentImage0.x = collectedPresentImage1.x = collectedPresentImage2.x = collectedPresentImage3.x = collectedPresentImage4.x = collectedPresentImage5.x = collectedPresentImage6.x = collectedPresentImage7.x = collectedPresentImage8.x = collectedPresentImage9.x = 2000
                                collectedPresentImage0.y = collectedPresentImage1.y = collectedPresentImage2.y = collectedPresentImage3.y = collectedPresentImage4.y = collectedPresentImage5.y = collectedPresentImage6.y = collectedPresentImage7.y = collectedPresentImage8.y = collectedPresentImage9.y = 2000
                                overlayguess.x = 2000
                                overlayguess.y = 2000
                                overlayskip.x = 2000
                                overlayskip.y = 2000
                                overlayguessdone.x = 2000
                                overlayguessdone.y = 2000

                                overlayOn = False



                        #Collecting a present
                        if presentImage9.collidepoint(event.pos) and clock_unmoved == False:
                                mouse_x, mouse_y = event.pos
                                #Log present collection
                                f = open('log.txt','a')
                                f.write('\n' + 'Found present ' + str(i))
                                f.close()
                                i += 1
                                presentImage9.x = 2000
                                presentImage9.y = 2000
                                print('workinghid')

                                #play sound
                                blip.play()
                                print ('playing')
                                #time.sleep(0.5)

                                time.sleep(0.5)
                                overlayfab.x = 0
                                overlayfab.y = 0
                                
                                collectedPresentImage9.x = 601
                                collectedPresentImage9.y = 312
                                overlayguess.x = 505
                                overlayguess.y = 512
                                overlayskip.x = 689
                                overlayskip.y = 512

                                overlayOn = True

                                hidden += 1

                        #Shake0
                        if collectedPresentImage0.collidepoint(event.pos):
                                mouse_x, mouse_y = event.pos
                                #play sound
                                pig.play()
                                sensory_interactions_sound += 1

                        #Shake1
                        if collectedPresentImage1.collidepoint(event.pos):
                                mouse_x, mouse_y = event.pos
                                #play sound
                                ball.play()
                                sensory_interactions_sound += 1

                        #Shake2
                        if collectedPresentImage2.collidepoint(event.pos):
                                mouse_x, mouse_y = event.pos
                                #play sound
                                bike.play()
                                sensory_interactions_sound += 1

                        #Shake3
                        if collectedPresentImage3.collidepoint(event.pos):
                                mouse_x, mouse_y = event.pos
                                #play sound
                                horn.play()
                                sensory_interactions_sound += 1

                        #Shake4
                        if collectedPresentImage4.collidepoint(event.pos):
                                mouse_x, mouse_y = event.pos
                                #play sound
                                cloth.play()
                                sensory_interactions_sound += 1

                        #Shake5
                        if collectedPresentImage5.collidepoint(event.pos):
                                mouse_x, mouse_y = event.pos
                                #play sound
                                sad.play()
                                sensory_interactions_sound += 1

                        #Shake6
                        if collectedPresentImage6.collidepoint(event.pos):
                                mouse_x, mouse_y = event.pos
                                #play sound
                                coins.play()
                                sensory_interactions_sound += 1

                        #Shake7
                        if collectedPresentImage7.collidepoint(event.pos):
                                mouse_x, mouse_y = event.pos
                                #play sound
                                dog.play()
                                sensory_interactions_sound += 1

                        #Shake8
                        if collectedPresentImage8.collidepoint(event.pos):
                                mouse_x, mouse_y = event.pos
                                #play sound
                                #print ('collectedPresentImage8')
                                rattle.play()
                                sensory_interactions_sound += 1


                        #Shake9
                        if collectedPresentImage9.collidepoint(event.pos):
                                mouse_x, mouse_y = event.pos
                                #play sound
                                train.play()
                                sensory_interactions_sound += 1

                        

                        #Done 
                        if donefab.collidepoint(event.pos):
                                mouse_x, mouse_y = event.pos
                                #Log present collection
                                running = False
                                print('done')

                        
                                
        elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:            
                        hammerfab_dragging = False
                        keyfab_dragging = False
                        wclockfab_dragging = False

                if keyfab.x < 915 and keyfab.x > 875 and keyfab.y < 642 and keyfab.y > 602:
                        chestfab.x = 2000
                        chestfab.y = 2000
                        chest_visible = False
                        # objects_manipulated += 1

                        magic.play()
                        # print ('playing')
                        magic = empty
                        # successful_manipulations += 1

                if hammerfab.x < 625 and hammerfab.x > 496 and hammerfab.y < 717 and hammerfab.y > 542:
                        drumfab.x = 2000
                        drumfab.y = 2000
                        drum_visible = False
                        # objects_manipulated +=1

                        chop.play()
                        # print ('playing')
                        chop = empty
                        # successful_manipulations += 1


                if (wclockfab.x < 725 or wclockfab.x > 846 or wclockfab.y > 105) and overlayOn == False:
                        # drumfab.x = 2000
                        # drumfab.y = 2000
                        clock_unmoved = False
                        # objects_manipulated +=1
                        print ('clock moved')
                        # successful_manipulations += 1

        elif event.type == pygame.MOUSEMOTION:
                if hammerfab_dragging:
                        mouse_x, mouse_y = event.pos
                        hammerfab.x = mouse_x + offset_x
                        hammerfab.y = mouse_y + offset_y  

                if keyfab_dragging:
                        mouse_x, mouse_y = event.pos
                        keyfab.x = mouse_x + offset_x
                        keyfab.y = mouse_y + offset_y  

                if wclockfab_dragging:
                        mouse_x, mouse_y = event.pos
                        wclockfab.x = mouse_x + offset_x
                        wclockfab.y = mouse_y + offset_y 


                  # #SPEECH RECOGNITION SEGMENT -- NOT FOR DEMO
                                # # obtain audio from the microphone
                                # import speech_recognition as sr
                                # r = sr.Recognizer()
                                # with sr.Microphone() as source:
                                #         print("Say something!")
                                #         audio = r.listen(source)

                                # # obtain path to "english.wav" in the same folder as this script
                                
                                # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")
                                # # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
                                # # AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

                                # # use the audio file as the audio source
                                # r = sr.Recognizer()
                                # with sr.AudioFile(AUDIO_FILE) as source:
                                #         audio = r.record(source)  # read the entire audio file
                                #         print(audio)

                                # # recognize speech using Sphinx
                                # try:
                                #         print("Sphinx thinks you said " + r.recognize_sphinx(audio))
                                # except sr.UnknownValueError:
                                #         print("Sphinx could not understand audio")
                                # except sr.RequestError as e:
                                #         print("Sphinx error; {0}".format(e))
                                                 

    # - updates (without draws) -

    # empty

    # - draws (without updates) -

    screen.fill(WHITE)
    screen.blit(bg, (0, 0))

    # pygame.draw.rect(screen, RED, rectangleA)
    # pygame.draw.rect(screen, BLACK, rectangleB)
    screen.blit(img0, presentImage0)
    screen.blit(img1, presentImage1)
    screen.blit(img2, presentImage2)
    screen.blit(shelf, shelffab)
    screen.blit(img3, presentImage3)
    screen.blit(img4, presentImage4)
    screen.blit(img6, presentImage6)
    screen.blit(tree, treefab)
    screen.blit(img5, presentImage5)
    screen.blit(img7, presentImage7)
    screen.blit(img8, presentImage8)
    screen.blit(img9, presentImage9)
    # screen.blit(img10, presentImage10)
    # screen.blit(img11, presentImage11)
    screen.blit(drum, drumfab)
    screen.blit(chest, chestfab)
    screen.blit(wclock, wclockfab)
    screen.blit(hammer, hammerfab)
    screen.blit(key, keyfab)
    screen.blit(done, donefab)
    screen.blit(overlay, overlayfab)
    screen.blit(oguess, overlayguess)
    screen.blit(oskip, overlayskip)
    screen.blit(oguessdone, overlayguessdone)
    screen.blit(img0, collectedPresentImage0)
    screen.blit(img1, collectedPresentImage1)
    screen.blit(img2, collectedPresentImage2)
    screen.blit(img3, collectedPresentImage3)
    screen.blit(img4, collectedPresentImage4)
    screen.blit(img5, collectedPresentImage5)
    screen.blit(img6, collectedPresentImage6)
    screen.blit(img7, collectedPresentImage7)
    screen.blit(img8, collectedPresentImage8)
    screen.blit(img9, collectedPresentImage9)  

    pygame.display.flip()

    # - constant game speed / FPS -

    clock.tick(FPS)

# - end -

# Log parameters 
# Global : 
#     mouse click locations 
#     time stamp of events 

# Event based : 
#     Interacting with novel sensory interactions / sensory experiences such as touch, sight, and sound - deviating from regular : Number of sound interactions 
#     Novel objects interacted with (animated presents, and objects with sound) : Number of animated presents clicked on 
#     Ambiguous objects interacted with : Clock, paper stroll clicks
#     Number of manipulations : Key, axe, tree, present shaking
#     Number of attempts made to answer the guessing puzzle : Number of clicks on Guess
#     Number of questions asked : NA 
#     Number of questions that aided the hypothesis of what’s inside : NA
#     Number of hidden presents found : Easy presents collected, Hidden presents collected, Total presents collected
#     Time spent exploring the game : Time stamps 
#     If the objects were mapped to their correct use : Present behind axe, key collected


from datetime import datetime

f = open('log.txt','a')

#     Interacting with novel sensory interactions / sensory experiences such as touch, sight, and sound - deviating from regular : Number of sound interactions 
f.write('\n' + '[Sensory Interactions : sound] = ' + str(sensory_interactions_sound))

#     Novel objects interacted with (animated presents, and objects with sound) : Number of animated presents clicked on 
#f.write('\n' + '[Novel objects manipulated] = ' + str(animated_objects_manipulated))

#     Ambiguous objects interacted with : Clock, paper stroll clicks
#TODO
f.write('\n' + '[Ambiguous objects manipulated] = ' + str(ambiguous_objects_manipulated))

#     Number of manipulations : Key, axe, tree, present shaking
f.write('\n' + '[Objects manipulated] = ' + str(objects_manipulated))
f.write('\n' + '[Total manipulation actions] = ' + str(number_of_manipulations))

#     Number of attempts made to answer the guessing puzzle : Number of clicks on Guess
f.write('\n' + '[Number of guesses] = ' + str(guesses))

#     Number of questions asked : NA 

#     Number of questions that aided the hypothesis of what’s inside : NA

#     Number of hidden presents found : Easy presents collected, Hidden presents collected, Total presents collected
f.write('\n' + '[Presents collected] = ' + str(i))
#TODO
f.write('\n' + '[Easy presents collected] = ' + str(i - hidden))
f.write('\n' + '[Hidden presents collected] = ' + str(hidden))

#     If the objects were mapped to their correct use : Present behind axe, key collected
# TODO
f.write('\n' + '[Objects mapped to correct use] = ' + str(successful_manipulations))

#     Time spent exploring the game : Time stamps  
f.write('\n' + str(datetime.now()) + ' , session complete')

f.close()

pygame.quit()





















