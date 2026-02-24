import pygame, sys
from player import Player
from farm import Farm

# --- Setup ---
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
TILE_SIZE = 40
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RPG Demo")

# --- Create Player and Farm ---
player = Player(5,5)
farm = Farm(SCREEN_WIDTH//TILE_SIZE, SCREEN_HEIGHT//TILE_SIZE)

clock = pygame.time.Clock()

# --- Main Loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            player.handle_key(event.key, farm)

    # Draw
    screen.fill((200,200,200))
    farm.draw(screen, TILE_SIZE)
    player.draw(screen, TILE_SIZE)
    pygame.display.flip()
    clock.tick(10)