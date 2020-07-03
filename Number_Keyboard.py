import os # For hiding pygame message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from sys import exit
from pygame.locals import*

def keyboard(screen_msg):
    pygame.init()
    screen = pygame.display.set_mode((400,600))
    pygame.display.set_caption("Keyboard")
    screen_msg = " " + screen_msg
    number = ""
    
    #--------------------------Colors--------------------------
    Black = (0,0,0)
    Gray1 = (80,80,80)
    Gray2 = (190,190,190)
    Gray3 = (232,232,232)
    White = (255,255,255)
    
    #--------------------------Fonts---------------------------
    buttonFont = pygame.font.SysFont("cambria", 50)
    textFont = pygame.font.SysFont("cambria", 34)
    enterFont = pygame.font.SysFont("cambria", 38)
    
    #--------------------------Buttons-------------------------
    #------1-to-9---------
    for j in range(4):
        for i in range(3):
            pygame.draw.rect(screen,Gray1,(130*i+10,110*j+160,120,100))
            if j < 3:
                buttonText = buttonFont.render(str(j*3+i+1), 1, White)
                screen.blit(buttonText, (130*i+57, 110*j+180))
    
    #------0--------------
    button0 = buttonFont.render("0", 1, White)
    screen.blit(button0, (187, 510))
    
    #------Enter----------
    buttonEnter = enterFont.render("Enter", 1, White)
    screen.blit(buttonEnter, (284, 514))
    
    #------Backspace------
    for i,j,w in [((60,526),(91,526),4), ((60,556),(91,556),4), ((89,526),(89,556),4), ((44,541),(60,527),5), ((44,542),(60,556),5), ((63,532),(80,550),5), ((80,532),(63,550),5)]:
        pygame.draw.line(screen,White,i,j,w)
    
    #--------------------------Main-------------------------
    while True:
        #-----------------Update-screen---------------------
        pygame.draw.rect(screen,Gray3,(10,10,380,140))
        if len(number) == 0:
            text = textFont.render(screen_msg, 0, Gray2)
        else:
            text = textFont.render(number, 0, Black)
        screen.blit(text, (20, 70))
        pygame.display.flip()
        
        for evento in pygame.event.get():
            #---------------------Quit---------------------
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                pygame.quit()
                return None
            
            #-----------------Mouse-actions----------------
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mousePos = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]]
                if mousePos and 10 <= mousePos[0] <= 130 and 490 <= mousePos[1] <= 600:
                    number = number[:-1]
                elif mousePos and 270 <= mousePos[0] <= 370 and 490 <= mousePos[1] <= 600:
                    return number
                elif len(number) <= 17:
                    if 140 <= mousePos[0] <= 260 and 490 <= mousePos[1] <= 600:
                        number += "0"
                    elif 10 <= mousePos[0] <= 370 and 160 <= mousePos[1] <= 480 and (mousePos[0] // 10) % 13 != 0 and ((mousePos[1]-160) // 10) % 11 != 10:
                        number += str((mousePos[0]-10)//130 + ((mousePos[1]-160)//110)*3 + 1)
                        
            #----------------Keyboard-actions--------------
            elif evento.type == pygame.KEYDOWN:
                keyDown = evento.key
                if keyDown == pygame.K_BACKSPACE:
                    number = number[:-1]
                elif keyDown == pygame.K_KP_ENTER or keyDown == pygame.K_RETURN:
                    return number
                elif evento.unicode.isdigit() and len(number) <= 17:
                    number += evento.unicode
       
number = keyboard("Ananas")
if number:
    print(number)
exit(0)