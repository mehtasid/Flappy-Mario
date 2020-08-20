import random 
import sys 
import pygame
from pygame.locals import * 

FPS = 32
width = 1080
height = 1920
screen = pygame.display.set_mode((width, height))
gy = height * 0.8
sprites = {}
sounds = {}
player = 'sprites/mario.png'
background = 'sprites/background.png'
pipe1 = 'sprites/balloon1.png'
pipe2 = 'sprites/balloon2.png'

def welcomescreen():
    playerx = int(width/5)
    playery = int((height - sprites['player'].get_height())/2)
    messagex = int((width - sprites['message'].get_width())/2)
    messagey = int(height*0.13)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return
            else:
                screen.blit(sprites['background'], (0, 0))    
                screen.blit(sprites['player'], (playerx, playery))    
                screen.blit(sprites['message'], (messagex,messagey ))    
                pygame.display.update()
                FPSCLOCK.tick(FPS)

def mainGame():
    score = 0
    playerx = int(width/5)
    playery = int(width/2)
    newpipe1 = getRandompipe()
    newpipe2 = getRandompipe()
    upperpipes = [
        {'x': width+200, 'y':newpipe1[0]['y']},
        {'x': width+200+(width/2), 'y':newpipe2[0]['y']},
    ]
    lowerpipes = [
        {'x': width+200, 'y':newpipe1[1]['y']},
        {'x': width+200+(width/2), 'y':newpipe2[1]['y']},
    ]

    pipeVelX = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8 
    playerFlapped = False 


    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    sounds['wing'].play()


        crashTest = isCollide(playerx, playery, upperpipes, lowerpipes) 
        if crashTest:
            return     
        playerMidPos = playerx + sprites['player'].get_width()/2
        for pipe in upperpipes:
            pipeMidPos = pipe['x'] + sprites['pipe1'].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos +4:
                score +=1
                print(f"Your score is {score}") 
                sounds['point'].play()


        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False            
        playerHeight = sprites['player'].get_height()
        playery = playery + min(playerVelY, gy - playery - playerHeight)
        for upperpipe , lowerpipe in zip(upperpipes, lowerpipes):
            upperpipe['x'] += pipeVelX
            lowerpipe['x'] += pipeVelX
        if 0<upperpipes[0]['x']<5:
            newpipe = getRandompipe()
            upperpipes.append(newpipe[0])
            lowerpipes.append(newpipe[1])
        if upperpipes[0]['x'] < -sprites['pipe1'].get_width():
            upperpipes.pop(0)
            lowerpipes.pop(0)
        screen.blit(sprites['background'], (0, 0))
        for upperpipe, lowerpipe in zip(upperpipes, lowerpipes):
            screen.blit(sprites['pipe1'], (upperpipe['x'], upperpipe['y']))
            screen.blit(sprites['pipe2'], (lowerpipe['x'], lowerpipe['y']))
        screen.blit(sprites['player'], (playerx, playery))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def isCollide(playerx, playery, upperpipes, lowerpipes):
    if playery> gy - 25  or playery<0:
        sounds['hit'].play()
        return True
    
    for pipe in upperpipes:
        pipeHeight = sprites['pipe1'].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < sprites['pipe1'].get_width()):
            sounds['hit'].play()
            return True

    for pipe in lowerpipes:
        if (playery + sprites['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < sprites['pipe1'].get_width():
            sounds['hit'].play()
            return True

    return False

def getRandompipe():
    pipeHeight = sprites['pipe1'].get_height()
    offset = height/3
    y2 = offset + random.randrange(0, int(height - 1.2 *offset))
    pipeX = width + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},
        {'x': pipeX, 'y': y2} 
    ]
    return pipe

if __name__ == "__main__":
    pygame.init() 
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Mario by Siddharth')
    sprites['message'] =pygame.image.load('sprites/message.png').convert_alpha()
    sprites['pipe'] =(pygame.transform.rotate(pygame.image.load(pipe1).convert_alpha(), 180), 
    pygame.image.load(pipe2).convert_alpha()
    )
    sprites['background'] = pygame.image.load(background).convert()
    sprites['player'] = pygame.image.load(player).convert_alpha()
    sounds['die'] = pygame.mixer.Sound('audio/die.wav')
    sounds['hit'] = pygame.mixer.Sound('audio/hit.wav')
    sounds['point'] = pygame.mixer.Sound('audio/point.wav')
    sounds['swoosh'] = pygame.mixer.Sound('audio/swoosh.wav')
    sounds['wing'] = pygame.mixer.Sound('audio/wing.wav')
    while True:
        welcomescreen() 
        mainGame() 
