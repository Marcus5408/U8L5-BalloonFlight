import pygame
import random
from bird import Bird
from balloon import Balloon

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.Font("u8l5_balloonflight/frenchFries-Regular.ttf", 48)
subtitle_font = pygame.font.Font("u8l5_balloonflight/frenchFries-Regular.ttf", 24)
pygame.display.set_caption("Balloon Flight!")


# set up variables for the display
size = (800, 600)
screen = pygame.display.set_mode(size)
BIRD_START_X = 800

file_dir = __file__.replace("__init__.py", "")
bg = pygame.image.load(f"{file_dir}background.png")
house = pygame.image.load(f"{file_dir}house.png")
tree = pygame.image.load(f"{file_dir}tree.png")


b = Balloon(300, 200)
bird = Bird(BIRD_START_X, 250)

b.mask = pygame.mask.from_surface(b.image)
bird.mask = pygame.mask.from_surface(bird.image)

INITIAL_HOUSE_X = random.randint(0, 600)
INITIAL_TREE_X = random.randint(0, 600)
house_x = INITIAL_HOUSE_X
tree_x = INITIAL_TREE_X


# render the text for later

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------
clock = pygame.time.Clock()
frame = 0
points = 0
game_over = False
b_move = False
title_screen = True
time_since_up = 0
while run:
    # --- Title Screen
    while title_screen:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                title_screen = False
            elif event.type == pygame.QUIT:
                run = False
                title_screen = False

        screen.blit(bg, (0, 0))
        title = my_font.render("Balloon Flight!", True, (0, 0, 0))
        subtitle = subtitle_font.render("Press any key to start", True, (0, 0, 0))
        screen.blit(title, (size[0] // 2 - title.get_width() // 2, 200))
        screen.blit(subtitle, (size[0] // 2 - subtitle.get_width() // 2, 300))
        pygame.display.update()

    # --- Main event loop
    clock.tick(60)
    if frame % 30 == 0:
        bird.switch_image()
    elif frame % 2 == 0:
        bird.move_bird()
        if bird.x < (0 - bird.image_size[0]):
            bird.x = screen.get_width() + bird.image_size[0]
            points += 1
        house_x -= 2
        if house_x < (0 - house.get_width()):
            house_x = screen.get_width() + house.get_width()
        tree_x -= 5
        if tree_x < (0 - tree.get_width()):
            tree_x = screen.get_width() + tree.get_width()

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                b_move = True
                time_since_up = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                b_move = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            b_move = True
            time_since_up = 0
        if event.type == pygame.MOUSEBUTTONUP:
            b_move = False

    if b_move:
        b.move_balloon("up", size, 1)
    else:
        time_since_up += 1
        b.move_balloon("down", size, time_since_up // 10)

    if b.rect.colliderect(bird.rect):
        offset_x = bird.rect.x - b.rect.x
        offset_y = bird.rect.y - b.rect.y
        game_over = b.mask.overlap(bird.mask, (offset_x, offset_y))

    score_text = subtitle_font.render(f"Score: {points}", True, (0, 0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(house, (house_x, 360))
    screen.blit(tree, (tree_x, 360))
    screen.blit(bird.image, bird.rect)
    screen.blit(b.image, b.rect)
    pygame.display.update()

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                bird.x = BIRD_START_X
                bird.y = 250
                b.x = 300
                b.y = 200
                house_x = INITIAL_HOUSE_X
                tree_x = INITIAL_TREE_X
                points = 0
                game_over = False
            elif event.type == pygame.QUIT:
                run = False
                game_over = False

        screen.blit(bg, (0, 0))
        game_over_text = my_font.render("Game Over!", True, (0, 0, 0))
        score_text = subtitle_font.render(f"Score: {points}", True, (0, 0, 0))
        play_again = subtitle_font.render(
            "Press any key to play again", True, (0, 0, 0)
        )
        screen.blit(
            game_over_text, (size[0] // 2 - game_over_text.get_width() // 2, 200)
        )
        screen.blit(score_text, (size[0] // 2 - score_text.get_width() // 2, 300))
        screen.blit(play_again, (size[0] // 2 - play_again.get_width() // 2, 400))
        pygame.display.update()
    frame += 1

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
