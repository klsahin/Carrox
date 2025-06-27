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


<<<<<<< Updated upstream

class Carrot:
=======
    
class Carrot ():
>>>>>>> Stashed changes
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
        self.visible = True  # Add this line

    def load_image(self):
        self.image = pygame.image.load(self.path).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        
<<<<<<< Updated upstream
        
            
    def shake(self, left, right, screen): #left and right are bool ?
        original_path = self.path
        original_size = self.size
        original_position = self.position

        # hide original carrot ???
        self.visible = False
        # self.load_image()  # Load the carrot image at the new size and position
        # screen.blit(self.image, self.position)  # Draw the carrot at its new position
        # pygame.display.flip()

        self.position = [self.x*0.9 - 20, self.y * 0.8] 
        self.size = [self.width * 2, self.height * 1.2]

        
        #self.visible = True

        print("shaking")
         # Shaking animation (draw directly to screen)
        for i in [1,2,1]:
            if left:
                self.path = f'assets/carrotShakes/carrotL{i}.png'
            elif right:
                self.path = f'assets/carrotShakes/carrotR{i}.png'
            self.load_image()
            screen.blit(self.image, self.position)
            pygame.display.flip()
            pygame.time.wait(200)

        # Restore carrot state
        self.path = original_path
        self.size = original_size
        self.position = original_position
        self.visible = True
        self.load_image()
        
=======

    def shake(self, left, right, screen): #left and right are bool ?
        original_path = self.path
        original_size = self.size
        original_position = self.position
        self.position = [self.x, self.y * 0.8] 
        self.size = [self.width * 1.5, self.height * 1.2]
        print("shaking")
        if left:
            for i in [1,2,1]:
                self.path = f'assets/carrotShakes/carrotL{i}.png'
                self.load_image()
                screen.blit(self.image, self.position)  # Draw the carrot at its position
                pygame.display.flip()  # Update the display to show the new image
                pygame.time.wait(200)
                print(f"Shaking left: {self.path}")  # Debug print
        elif right:
            for i in [1,2,1]:
                self.path = f'assets/carrotShakes/carrotR{i}.png'
                self.load_image()
                screen.blit(self.image, self.position)
                pygame.display.flip()
                pygame.time.wait(200)
                print(f"Shaking right: {self.path}")
        self.path = original_path
        self.size = original_size
        self.position = original_position
        self.load_image()  # Reset to original image after shaking
    
>>>>>>> Stashed changes
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
        self.image = pygame.image.load(self.imagePath).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)

    def update(self, carrot_count):
        if 0 <= carrot_count <= 3:
            self.imagePath = f'assets/{carrot_count}basket.png'
        elif carrot_count > 3:
            self.imagePath = 'assets/nbasket.png'  # Use a fixed image for
        self.load_image()
