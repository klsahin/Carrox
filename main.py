import pygame
from classes import Carrot, CarrotPit, Background, Basket

pygame.init()

screen = pygame.display.set_mode((1194, 834))

shakeCounter = 0

running = True
mode = 'game'

# Load background
background = Background(1194, 834)
background.load_image()  # Load background image

# Adjusted sizes to match the interface
pit_width, pit_height = 150, 400
carrot_width, carrot_height = 170, 400
basket_width, basket_height = 250, 650

# Calculate positions for 3 evenly spaced carrots
# Screen width = 1194, leave space for basket on right
available_width = 700  # Leave ~450px for basket area
margin = 60  # Left margin
spacing = (available_width - 3 * carrot_width) / 4  # Space between and around carrots

# X positions for 3 carrots (evenly spaced)
carrot_x1 = margin + spacing
carrot_x2 = margin + spacing + carrot_width + spacing
carrot_x3 = margin + spacing + 2 * (carrot_width + spacing)

carrot_xs = [carrot_x1, carrot_x2, carrot_x3]

# Y positions - place carrots lower to match the ground level in image
ground_level = 650  # Adjust based on your background image
pit_y = ground_level - pit_height*0.75 - 20
carrot_y = ground_level - carrot_height*0.75 -25 # Carrots stick into ground slightly

# Pit positions (centered under carrots)
pit_xs = [x + (carrot_width - pit_width) // 2 for x in carrot_xs]

# Create 3 pits and 3 carrots
carrotPits = []
for x in pit_xs:
    carrotPit = CarrotPit(x, pit_y, pit_width, pit_height)
    carrotPit.load_image()
    carrotPits.append(carrotPit)

carrots = []
for i, x in enumerate(carrot_xs):
    carrot = Carrot(x, carrot_y, carrot_width, carrot_height, i)
    carrot.load_image()  # Load carrot image
    carrots.append(carrot)


# Basket position (right side, properly spaced)

basket_orig_width, basket_orig_height = 846, 1096  # From file info
basket_target_height = ground_level - 100  #550 # Make basket sit on ground, adjust as needed
basket_scale = basket_target_height / basket_orig_height
basket_target_width = int(basket_orig_width * basket_scale) #423

basket_x = 1194 - basket_target_width - 40  # 722 40px right margin
basket_y = ground_level - basket_target_height - 100  # Sit on ground level

carrots_in_basket = []

basket = Basket(basket_x, basket_y, basket_target_width, basket_target_height, 0)
basket.load_image()  # Load basket image

# Load Super Bubble font for carrot count display
font_path = 'assets/Super Bubble.ttf'
carrot_font = pygame.font.Font(font_path, 64)  # Adjust size as needed
carrot_orange = (255, 140, 0)

print(f"Carrot positions: {carrot_xs}")
print(f"Pit positions: {pit_xs}")
print(f"Basket position: ({basket.position})")

# def shake(carrot, left, right):
#     if left:
#         for i in range(10):
#             rotated = pygame.transform.rotate(carrot.image, -i)  # incrementing left
#             screen.blit(rotated, carrot.position)  
#             pygame.display.flip()  # Update the display while shaking 
#     elif right:
#         for i in range(10):
#             rotated = pygame.transform.rotate(carrot.image, i)  # incrementing right
#             screen.blit(rotated, carrot.position) 
#             pygame.display.flip()  # Update the display while shaking 

def flyToBasket():
    pass

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # mimic carrot movement with space bar
                # Handle space key press
                mainCarrot = carrots[-1]
                if shakeCounter >= 4:
                    shakeCounter = 0  # Reset shake counter
                    # Move the carrot to the basket
                    print("Flying carrot to basket...")
                      
                    carrots_in_basket.append(mainCarrot)
                    basket.update(len(carrots_in_basket))  # Update basket with new carrot count
                    flyToBasket()
<<<<<<< Updated upstream
                    
                elif shakeCounter < 4 and shakeCounter % 2 == 0:
                    shakeCounter += 1
                    print("Shaking carrot...")
                    mainCarrot.visible = False  # Hide the carrot
                    mainCarrot.shake(left=True, right=False, screen=screen)  # Example shake left
                    mainCarrot.visible = True  # Show the carrot again after shaking
                elif shakeCounter < 4 and shakeCounter % 2 == 1:
                    shakeCounter += 1
                    print("Shaking carrot...")
                    mainCarrot.shake(left=False, right=True, screen=screen)

=======

                elif shakeCounter < 4 and shakeCounter % 2 == 0:
                    shakeCounter += 1
                    print("Shaking carrot...")
                    mainCarrot.shake(left=True, right=False, screen=screen)  # Example shake left
                elif shakeCounter < 4 and shakeCounter % 2 == 1:
                    shakeCounter += 1
                    print("Shaking carrot...")
                    mainCarrot.shake(left=False, right=True, screen=screen)  
>>>>>>> Stashed changes

    # Draw background first
    screen.blit(background.image, background.position)

    # Draw carrot count at top left
    carrot_count = len(carrots_in_basket)
    count_text = carrot_font.render(str(carrot_count), True, carrot_orange)
    screen.blit(count_text, (40, 30))

    # Draw pits
    for pit in carrotPits:
        screen.blit(pit.image, pit.position)

    # Draw carrots
    for carrot in carrots:
        if carrot.visible:
            screen.blit(carrot.image, carrot.position)

    # Draw basket
    screen.blit(basket.image, basket.position)

    pygame.display.flip()



pygame.quit()
