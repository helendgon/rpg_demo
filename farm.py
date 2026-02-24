import pygame

class Farm:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        # 2D list representing crop spots (0 = empty)
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def draw(self, screen, tile_size):
        for y in range(self.rows):
            for x in range(self.cols):
                rect = pygame.Rect(x*tile_size, y*tile_size, tile_size, tile_size)
                pygame.draw.rect(screen, (100,200,100), rect)  # green for farm tiles
                pygame.draw.rect(screen, (0,0,0), rect, 1)     # black grid lines