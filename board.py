import pygame

COLS = 8
ROWS = 8
CELL_SIZE = 70 

GRID_COLOR = (50, 50, 60) 
BORDER_COLOR = (100, 100, 120) 

board = [[0] * COLS for _ in range(ROWS)]

def draw_board(screen):
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE + 20 
            y = row * CELL_SIZE + 20
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect) 
            pygame.draw.rect(screen, BORDER_COLOR, rect, 2) 
