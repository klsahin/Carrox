import pygame

class Background:
    def __init__(self, width, height, image = 'assets/background.png'):
        self.position = [0,0]
        self.size = [width, height]
        self.image = pygame.transform.scale(
            pygame.image.load(image).convert(), (width, height)
        )

class Carrot:
    def __init__(self, x, y, width, height, image): #image = image number!
        self.position = [x, y]
        self.size = [width, height]
        path = ["assets/carrot1.png", "assets/carrot2.png", "assets/carrot3.png"][image]
        self.image = pygame.image.load(path).convert_alpha()  # Load the carrot image

    def shake(self, left, right): #left and right are bool ?
        if left:
            #twist left
            pass
        elif right:
            #twist right
            pass

    def flyToBasket(self):
        #fly to basket
        pass

    def scroll(self):
        #scroll carrots
        pass


class CarrotPit:
    def __init__(self, x, y, width, height, image = 'assets/carrotpit.png'):
        self.position = [x, y]
        self.size = [width, height]
        self.image = pygame.image.load(image).convert_alpha()

    def scroll(self):
        #scroll pits
        pass
