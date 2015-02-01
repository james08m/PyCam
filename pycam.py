__author__ = 'J08M'

from VideoCapture import Device
import pygame
from button import*
from utilities import*

pygame.init()
pygame.mixer.init()

# Create and init window
window = pygame.display.set_mode((1280,720), pygame.RESIZABLE)
play = True

# Sounds
sound = pygame.mixer.Sound('pic.wav')
sound.play()

# Images
IMG_TakePicture = pygame.image.load("takepicture.png")
# Buttons
BTN_TakePicture = Button(( 20,20,55,55 ))
BTN_TakePicture.setIcon(IMG_TakePicture)

# Init webcame device
cam = Device()

while play:
    # Event handling
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        play = False
    if event.type == pygame.MOUSEBUTTONDOWN: # If mouse down
                mouse_position = pygame.mouse.get_pos()
                if BTN_TakePicture.selected(mouse_position):
                    sound.play()
                    title = "pictures/" + getTimeToSecondes() + ".jpg"
                    cam.saveSnapshot(title)

    # Get webcam frame
    #frame = cam.getImage()
    cam.saveSnapshot('image.jpg')
    frame = pygame.image.load("image.jpg").convert()

    # Draw frame and buttons on the window
    window.blit(frame, (0,0))
    BTN_TakePicture.draw(window)

    # Refresh window
    pygame.display.flip()

