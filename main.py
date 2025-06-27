import pygame
from classes import Carrot, CarrotPit, Background, Basket
import random

pygame.init()

screen = pygame.display.set_mode((1194, 834))

shakeCounter = 0

running = True
mode = 'game'

# Load background
background = Background(1194, 834)  # Uses background1.png by default now
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


def flyToBasket():
    pass

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # mimic carrot movement with space bar
                # Find the last visible carrot
                mainCarrot = next((c for c in reversed(carrots) if c.visible), None)
                if mainCarrot is not None:
                    if shakeCounter >= 4:
                        shakeCounter = 0  # Reset shake counter
                        print("Flying carrot to basket...")
                        carrots_in_basket.append(mainCarrot)
                        basket.update(len(carrots_in_basket))
                        mainCarrot.visible = False
                        flyToBasket()

                        # --- SCROLL LOGIC START (REVERSED) ---
                        scroll_dx = carrot_xs[1] - carrot_xs[0]  # Distance between carrots
                        background.scroll(-scroll_dx)  # Scroll to the right
                        # Move all carrots and pits right by scroll_dx
                        for carrot in carrots:
                            carrot.position[0] += scroll_dx
                        for pit in carrotPits:
                            pit.position[0] += scroll_dx

                        # Remove rightmost carrot only, not the pit
                        carrots.pop(-1)
                        # Remove rightmost pit only if it is off the screen
                        if carrotPits[-1].position[0] > screen.get_width():
                            carrotPits.pop(-1)

                        # Add new random carrot and pit on the left
                        new_x = carrot_xs[0] 
                        new_index = random.randint(0, 2)
                        new_carrot = Carrot(new_x, carrot_y, carrot_width, carrot_height, new_index)
                        new_carrot.load_image()
                        carrots.insert(0, new_carrot)


                        new_pit_x = new_x + (carrot_width - pit_width) // 2
                        new_pit = CarrotPit(new_pit_x, pit_y, pit_width, pit_height)
                        new_pit.load_image()
                        carrotPits.insert(0, new_pit)
                        # --- SCROLL LOGIC END (REVERSED) ---

                    # shaking logic
                    elif shakeCounter < 4 and shakeCounter % 2 == 0:
                        shakeCounter += 1
                        print("Shaking carrot...")
                        mainCarrot.shake(left=True, right=False, screen=screen, background=background, carrotPits=carrotPits, carrots=carrots, basket=basket)  # Shake left
                    elif shakeCounter < 4 and shakeCounter % 2 == 1:
                        shakeCounter += 1
                        print("Shaking carrot...")
                        mainCarrot.shake(left=False, right=True, screen=screen, background=background, carrotPits=carrotPits, carrots=carrots, basket=basket)

    # Draw background first
    background.draw(screen)

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
