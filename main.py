import pygame, sys, random
from pygame.locals import*

fps= 100
screen= pygame.display.set_mode((1700, 1000))
sprites, sounds, b= {}, {}, 0
player, background= 'Flappy Bird/aeroplane.png', 'Flappy Bird/background.jpg'
pipe, base= 'Flappy Bird/tower.jpg', 'Flappy Bird/ground.png'

def create_pipe():
    random_pipe_pos = random.randrange(305, 600)
    bottom_pipe = sprites['pipe'].get_rect(midtop = (1700,random_pipe_pos))
    top_pipe = sprites['pipe'].get_rect(midbottom = (1700,random_pipe_pos - 300))
    return bottom_pipe,top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx-=3
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom>=900:
            screen.blit(sprites['pipe'],pipe)
        else:
            screen.blit((pygame.transform.flip(sprites['pipe'],False,True)), pipe)

def check_collision(pipes):
    for pipe in pipes:
        if pr.colliderect(pipe):
            sounds['out'].play()
            return False
    if pr.top <= -5 or pr.bottom >= 900:
        return False

    return True                    

def welcomeScreen():
    bx=0
    sounds['intro'].play(-1)
    while True:
        for event in pygame.event.get():
            if event.type== QUIT or (event.type==KEYDOWN and event.key== K_ESCAPE):
                pygame.exit()
                sys.exit()
            elif event.type== KEYDOWN and (event.key== K_SPACE or event.key== K_UP):
                return
              
        screen.blit(sprites['background'],(0,0))
        screen.blit(sprites['player'],(0,350))
        screen.blit(sprites['base'],(bx,800))
        screen.blit(sprites['base'],(bx+1700,800))
        bx-=1
        if bx<=-1700:
            bx=0
        pygame.display.update()
        fpsclock.tick(fps)

def mainGame():
    pr= sprites['player'].get_rect(topleft=(0,350))
    pipelist=[]
    SP=pygame.USEREVENT
    pygame.time.set_timer(SP, 1200)
    bx, b, g, score=0, 0, 0.50, 0
    game_active=True

    while True:
        sounds['intro'].stop()
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if (event.key == K_SPACE or event.key == K_UP) and game_active:
                    b=0
                    b-=10
                    sounds['flap'].play()
                if  (event.key == K_SPACE or event.key == K_UP) and game_active == False:
                    pipelist.clear()
                    pr.topleft = (0,350)
                    score = 0 

            if event.type == SP:
                pipelist.extend(create_pipe())
                #print(pipelist)

        screen.blit(sprites['background'],(0,0))

        if game_active:
            # Bird
            b+= g
            pr.centery += b
            screen.blit(sprites['player'],pr)
            game_active = check_collision(pipelist)

            # Pipes
            pipelist = move_pipes(pipelist)
            draw_pipes(pipelist)
            score += 0.01
            # score_display('main_game')
            # score_sound_countdown -= 1
            # if score_sound_countdown <= 0:
            #     score_sound.play()
            #     score_sound_countdown = 100
        # else:
        #     screen.blit(game_over_surface,game_over_rect)
        #     high_score = update_score(score,high_score)
        #     score_display('game_over')

        pipelist= move_pipes(pipelist)
        draw_pipes(pipelist)
        screen.blit(sprites['base'],(bx,800))
        screen.blit(sprites['base'],(bx+1700,800)) 
        bx-=1 
        if bx<=-1700:
            bx=0
        pygame.display.update()
        fpsclock.tick(fps)            
    
if __name__ == "__main__":
    pygame.init()
    fpsclock= pygame.time.Clock()
    pygame.display.set_caption('Flappy Jihad')
    sprites['pipe']= pygame.transform.scale(pygame.image.load(pipe).convert_alpha(), (150,600))
    sprites['background']= pygame.transform.scale(pygame.image.load(background).convert_alpha(), (1700,900))
    sprites['player']= pygame.transform.scale(pygame.image.load(player).convert_alpha(), (300,100))
    sprites['base']=pygame.transform.scale(pygame.image.load(base).convert_alpha(),(1700,112))
    sounds['intro']= pygame.mixer.Sound('Sounds/bomb.wav')
    sounds['out']=pygame.mixer.Sound('Sounds/out.wav')
    sounds['flap']=pygame.mixer.Sound('Sounds/wing.wav')
    pr= sprites['player'].get_rect(topleft=(0,350))

    while True:
        welcomeScreen()
        mainGame()



    
