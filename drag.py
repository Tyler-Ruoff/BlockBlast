import pygame
from board import CELL_SIZE, board

dragging = False
dragged_block = None
drag_pos = (0, 0)
drag_origin_index = None

def draw_preview_blocks(screen, blocks):
    start_x = 30
    start_y = 590
    spacing = 190

    for i, block in enumerate(blocks):
        for (row, col) in block.cells:
            x = start_x + i * spacing + col * 40
            y = start_y + row * 40
            rect = pygame.Rect(x, y, 38, 38)
            pygame.draw.rect(screen, block.color, rect)
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)

def handle_drag(event, blocks, screen):
    global dragging, dragged_block, drag_pos, drag_origin_index

    if event.type == pygame.MOUSEBUTTONDOWN:
        mx, my = event.pos
        start_x = 30
        start_y = 590
        spacing = 190

        for i, block in enumerate(blocks):
            for (row, col) in block.cells:
                x = start_x + i * spacing + col * 40
                y = start_y + row * 40
                rect = pygame.Rect(x, y, 38, 38)
                if rect.collidepoint(mx, my):
                    dragging = True
                    dragged_block = block
                    drag_pos = (mx, my)
                    drag_origin_index = i
                    return

    elif event.type == pygame.MOUSEMOTION:
        if dragging:
            drag_pos = event.pos

    elif event.type == pygame.MOUSEBUTTONUP:
        if dragging:
            place_block_on_board(drag_pos)
            dragging = False
            dragged_block = None

def place_block_on_board(pos):
    from board import COLS, ROWS
    mx, my = pos
    col = (mx - 20) // CELL_SIZE
    row = (my - 20) // CELL_SIZE

    if dragged_block is None:
        return False

    for (r, c) in dragged_block.cells:
        if not (0 <= row + r < ROWS and 0 <= col + c < COLS):
            return False
        if board[row + r][col + c] != 0:
            return False

    for (r, c) in dragged_block.cells:
        board[row + r][col + c] = dragged_block.color

    return True

def draw_dragging(screen):
    if dragging and dragged_block:
        mx, my = drag_pos
        for (row, col) in dragged_block.cells:
            x = mx + col * CELL_SIZE
            y = my + row * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE - 2, CELL_SIZE - 2)
            pygame.draw.rect(screen, dragged_block.color, rect)
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)
