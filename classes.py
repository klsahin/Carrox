import pygame
import math

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
        self.position = [self.x, self.y]
        self.size = [width, height]
        self.index = index
        self.path = f'assets/carrot{self.index+1}.png'
        self.image = None  # Placeholder for the image, to be loaded later
        self.visible = True
        # Unrooting state
        self.unroot_level = 0
        self.max_unroot_level = 3  # Number of shakes to fully unroot (tweak as needed)

    def load_image(self):
        self.image = pygame.image.load(self.path).convert_alpha()
        self.image = pygame.transform.scale(self.image, self.size)



    def shake(self, left, right, screen, background, carrotPits, carrots, basket, carrot_count, carrot_font, carrot_orange, fly_after_shake=False):
        original_path = self.path
        original_size = self.size
        original_position = self.position.copy()

        self.visible = False  # Hide original carrot during shake

        self.size = [self.width * 2, int(self.height * 1.1)]  # Adjusting size for shake effect
        self.position = [self.position[0] - self.width // 2, self.position[1] - self.height // 10]

        # Frame-by-frame shake animation
        if left:
            shake_frames = ["L1", "L2"]
        elif right:
            shake_frames = ["R1", "R2"]
        else:
            shake_frames = []

        unroot_step = 22  # Amount to move up per shake frame (tweak as needed)
        for frame_idx, frame_name in enumerate(shake_frames):
            # Redraw the whole scene
            background.draw(screen)
            count_text = carrot_font.render(str(carrot_count), True, carrot_orange)
            screen.blit(count_text, (40, 30))
            for pit in carrotPits:
                screen.blit(pit.image, pit.position)
            for carrot in carrots:
                if carrot.visible:
                    screen.blit(carrot.image, carrot.position)
            screen.blit(basket.image, basket.position)

            # Move carrot up by unroot_step * frame_idx
            shake_position = [self.position[0], self.position[1] - unroot_step * frame_idx]
            # Load and draw the shake frame
            self.path = f'assets/carrotShakes/carrot{frame_name}.PNG'
            self.load_image()
            screen.blit(self.image, shake_position)
            pygame.display.flip()  # update the display
            pygame.time.wait(220)

        # Restore carrot state, but keep it unrooted (higher y)
        self.path = original_path
        self.size = original_size
        # Only restore x, keep y unrooted
        total_unroot = unroot_step * (len(shake_frames) - 1)
        self.position = [original_position[0], original_position[1] - total_unroot]
        self.visible = True
        self.load_image()

        # Trigger the fly-to-basket animation only if requested
        if fly_after_shake:
            self.flyToBasket(screen, background, carrotPits, carrots, basket, carrot_count, carrot_font, carrot_orange)

    def flyToBasket(self, screen, background, carrotPits, carrots, basket, carrot_count, carrot_font, carrot_orange):
        # Start and end positions
        start_x, start_y = self.position
        end_x = basket.position[0] + basket.size[0] // 2 - self.size[0] // 2
        end_y = basket.position[1] + basket.size[1] // 2 - self.size[1] // 2
        original_size = self.size.copy()

        # --- PHASE 2: Fly in arc and spin into basket (no pull up phase) ---
        arc_frames = 30
        for frame in range(arc_frames):
            t = frame / (arc_frames - 1)
            # Arc path: linear x, arc y
            x = start_x + (end_x - start_x) * t
            arc_height = -80  # how high the arc goes (negative is up)
            y = start_y + (end_y - start_y) * t + arc_height * math.sin(math.pi * t)
            # Spin angle
            angle = -360 * t
            # Rotate the carrot image
            rotated_image = pygame.transform.rotate(self.image, angle)
            rotated_rect = rotated_image.get_rect(center=(x + original_size[0] // 2, y + original_size[1] // 2))
            # Redraw scene
            background.draw(screen)
            count_text = carrot_font.render(str(carrot_count), True, carrot_orange)
            screen.blit(count_text, (40, 30))
            for pit in carrotPits:
                screen.blit(pit.image, pit.position)
            for carrot in carrots:
                if carrot.visible and carrot is not self:
                    screen.blit(carrot.image, carrot.position)
            screen.blit(basket.image, basket.position)
            # Draw the spinning carrot
            screen.blit(rotated_image, rotated_rect.topleft)
            pygame.display.flip()
            pygame.time.wait(20)

        # After animation, hide the carrot
        self.visible = False

    def scroll(self):
        #scroll carrots
        pass

    def unroot_and_maybe_fly(self, left, right, screen, background, carrotPits, carrots, basket, carrot_count, carrot_font, carrot_orange):
        self.unroot_level += 1
        if self.unroot_level >= self.max_unroot_level:
            self.shake(left, right, screen, background, carrotPits, carrots, basket, carrot_count, carrot_font, carrot_orange, fly_after_shake=True)
            self.unroot_level = 0  # Reset for next time
        else:
            self.shake(left, right, screen, background, carrotPits, carrots, basket, carrot_count, carrot_font, carrot_orange, fly_after_shake=False)


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


class Basket:
    def __init__(self, x, y, width, height, index):
        self.position = [x+18, y+65]
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
