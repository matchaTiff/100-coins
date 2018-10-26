
# name: Tiffany
# date: 03/20/17

#____________________________________________________________________________________

import pygame, random, time
from random import randint
from pygame.locals import *
pygame.init()

# Colors_____________________________________________________________________________

black = (0,0,0)
white = (255,255,255)
blue = (21,75,122)

# Window_____________________________________________________________________________

size = width, height = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("100 Coins")
clock = pygame.time.Clock()

#____________________________________________________________________________________

atArcade = False
atAracadeNot = False
atHome = False
atOutside = False
atRoom = False

#____________________________________________________________________________________

def startMenu():
    start = True
    while start:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    start = False
        
        screen.fill(white)
        font = pygame.font.SysFont("OCR A Extended", 30)
        text = font.render("Start(c)", True, black)
        rect = text.get_rect(center = (width/2, height/2))
        screen.blit(text, rect)
        pygame.display.update()

#____________________________________________________________________________________

def coinCount(count):
    font = pygame.font.SysFont("kroeger 05_55 caps", 25)
    text = font.render("Coins: " + str(count), True, black)
    screen.blit(text, (15, 15))

#____________________________________________________________________________________

def intro0(msg, color):
    def introDialogue():
        global s
        s = pygame.Surface((480,410))
        s.set_alpha(200)
        s.fill((255,255,255))
        screen.blit(s, (10, 55))
        
    introDialogue()
    introFont = pygame.font.SysFont("OCR A Extended", 20)
    screenText = introFont.render(msg, True, color)
    text_rect = screenText.get_rect(center = (width/2, 100))
    screen.blit(screenText, text_rect)

def intro1(msg, color):
    introFont = pygame.font.SysFont("OCR A Extended", 20)
    screenText = introFont.render(msg, True, color)
    text_rect = screenText.get_rect(center = (width/2, 150))
    screen.blit(screenText, text_rect)

def intro2(msg, color):
    introFont = pygame.font.SysFont("OCR A Extended", 20)
    screenText = introFont.render(msg, True, color)
    text_rect = screenText.get_rect(center = (width/2, 200))
    screen.blit(screenText, text_rect)

def intro3(msg, color):
    introFont = pygame.font.SysFont("OCR A Extended", 20)
    screenText = introFont.render(msg, True, color)
    text_rect = screenText.get_rect(center = (width/2, 250))
    screen.blit(screenText, text_rect)

def intro4(msg, color):
    introFont = pygame.font.SysFont("OCR A Extended", 20)
    screenText = introFont.render(msg, True, color)
    text_rect = screenText.get_rect(center = (width/2, 300))
    screen.blit(screenText, text_rect)

def intro5(msg1, msg2, msg3, color):
    introFont = pygame.font.SysFont("OCR A Extended", 20)
    screenText1 = introFont.render(msg1, True, color)
    screenText2 = introFont.render(msg2, True, color)
    screenText3 = introFont.render(msg3, True, color)
    text_rect1 = screenText1.get_rect(center = (width/2, 350))
    text_rect2 = screenText2.get_rect(center = (width/2, 390))
    text_rect3 = screenText3.get_rect(center = (width/2, 430))
    screen.blit(screenText1, text_rect1)
    screen.blit(screenText2, text_rect2)
    screen.blit(screenText3, text_rect3)

def displayIntro():
    background = pygame.image.load("7.jpg").convert()
    background = pygame.transform.scale(background, size)
    screen.blit(background, (0, 0))
    
    intro0("You go to an arcade.", black)
    intro1("You dig into your pockets,", black)
    intro2("only to find out you have no coins!", black)
    intro3("Your mission is to find coins.", black)
    intro4("Where will you go first?", black)
    intro5("Home (h)", "Outside (s)", "Arcade (a)", blue)

#____________________________________________________________________________________

def dialogueBox():
    global s
    s = pygame.Surface((480,100))
    s.set_alpha(200)
    s.fill((255,255,255))
    screen.blit(s, (10, 385))


def displayText(msg, color):
    dialogueBox()

    introFont = pygame.font.SysFont("OCR A Extended", 20)
    screenText = introFont.render(msg, True, color)
    text_rect = screenText.get_rect(center = (width/2, height*0.875))
    screen.blit(screenText, text_rect)
    

def options(choice1, choice2, color):
    s = pygame.Surface((480,150))
    s.set_alpha(200)
    s.fill((255,255,255))
    screen.blit(s, (10, 160))
    
    optionsFont = pygame.font.SysFont("OCR A Extended", 20)
    choice1 = optionsFont.render(choice1, True, color)
    choice2 = optionsFont.render(choice2, True, color)
    text_rect1 = choice1.get_rect(center = (width/2, height*0.55))
    text_rect2 = choice2.get_rect(center = (width/2, height*0.4))
    screen.blit(choice1, text_rect1)
    screen.blit(choice2, text_rect2)

#____________________________________________________________________________________

def toHome():
    global homeBackground
    homeBackground = pygame.image.load("home.jpg").convert()
    homeBackground = pygame.transform.scale(homeBackground, size)
    screen.blit(homeBackground, (0, 0))
    nextTextHome()


def nextTextHome():
    global atHome
    atHome = True

    displayText("You ask your mom for coins (h)", black)
    pygame.display.update()

    if atHome == True:
        start = True
        while start:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        start = False
                        screen.blit(homeBackground, (0, 0))
                        displayText("She said no.", black)
                        
                        options("> Look in room (r)", "> Go outside (s)", blue)

#____________________________________________________________________________________

def toOutside():
    global oBackground
    oBackground = pygame.image.load("outside.png").convert()
    oBackground = pygame.transform.scale(oBackground, size)
    screen.blit(oBackground, (0, 0))
    nextTextOutside()

def nextTextOutside():
    global atOutside
    atOutside = True

    displayText("An old-man approaches you, (s)", black)
    pygame.display.update()
    
    if atOutside == True:
        start = True
        while start:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        start = False
                        screen.blit(oBackground, (0, 0))
                        displayText("You thank him for the coins.", black)
                        
                        options("> Go to arcade (a)", "> Go home (h)", blue)

#____________________________________________________________________________________

def toArcade():
    global arcadeBackground
    arcadeBackground = pygame.image.load("arcade.jpg").convert()
    arcadeBackground = pygame.transform.scale(arcadeBackground, size)
    screen.blit(arcadeBackground, (0, 0))
    
    global atArcade
    atArcade = True

    displayText("You have enough coins to play! (a)" , black)
    pygame.display.update()
    
    if atArcade == True:
        start = True
        while start:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        start = False
                        screen.blit(arcadeBackground, (0, 0))
                        displayText("What will you do?", black)
                        
                        options("> Keep playing (h, s, r)" , "> End Game (e)", blue)
                            

                        
def notEnough():
    global arcadeBackground
    arcadeBackground = pygame.image.load("arcade.jpg").convert()
    arcadeBackground = pygame.transform.scale(arcadeBackground, size)
    screen.blit(arcadeBackground, (0, 0))
    
    atArcadeNot = True

    displayText("You don't have enough coins" , black)
    pygame.display.update()
    
    if atArcadeNot == True:
        start = True
        while start:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        start = False
                        screen.blit(arcadeBackground, (0, 0))
                        displayText("What will you do?", black)
                        
                        options("> Go outsite (s)", "> Go home (h)", blue)

#____________________________________________________________________________________

def randomItems():
    global random
    random = randint(1,7)
    
    if random == 1:
        displayText("You found 20 coins!", black)
    if random == 2:
        displayText("You found a sock", black)
    if random == 3:
        displayText("You found 2 coins!", black)
    if random == 4:
        displayText("You found a pizzabox?", black)
    if random == 5:
        displayText("You found 10 coins!", black)
    if random == 6:
        displayText("You found 15 coins!", black)
    if random == 7:
        displayText("You found a pair of glasses", black)

def toRoom():
    global roomBackground
    roomBackground = pygame.image.load("room.png").convert()
    roomBackground = pygame.transform.scale(roomBackground, size)
    screen.blit(roomBackground, (0, 0))
    nextTextRoom()

def nextTextRoom():
    global atRoom
    atRoom = True

    displayText("You look through your room, (r)", black)
    pygame.display.update()
    
    if atRoom == True:
        start = True
        while start:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        start = False
                        screen.blit(roomBackground, (0, 0))

                        randomItems()
                                    
                        options("> Look through your room again (r)", "> Go home (h)", blue)

#____________________________________________________________________________________

def theEnd():
    endBackground = pygame.image.load("theend.png").convert()
    endBackground = pygame.transform.scale(endBackground, size)
    screen.blit(endBackground, (0, 0))
    font = pygame.font.SysFont("OCR A Extended", 30)
    text = font.render("The End", True, white)
    rect = text.get_rect(center = (width/2, height/2))
    screen.blit(text, rect)
    pygame.display.update()
    
    if atArcade == True:
        start = True
        while start:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

# Main Program Loop__________________________________________________________________

def main():

    pygame.mixer.music.load("aprilshowers.wav")
    pygame.mixer.music.play(-1)
    coins = 0
    amount = 0
    amount2 = 0
    
    done = False
    
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                toHome()
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                toOutside()
                amount += 1
                
                if atOutside == True and amount == 1:
                    coins += 25
                    
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                if coins >= 100:
                    toArcade()

                else:
                    notEnough()
                    
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e and atArcade == True:
                theEnd()
                
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                toRoom()
                
                if atRoom == True:
                    if random == 1:
                        coins += 20
                    elif random == 3:
                        coins += 2
                    elif random == 5:
                        coins += 10
                    elif random == 6:
                        coins += 15
                
            coinCount(coins)
            pygame.display.update()
        clock.tick(60)

#____________________________________________________________________________________

startMenu()
displayIntro()
main()
theEnd()
pygame.quit()
quit()
