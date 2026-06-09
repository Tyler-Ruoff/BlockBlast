import pygame

COLS = 8
ROWS = 8
CELL_SIZE = 70 

GRID_COLOR = (255, 255, 255) 
BORDER_COLOR = (200, 200, 200)

board = [[0] * COLS for _ in range(ROWS)]

def draw_board(screen):
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE + 20 
            y = row * CELL_SIZE + 20
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect) 
            pygame.draw.rect(screen, BORDER_COLOR, rect, 2) 
            
def reset_board():
    global board
    board = [[0] * COLS for _ in range(ROWS)] 

def draw_reset_button(screen):
    font = pygame.font.SysFont(None, 36)
    button_rect = pygame.Rect(220, 630, 160, 45) 
    
    pygame.draw.rect(screen, (200, 50, 50), button_rect)     
    pygame.draw.rect(screen, (255, 100, 100), button_rect, 3) 
    
    text = font.render("RESET", True, (255, 255, 255))
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
    
    return button_rect 
