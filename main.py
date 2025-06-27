import pygame
from classes import *

pygame.init()

screen = pygame.display.set_mode((800, 1400))


shakeCounter = 0

running = True
mode = 'game'
# on start:
# 1. Load background image
# 2. Load basket image
# 3. Create three pit objects
# 4. Create three carrot objects
background = Background(800, 1400)
carrotPit1 = CarrotPit(100, 1200, 100, 100)
carrotPit2 = CarrotPit(350, 1200, 100, 100)
carrotPit3 = CarrotPit(600, 1200, 100, 100)
carrot1 = Carrot(100, 100, 50, 50, 0)
carrot2 = Carrot(200, 100, 50, 50, 1)
carrot3 = Carrot(300, 100, 50, 50, 2)

while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #if mode == 'game':
        
    # if shakeCounter > 5:
    #     carrot.flyToBasket()
    #     shakeCounter = 0
    # elif shakeCounter > 0:
    #     carrot.shake(left=True, right=False) #data for left, right values
    #     shakeCounter += 1

    pygame.display.flip()

pygame.quit()