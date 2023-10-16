import pygame
#imports pygame to use its assets
import os
#imports OS specific stuff to be more cross compatable
import random
#hehe
WIDTH, HEIGHT = 500,800
#this is window size
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
#this acts as the window to more easily edit
pygame.display.set_caption("Zombois TTRPG")
#this names the window
MAINBGCOLOUR = 100,100,100
#The color I will use for the background
BUTTONBGCOLOUR = 35,30,30
TEXT_COL = 255,255,255
pygame.font.init()
FONTSIZE = 24
font = pygame.font.SysFont("cascadia-code",FONTSIZE)
MAXFPS = 24
def draw_text (text,font,text_col,x,y):
	img = font.render(text,True,text_col)
	WIN.blit(img,(x,y))
	pygame.display.update()


def draw_window():
#contains things we write to the screen
        WIN.fill((MAINBGCOLOUR))
        text_rect = pygame.Rect((WIDTH*0.2,100),(WIDTH* 0.6 ,100))
        pygame.draw.rect(WIN,(BUTTONBGCOLOUR),text_rect)
        text = "mouse pos" + str(pygame.mouse.get_pos()) 
        draw_text(text,font,(TEXT_COL),WIDTH /2 - len(text)/2 *14,130)


#sets the bg colour of the window
#blit draws an image to the screen, it takes an source image, and cords as input
        pygame.display.update()
#updates the display to add everything that changed

def main():
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(MAXFPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		draw_window()
	pygame.quit()


if __name__ == "__main__":
    main()
