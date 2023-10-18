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
MAXFPS = 13
#sets the maximum fps
layer = 0

something = [False,False,False,False]

def button_event(button_num):
	global layer 
	if button_num == 0:
		layer = 1
	if button_num == 1:
		print("gooboo")
	if button_num == 3:
		layer = 0
		

def button_hitbox (borderX_min,borderY_min,borderX_max,borderY_max,button_num):
	global something
	pos = pygame.mouse.get_pos() 
	if pos[0] > borderX_min and pos[0] < borderX_max and pos[0] != 0:
		if pos[1] > borderY_min and pos[1] < borderY_max:
			#add a hover color to buttons
			pygame.event.get()
			if pygame.mouse.get_pressed(num_buttons=3)[0]:
				something[button_num] = True
				#if pygame.event.get() == pygame.MOUSEBUTTONDOWN:
				
				print(str(button_num))
			elif something[button_num] == True:
				if pygame.mouse.get_pressed(num_buttons=3)[0] == False:
					button_event(button_num)
					something[button_num] = False
		else:
			something[button_num] = False
	else:
		something[button_num] = False
#set something false by default then true on click and then false only 
#on release or moving out of the hitbox, and switching layers
#how to make it controllable per button, in a less stupid way
#check to see if M1 was being held down

def button (text,rect_H,button_num,layer_num):
	global something 
	global layer
			
	if layer == layer_num:
		rect_hight = 50
		text_center = WIDTH /2 - len(text)/2 *14
		rect_L =text_center -15 
		rect_W =WIDTH - text_center*2+30 
		
		text_rect = pygame.Rect(( text_center - 15,rect_H),(rect_W, rect_hight))
		pygame.draw.rect(WIN,(BUTTONBGCOLOUR),text_rect)
		button_hitbox(rect_L,rect_H,rect_W+rect_L,rect_H+rect_hight,button_num)
		draw_text(text,text_center,rect_H+9)
	elif something[button_num] == True:
		something[button_num] = False
			#unstupid this

def draw_text (text,x,y):

	img = font.render(text,True,TEXT_COL)
	WIN.blit(img,(x,y))



def draw_window():
#contains things we write to the screen
        WIN.fill((MAINBGCOLOUR))
        #sets the bg colour of the window
        button("mouse pos" + str(pygame.mouse.get_pos()),120,0,0)
        button(str(min(random.randint(0,10000),random.randint(0,10000))),220,1,0)
        button("menu "+str(random.randint(1,5))+ " the again",120,2,1)
        button("wait, no let me go back",220,3,1)

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
