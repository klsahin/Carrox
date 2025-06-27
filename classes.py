import pygame

class Background:
    def __init__(self, width, height, path = 'assets/background.png'):
        self.position = [0,0]
        self.size = [width, height]
        self.imagePath = path
        self.image = None

    def load_image(self):
        self.image = pygame.image.load(self.imagePath).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)


    
class Carrot:
    def __init__(self, x, y, width, height, index): #image = image number!
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.position = [x, y]
        self.size = [width, height]
        self.index = index
        self.path = f'assets/carrot{self.index+1}.png'
        self.image = None  # Placeholder for the image, to be loaded later

    def load_image(self):
        if self.image is None:
            self.image = pygame.image.load(self.path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        return self.image

    # def shake(self, left, right): #left and right are bool ?
    #     if left:
    #         #twist left
    #         for i in range(10):
    #             rotated = pygame.transform.rotate(self.image, i)  # Example rotation
    #             screen.blit(rotated, self.position)  # Assuming 'screen' is defined globally
    #     elif right:
    #         #twist right
    #         pass
    
    def flyToBasket(self):
        #fly to basket
        pass

    def scroll(self):
        #scroll carrots
        pass
    

class CarrotPit:
    def __init__(self, x, y, width, height, path = 'assets/carrotpit.png'):
        self.position = [x, y]
        self.size = [width, height]
        self.image = None
        self.imagePath = path

    def load_image(self):
        if self.image is None:
            self.image = pygame.image.load(self.imagePath).convert_alpha()
            self.image = pygame.transform.scale(self.image, self.size)
        return self.image
    def scroll(self):
        #scroll pits
        pass
    

class Basket():
    def __init__(self, x, y, width, height, index):
        self.position = [x, y]
        self.size = [width, height]
        self.image = None
        self.index = index
        self.imagePath = f'assets/{index}basket.png'

    def load_image(self):
        if self.image is None:
            self.image = pygame.image.load(self.imagePath).convert_alpha()
            self.image = pygame.transform.scale(self.image, self.size)
        return self.image
