import pygame
from board import draw_board, draw_reset_button, reset_board

pygame.init()

screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption("Block Blast")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                reset_board()

    screen.fill((30, 30, 40))
    draw_board(screen)
    button_rect = draw_reset_button(screen) 
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
