#what am i trying to do?
#a basic GUI that contains buttons on a menu that show different info,
#rolls stats for a character and stores it in a way that it can be 
#easily sent as a character file, optionally id also like to have all 
#the actions you can take by default as buttons to preform, with 
#any bonuses as easy add ons to the roll
#and then even more optionally have the outcome print out to whatever 
#VTT were using
#
#style note, try not to go much further than 3 deep 
#outside of simple if>then "check" statements 
#such as if x > y and < z ... etc
#
import pygame
#imports pygame to use its assets
import os
#imports OS specific stuff to be more cross compatable
import random
#hehe
WIDTH, HEIGHT = 500,700
#this is window size
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#this acts as the window to more easily edit
pygame.display.set_caption("Zombois TTRPG")
#this names the window
MAINBGCOLOUR = 37,35,35
#The color I will use for the background
BUTTONBGCOLOUR = 33,30,30
TEXT_COL = 255,255,255
pygame.font.init()
FONTSIZE = 24
#sets the fontsize for normal use
font = pygame.font.SysFont("cascadia-code",FONTSIZE)
#sets the font for normal use
MAXFPS = 15
#sets the maximum fps



def button_hitbox (borderX_min,borderY_min,borderX_max,borderY_max,button_num):
	pos = pygame.mouse.get_pos() 
	if pos[0] > borderX_min and pos[0] < borderX_max and pos[0] != 0:
		if pos[1] > borderY_min and pos[1] < borderY_max:
			pygame.event.get()
			if pygame.mouse.get_pressed(num_buttons=3)[0]:
				print("print "+str(button_num))
#figure out how to seperate one button from annother,
#in a less stupid way, with a check to see if M1 was being held down

def button (text,rect_H,button_num,layer):
        rect_hight = 50
        text_center = WIDTH /2 - len(text)/2 *14
        rect_L =text_center -15 
        rect_W =WIDTH - text_center*2+30 
        
        text_rect = pygame.Rect(( text_center - 15,rect_H),(rect_W, rect_hight))
        pygame.draw.rect(WIN,(BUTTONBGCOLOUR),text_rect)
        button_hitbox(rect_L,rect_H,rect_W+rect_L,rect_H+rect_hight,button_num)
        draw_text(text,text_center,rect_H+9)
        #unstupid this
        
		

def draw_text (text,x,y):

	img = font.render(text,True,TEXT_COL)
	WIN.blit(img,(x,y))



def draw_window():
#contains things we write to the screen
        WIN.fill((MAINBGCOLOUR))
        #sets the bg colour of the window
        button("mouse pos" + str(pygame.mouse.get_pos()),120,0,0)
        button(str(random.randint(0,10000)),220,1,0)
        # ~ rect_2_L =WIDTH*0.1
        # ~ rect_2_W = WIDTH* 0.8
        # ~ rect_2_H = 220
        # ~ button(rect_2_L,rect_2_H,rect_2_W+rect_2_L,rect_2_H+rect_hight,2)
        # ~ rect = pygame.Rect((rect_2_L,rect_2_H),(rect_2_W ,rect_hight))
        # ~ pygame.draw.rect(WIN,(BUTTONBGCOLOUR),rect)
        # ~ draw_text(text_1,font,(TEXT_COL),text_1_center,130)


#this is no longer used but is still here
#so that i dont have to refrence the docs
#blit draws an image to the screen, 
#it takes an source image and cords as input
        


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
