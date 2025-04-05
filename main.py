"""Main game module for the TikTok-style content sorting game."""

import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from game_manager import GameManager

def main():
    """Main game loop."""
    # Initialize Pygame
    pygame.init()

    # Create window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('TikTok Game')

    # Initialize game
    game = GameManager()
    clock = pygame.time.Clock()

    # Game loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_click(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN and game.game_over:
                if event.key == pygame.K_SPACE:
                    game.reset_game()

        # Update game state
        game.update()

        # Draw everything
        game.draw(screen)
        pygame.display.flip()

        # Control game speed
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()