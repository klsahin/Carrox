import pygame

class Background:
    def __init__(self, width, height, path='assets/background1.png', path2='assets/background2.png'):
        self.position = [0, 0]
        self.size = [width, height]
        self.imagePath = path
        self.imagePath2 = path2
        self.image = None
        self.image2 = None
        self.x_offset = 0

    def load_image(self):
        self.image = pygame.image.load(self.imagePath).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)
        self.image2 = pygame.image.load(self.imagePath2).convert_alpha()
        self.image2 = pygame.transform.scale(self.image2, self.size)

    def draw(self, screen):
        # Draw two backgrounds side by side for endless effect
        w = self.size[0]
        x = -self.x_offset % w
        screen.blit(self.image, (x, 0))
        screen.blit(self.image2, (x + w, 0))
        # If x > 0, draw the second background before the first
        if x > 0:
            screen.blit(self.image2, (x - w, 0))

    def scroll(self, dx):
        self.x_offset += dx



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
        self.visible = True  # Add this line

    def load_image(self):
        self.image = pygame.image.load(self.path).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)



    def shake(self, left, right, screen, background, carrotPits, carrots, basket):
        original_path = self.path
        original_size = self.size
        original_position = self.position

        # Hide original carrot during shake
        self.visible = False

        self.size = [self.width * 2, self.height * 1.1]  # Reduce size for shake effect
        self.position = [self.x - self.width // 2, self.y - self.height // 10]
        shake_frames = [1, 2, 1]
        for i in shake_frames:
            # Redraw the whole scene
            background.draw(screen)
            for pit in carrotPits:
                screen.blit(pit.image, pit.position)
            for carrot in carrots:
                if carrot.visible:
                    screen.blit(carrot.image, carrot.position)
            screen.blit(basket.image, basket.position)

            # Draw the shake frame in place of the original carrot
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
        self.position = [x+10, y+70]
        self.size = [width*0.9, height*0.9]
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
