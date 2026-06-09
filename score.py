score = 0
goal = 820

def add_score(rows_cleared, cols_cleared):
    global score
    score += (rows_cleared + cols_cleared) * 100

def reset_score():
    global score
    score = 0

def is_goal_reached():
    return score >= goal

def draw_score(screen, pygame):
    font = pygame.font.SysFont(None, 48)
    
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 740))
    
    goal_text = font.render(f"Goal: {goal}", True, (255, 215, 0))
    screen.blit(goal_text, (350, 740))

def draw_win_screen(screen, pygame):
    font_big = pygame.font.SysFont(None, 100)
    font_small = pygame.font.SysFont(None, 48)

    overlay = pygame.Surface((600, 820), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))
    
    win_text = font_big.render("YOU WIN!", True, (255, 215, 0))
    win_rect = win_text.get_rect(center=(300, 350))
    screen.blit(win_text, win_rect)
    
    score_text = font_small.render(f"Final Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(300, 450))
    screen.blit(score_text, score_rect)
