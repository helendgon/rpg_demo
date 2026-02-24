import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (0,0,255)

    def handle_key(self, key, farm):
        if key == pygame.K_w and self.y > 0:
            self.y -= 1
        if key == pygame.K_s and self.y < farm.rows - 1:
            self.y += 1
        if key == pygame.K_a and self.x > 0:
            self.x -= 1
        if key == pygame.K_d and self.x < farm.cols - 1:
            self.x += 1

    def draw(self, screen, tile_size):
        pygame.draw.rect(screen, self.color,
                         (self.x*tile_size, self.y*tile_size, tile_size, tile_size))