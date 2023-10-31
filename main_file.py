#what am i trying to do?
#a basic GUI that contains buttons on a menu that show different info,
#rolls stats for a character and stores it in a way that it can be 
#easily sent as a human readable character file, optionally 
#id also like to have all the actions you can take by default 
#as buttons to preform, with any bonuses as easy add ons to the roll
#and then even more optionally have the outcome print out to whatever 
#VTT were using
#
#note, i should figure out how to package this and to use inno or
#something similar to automatically manage installation, instead of 
#having to manually install pygame, maybe just a powershell/bash
#script, dont know yet
#
import pygame
#imports pygame to use its assets
import os
#imports OS specific stuff to be more cross compatable
import random
#hehe
WIDTH, HEIGHT = 400,600
#this is window size
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#this acts as the window to more easily edit
pygame.display.set_caption("Zombois TTRPG helper")
#this names the window
MAINBGCOLOUR = 37,35,35
#The color I will use for the background
BUTTONBGCOLOUR = 33,30,30
BUTTONHOVERCOLOUR = 23,20,20
BUTTONCLICKCOLOUR = 43,40,40
TEXT_COL = 255,255,255
pygame.font.init()
FONTSIZE = 24
#sets the fontsize for normal use
font = pygame.font.SysFont("cascadia-code",FONTSIZE)
#sets the font for normal use
MAXFPS = 13
#sets the maximum fps
layer = 0
something = []
for x in range(1,255):
        something.append(False)
#figure out something much less stupid, this fucking sucks,
#and is heavily limited
def textbox(text,color,height,padding,layer_num):
        if layer == layer_num:
                x=0
                garbageVal = WIDTH/2
                vcenter = garbageVal - len(text[0]) * 14 
                youtube = pygame.Rect((WIDTH /2 - len(text[0])*7-padding   ,height-padding),(len(text[0])*14+padding+padding ,len(text)*24+padding*2))
                pygame.draw.rect(WIN,((color)),youtube)
                for line in text:
                        height_pos = x * 25 + height
                        draw_text(text[x], garbageVal - len(text[0]) *7,height_pos)
                        x += 1
#this is probably the best its getting with how abstract all the math makes this
#and im not making it into an object, for my sanity
def button_event(button_num):
        global layer 
        global WIDTH,HEIGHT
        if button_num == 8:
                layer = 1
                WIDTH,HEIGHT =400,600
                WIN = pygame.display.set_mode((WIDTH,HEIGHT))
        elif button_num == 1:
                print("gooboo")
        elif button_num == 3:
                layer = 0
        elif button_num == 4:
                pygame.quit()
        elif button_num == 5:
                layer = 2
                WIDTH,HEIGHT=600,600
                WIN = pygame.display.set_mode((WIDTH,HEIGHT))
        elif button_num == 6:
                layer = 3
        elif button_num == 7:
                layer = 4
        else:
                print("attach a function to button #"+str(button_num))
def button_hitbox (borderX_min,borderY_min,borderX_max,borderY_max,button_num):
        global something
        pos = pygame.mouse.get_pos() 
        if pos[0] > borderX_min and pos[0] < borderX_max and pos[0] != 0:
                if pos[1] > borderY_min and pos[1] < borderY_max:
                        #add a hover color to buttons
                        pygame.event.get()
                        if pygame.mouse.get_pressed(num_buttons=3)[0]:
                                something[button_num] = True
                        elif something[button_num] == True:
                                if pygame.mouse.get_pressed(num_buttons=3)[0] == False:
                                        button_event(button_num)
                                        something[button_num] = False
                else:
                        something[button_num] = False
        else:
                something[button_num] = False
#how to make it controllable per button, in a less stupid way
#check to see if M1 was being held down before going in the box, somehow
#that doesnt just add more layers to check, if possible
def button (text,rect_H,button_num,layer_num):
        global something 
        # ~ global layer
        rect_hight = 50
        text_center = WIDTH /2 - len(text)/2 *14
        rect_L =text_center -15 
        rect_W =WIDTH - text_center*2+30 
        text_rect = pygame.Rect(( text_center - 15,rect_H),(rect_W, rect_hight))
        pygame.draw.rect(WIN,(BUTTONBGCOLOUR),text_rect)
        button_hitbox(rect_L,rect_H,rect_W+rect_L,rect_H+rect_hight,button_num)
        draw_text(text,text_center,rect_H+9)
        if something[button_num] == True and layer != layer_num:
                something[button_num] = False
#unstupid this
def draw_text (text,x,y):
        img = font.render(text,True,TEXT_COL)
        WIN.blit(img,(x,y))
#blit draws an image to the screen, 
#it takes an source image and cords as input
def draw_window():
#contains things we write to the screen
        WIN.fill(MAINBGCOLOUR)
        if layer == 0:
                textbox(["Zomboi's TTRPG"],(80,80,80),50,10,0)
                button("Learn The Rules",120,8,0)
                button("Create a Character Sheet",220,1,0) 
                button("exit",520,4,0)
        elif layer == 1:
                textbox(["Rules"],(80,80,80),50,10,1)
                button("Basic Rules",120,5,1)
                button("Major Stats",200,6,1)
                button("Minor Stats",280,7,1)
                button("back",520,3,1)
        elif layer == 2:
                textbox(["rules -> basic rules"],(80,80,80),50,10,2)
                button("back",520,8,2)
                textbox([
                "This system emphisizes lots of ways to  ",
                "do things mechanically in the hope that ",
                "every build feels unique, even with the ",
                "same class, race, etc.",
                "",
                "however, that means theres alot to learn",
                "this will be the intro to some baseline ",
                "rules, which i will go into more depth  ",
                "with the specific rules. ",
                "",
                "how can i use this in a VTT scenario?[1]",
                "how do class/race/roll bonuses work? [2]",
                "what you can do in a turn?           [3]",
                ""],
                (20,20,20),100,10,2) 
        elif layer == 3:
                textbox(["rules -> Major Stats"],(80,80,80),50,10,3)
                button("back",520,8,3)
        elif layer == 4:
                textbox(["rules -> Minor Stats"],(80,80,80),50,10,4)
                button("back",520,8,4)
#text wall style button option, no click functionality, 
#just text and bg + padding, maybe scroll?
def main():
        clock = pygame.time.Clock()
        run = True
        while run:
                clock.tick(MAXFPS)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False
                draw_window()
                pygame.display.update()

            #updates the display to add everything that changed
        pygame.quit()


if __name__ == "__main__":
        main()
