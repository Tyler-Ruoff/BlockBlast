import pygame
import board as board_module
from board import draw_board, reset_board
from block import spawn_blocks, random_block
from check import check_and_clear
from score import add_score, reset_score, draw_score, draw_win_screen, is_goal_reached

pygame.init()

WIDTH, HEIGHT = 600, 820
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Blast")
clock = pygame.time.Clock()

GRID_X = 20
GRID_Y = 20
CELL_SIZE = 70
PIECE_CELL = 42

RESET_RECT = pygame.Rect(130, 775, 100, 35)
UNDO_RECT = pygame.Rect(10, 775, 100, 35)

tray_positions = [
    (70, 610),
    (260, 610),
    (450, 610)
]

blocks = spawn_blocks()
block_positions = tray_positions.copy()
undo_stack = []

dragging_index = None
drag_offset = (0, 0)


def draw_placed_blocks():
    for row in range(board_module.ROWS):
        for col in range(board_module.COLS):
            color = board_module.board[row][col]
            if color:
                rect = pygame.Rect(
                    GRID_X + col * CELL_SIZE + 2,
                    GRID_Y + row * CELL_SIZE + 2,
                    CELL_SIZE - 4,
                    CELL_SIZE - 4
                )
                pygame.draw.rect(screen, color, rect)


def draw_piece(block, pos):
    x, y = pos
    for row, col in block.cells:
        rect = pygame.Rect(
            x + col * PIECE_CELL,
            y + row * PIECE_CELL,
            PIECE_CELL,
            PIECE_CELL
        )
        pygame.draw.rect(screen, block.color, rect)
        pygame.draw.rect(screen, (40, 40, 50), rect, 2)


def get_piece_rect(block, pos):
    rows = [cell[0] for cell in block.cells]
    cols = [cell[1] for cell in block.cells]
    width = (max(cols) + 1) * PIECE_CELL
    height = (max(rows) + 1) * PIECE_CELL
    return pygame.Rect(pos[0], pos[1], width, height).inflate(30, 30)


def can_place(block, grid_row, grid_col):
    for row, col in block.cells:
        new_row = grid_row + row
        new_col = grid_col + col
        if new_row < 0 or new_row >= board_module.ROWS:
            return False
        if new_col < 0 or new_col >= board_module.COLS:
            return False
        if board_module.board[new_row][new_col]:
            return False
    return True


def place_block(block, grid_row, grid_col):
    undo_stack.append([row[:] for row in board_module.board])
    for row, col in block.cells:
        board_module.board[grid_row + row][grid_col + col] = block.color


def get_grid_position(pos):
    x, y = pos
    grid_col = round((x + PIECE_CELL / 2 - GRID_X - CELL_SIZE / 2) / CELL_SIZE)
    grid_row = round((y + PIECE_CELL / 2 - GRID_Y - CELL_SIZE / 2) / CELL_SIZE)
    return grid_row, grid_col


def draw_reset_button():
    pygame.draw.rect(screen, (200, 50, 50), RESET_RECT)
    pygame.draw.rect(screen, (255, 120, 120), RESET_RECT, 3)
    font = pygame.font.SysFont(None, 40)
    text = font.render("RESET", True, (255, 255, 255))
    screen.blit(text, text.get_rect(center=RESET_RECT.center))


def draw_undo_button():
    pygame.draw.rect(screen, (50, 100, 200), UNDO_RECT)
    pygame.draw.rect(screen, (100, 150, 255), UNDO_RECT, 3)
    font = pygame.font.SysFont(None, 40)
    text = font.render("UNDO", True, (255, 255, 255))
    screen.blit(text, text.get_rect(center=UNDO_RECT.center))


def is_game_over():
    for block in blocks:
        for r in range(board_module.ROWS):
            for c in range(board_module.COLS):
                if can_place(block, r, c):
                    return False
    return True


def draw_game_over():
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))
    font_big = pygame.font.SysFont(None, 100)
    font_small = pygame.font.SysFont(None, 48)
    text = font_big.render("GAME OVER", True, (255, 50, 50))
    screen.blit(text, text.get_rect(center=(300, 350)))
    hint = font_small.render("Press RESET to play again", True, (255, 255, 255))
    screen.blit(hint, hint.get_rect(center=(300, 450)))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if RESET_RECT.collidepoint(event.pos):
                reset_board()
                reset_score()
                blocks = spawn_blocks()
                block_positions = tray_positions.copy()
                undo_stack.clear()

            elif UNDO_RECT.collidepoint(event.pos):
                if undo_stack:
                    board_module.board = undo_stack.pop()

            else:
                for i in range(len(blocks) - 1, -1, -1):
                    rect = get_piece_rect(blocks[i], block_positions[i])
                    if rect.collidepoint(event.pos):
                        dragging_index = i
                        mouse_x, mouse_y = event.pos
                        block_x, block_y = block_positions[i]
                        drag_offset = (mouse_x - block_x, mouse_y - block_y)
                        break

        elif event.type == pygame.MOUSEMOTION:
            if dragging_index is not None:
                mouse_x, mouse_y = event.pos
                block_positions[dragging_index] = (
                    mouse_x - drag_offset[0],
                    mouse_y - drag_offset[1]
                )

        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging_index is not None:
                pos = block_positions[dragging_index]
                grid_row, grid_col = get_grid_position(pos)

                if can_place(blocks[dragging_index], grid_row, grid_col):
                    place_block(blocks[dragging_index], grid_row, grid_col)
                    rows, cols = check_and_clear()
                    add_score(rows, cols)
                    blocks[dragging_index] = random_block()

                block_positions[dragging_index] = tray_positions[dragging_index]
                dragging_index = None

    screen.fill((30, 30, 40))
    draw_board(screen)
    draw_placed_blocks()
    draw_score(screen, pygame)

    for i, block in enumerate(blocks):
        draw_piece(block, block_positions[i])

    draw_undo_button()
    draw_reset_button()

    if is_goal_reached():
        draw_win_screen(screen, pygame)
    elif is_game_over():
        draw_game_over()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
