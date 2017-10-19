import pygame, time, sys

pygame.init()
pygame.mixer.init()

bloop = pygame.mixer.Sound("bloop_x.wav")
bloop.play()
print ('playing yo')
time.sleep(1)