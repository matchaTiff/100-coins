# name: Tiffany
# date: 03/20/17


import pygame, time, script
from pygame.locals import *
pygame.init()


# Colors
black = (0,0,0)
white = (255,255,255)
grey = (128, 128, 128)
aqua = (108,197,200)

size = width, height = (1000, 563)


game_font = pygame.font.SysFont("OCR A Extended", 20)

homeBackground = pygame.image.load("1.jpg")
homeBackground = pygame.transform.scale(homeBackground, size)
streetBackground = pygame.image.load("3.jpg")
streetBackground = pygame.transform.scale(streetBackground, size)
vmBackground = pygame.image.load("5.jpg")
vmBackground = pygame.transform.scale(vmBackground, size)
    

# Window
pygame.display.set_caption("A Vending Machine")


clock = pygame.time.Clock()


game_script = 1
game_running = True

screen = pygame.display.set_mode(size)

def toHome():
    homeBackground = pygame.image.load("1.jpg").convert()
    homeBackground = pygame.transform.scale(homeBackground, size)
    #screen.blit(homeBackground, (0, 0))


def toStreets():
    streetBackground = pygame.image.load("3.jpg").convert()
    streetBackground = pygame.transform.scale(streetBackground, size)
    #screen.blit(streetBackground, (0, 0))
    

def toVM():
    vmBackground = pygame.image.load("5.jpg").convert()
    vmBackground = pygame.transform.scale(vmBackground, size)
    #screen.blit(vmBackground, (0, 0))

    
location = {'home' : homeBackground, 'streets' : streetBackground,
            'vending machine' : vmBackground}


def startMenu():
    
    screen.fill(white)
    font = pygame.font.SysFont("OCR A Extended", 30)
    text = font.render("Start", True, black)
    rect = text.get_rect(center = (width/2, height/2))
    b = screen.blit(text, rect)
    pygame.display.update()
    
    start = True
    while start:
        pygame.event.get()
        click_pos = pygame.mouse.get_pos()
        if (pygame.mouse.get_pressed())[0] == 1 and 410 < click_pos[0] < 590 and 310 < click_pos[1] < 365:
            start_game()
            

def start_game():
    global game_script, location
    turn = 0
    game_state = 1

    while game_state == 1:
        line = getattr(script, ('scene' + str(game_script)))(turn)
        pygame.event.get()
        click_state = pygame.mouse.get_pressed()
        if turn == 0:
            scene_start = 0
            for i in range (4):
                if scene_start == 0:
                    screen.blit(location[line[0]], [0, 0])
                elif scene_start == 1:
                    time.sleep(1)
                elif scene_start == 2:
                    time.sleep(1)
                    pygame.draw.rect(screen, (grey), pygame.Rect(130, 423, 740, 120))
                elif scene_start == 3:
                    time.sleep(1)
                    screen.blit(game_font.render(line[1], 1, white), (135, 430))
                    turn += 1
                    clicked = 0
                
                scene_start += 1
                pygame.display.flip()
                
        elif turn > 0 and click_state[0] == 1:
            line_start = 0
            for i in range (4):
                if line_start == 0 and line[0] != '0':
                    print(line[0])
                    screen.blit(location[line[0]], [0, 0])
                    time.sleep(1)
                elif line_start == 1 and line[1] != '0':
                    time.sleep(1)
                elif line_start == 2:
                    pygame.draw.rect(screen, (grey), pygame.Rect(130, 423, 740, 120))
                elif line_start == 3:
                    screen.blit(game_font.render(line[2], 1, white), (135, 430))
                    turn += 1
                    if  line[3] != '0':
                        game_script = line[3]
                        time.sleep(0.5)
                    game_state = line[4]
                    clicked = 0
                
                line_start += 1
                pygame.display.flip()
    

def game():
    global game_running
    while game_running == True:
        startMenu()

game()
