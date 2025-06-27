import pygame
from classes import *

pygame.init()

screen = pygame.display.set_mode((1194, 834))

shakeCounter = 0

running = True
mode = 'game'

# Load background
background = Background(1194, 834)

# Adjusted sizes to match the interface
pit_width, pit_height = 150, 100
carrot_width, carrot_height = 60, 100  # Half the original size
basket_width, basket_height = 250, 250

# Calculate positions for 3 evenly spaced carrots
# Screen width = 1194, leave space for basket on right
available_width = 750  # Leave ~450px for basket area
margin = 80  # Left margin
spacing = (available_width - 3 * carrot_width) / 4  # Space between and around carrots

# X positions for 3 carrots (evenly spaced)
carrot_x1 = margin + spacing
carrot_x2 = margin + spacing + carrot_width + spacing
carrot_x3 = margin + spacing + 2 * (carrot_width + spacing)

carrot_xs = [carrot_x1, carrot_x2, carrot_x3]

# Y positions - place carrots lower to match the ground level in image
ground_level = 650  # Adjust based on your background image
pit_y = ground_level - pit_height // 2
carrot_y = ground_level - carrot_height + 20  # Carrots stick into ground slightly

# Pit positions (centered under carrots)
pit_xs = [x + (carrot_width - pit_width) // 2 for x in carrot_xs]

# Create 3 pits and 3 carrots
carrotPits = [CarrotPit(x, pit_y, pit_width, pit_height) for x in pit_xs]
carrots = [Carrot(x, carrot_y, carrot_width, carrot_height, i) for i, x in enumerate(carrot_xs)]

# Basket position (right side, properly spaced)
basket_orig_width, basket_orig_height = 846, 1096  # From file info
basket_target_height = ground_level - 100  # Make basket sit on ground, adjust as needed
basket_scale = basket_target_height / basket_orig_height
basket_target_width = int(basket_orig_width * basket_scale)

basket_img = pygame.image.load('assets/0basket.png').convert_alpha()
basket_img = pygame.transform.scale(basket_img, (basket_target_width, basket_target_height))
basket_x = 1194 - basket_target_width - 40  # 40px right margin
basket_y = ground_level - basket_target_height + 50  # Sit on ground level

print(f"Carrot positions: {carrot_xs}")
print(f"Pit positions: {pit_xs}")
print(f"Basket position: ({basket_x}, {basket_y})")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background first
    screen.blit(background.image, background.position)

    # Draw pits
    for pit in carrotPits:
        screen.blit(pit.image, pit.position)

    # Draw carrots
    for carrot in carrots:
        screen.blit(carrot.image, carrot.position)

    # Draw basket
    screen.blit(basket_img, (basket_x, basket_y))

    pygame.display.flip()

pygame.quit()
