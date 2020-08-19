import pygame
import sys
from pygame.locals import *
import random

fps= 32
width= 540
height= 540
screen= pygame.display.set_mode((width, height))
sprites= {}
sounds= {}
player= 'Flappy Bird/mario.png'
background= 'Flappy Bird/background.png'
pipe1= 'Flappy Bird/balloon1.png'
pipe2= 'Flappy Bird/balloon2.png'

def welcomeScreen():
    """
    Showing welcome image on screen
    """ 
    px= int(width/5)
    py= int((height- sprites['player'].get_height())/2)
    mx= int((width- sprites['message'].get_width())/2)
    my= int(height*0.13)
    sounds['intro'].play()
    while True:
        for event in pygame.event.get():
            if event.type== QUIT or (event.type==KEYDOWN and event.key== K_ESCAPE):
                pygame.exit()
                sys.exit()
            elif event.type== KEYDOWN and (event.key== K_SPACE or event.key== K_UP):
                return
            else:
                screen.blit(sprites['background'],(0,0))
                screen.blit(sprites['player'],(px,py))
                screen.blit(sprites['message'],(mx,my))                
                pygame.display.update()
                fpsclock.tick(fps)

def mainGame():
    score=0
    px= int(width/5)
    py= int(height/2)

    newpipe1= getPipe()
    newpipe2= getPipe()

    upperPipes = [
        {'x': width+200, 'y':newPipe1[0]['y']},
        {'x': width+200+(width/2), 'y':newPipe2[0]['y']},
    ]
    lowerPipes = [
        {'x': width+200, 'y':newPipe1[1]['y']},
        {'x': width+200+(width/2), 'y':newPipe2[1]['y']},
    ]
    pipeVelX = -5

    




def getPipe():
    pheight= sprites['pipe'][1].get_height()
    offset= height/4
    y2= offset + random.randrange(0, int(height- 2*offset))
    px= width + 20
    y1= offset + pheight - y2
    pipe= [
        {'x': px, 'y': -y1},
        {'x': px, 'y': y2}
    ]
    return pipe




if __name__ == "__main__":
    pygame.init()
    fpsclock= pygame.time.Clock()
    pygame.display.set_caption('Flappy Mario by Siddharth')
    sprites['message']= pygame.image.load('Flappy Bird/message.png').convert_alpha()
    sprites['pipe']= (pygame.transform.rotate(pygame.image.load(pipe1).convert_alpha(), 180),
        pygame.image.load(pipe2).convert_alpha())
    sprites['background']= pygame.image.load(background).convert()
    sprites['player']= pygame.image.load(player).convert_alpha() 
    sounds['intro']= pygame.mixer.Sound('Sounds/Gadi.wav') 

while True:
    welcomeScreen()
    mainGame()



    
