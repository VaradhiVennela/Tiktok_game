import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
BG_COLOR = (20, 20, 20)
WHITE = (255, 255, 255)
RED = (255, 50, 50)

# Create window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('TikTok Game')

# Game classes
class Content:
    def __init__(self):
        self.width = 300
        self.height = 150
        self.x = (WINDOW_WIDTH - self.width) // 2
        self.y = WINDOW_HEIGHT
        self.speed = 3
        self.is_wrong = random.random() < 0.2  # 20% chance to be wrong content
        self.color = RED if self.is_wrong else (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.clicked = False
        self.points = -50 if self.is_wrong else 10

    def move(self):
        self.y -= self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        if not self.clicked:
            points_text = str(self.points)
            text = pygame.font.SysFont('Arial', 20).render(points_text, True, WHITE)
            text_rect = text.get_rect(center=(self.x + self.width//2, self.y + self.height//2))
            surface.blit(text, text_rect)

# Game variables
contents = [Content()]
score = 0
missed_contents = 0
MAX_MISSED = 5
game_over = False
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 32)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_pos = pygame.mouse.get_pos()
            for content in contents:
                if (content.x <= mouse_pos[0] <= content.x + content.width and
                    content.y <= mouse_pos[1] <= content.y + content.height and
                    not content.clicked):
                    score += content.points
                    content.clicked = True
                    if content.is_wrong:
                        game_over =
                         True
        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:
                # Reset game
                score = 0
                missed_contents = 0
                game_over = False
                contents = [Content()]

    if not game_over:
        # Game logic
        if random.random() < 0.02 and len(contents) < 5:  # 2% chance to spawn new content
            contents.append(Content())

        for content in contents:
            content.move()

        # Count missed contents
        for content in contents:
            if content.y + content.height < 0 and not content.clicked and not content.is_wrong:
                missed_contents += 1

        if missed_contents >= MAX_MISSED:
            game_over = True

        # Remove contents that are off screen
        contents = [content for content in contents if content.y + content.height > 0]

    # Drawing
    screen.fill(BG_COLOR)
    
    for content in contents:
        content.draw(screen)

    # Draw score
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    # Draw missed counter
    if not game_over:
        missed_text = font.render(f'Missed: {missed_contents}/{MAX_MISSED}', True, WHITE)
        screen.blit(missed_text, (10, 50))

    # Draw game over screen
    if game_over:
        game_over_text = font.render('Game Over!', True, RED)
        final_score_text = font.render(f'Final Score: {score}', True, WHITE)
        restart_text = font.render('Press SPACE to restart', True, WHITE)
        
        screen.blit(game_over_text, (WINDOW_WIDTH//2 - game_over_text.get_width()//2, WINDOW_HEIGHT//2 - 60))
        screen.blit(final_score_text, (WINDOW_WIDTH//2 - final_score_text.get_width()//2, WINDOW_HEIGHT//2))
        screen.blit(restart_text, (WINDOW_WIDTH//2 - restart_text.get_width()//2, WINDOW_HEIGHT//2 + 60))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()