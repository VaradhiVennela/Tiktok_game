\"""Game manager module for handling game state and logic."""

import random
import pygame
from content import Content
from config import (
    WINDOW_WIDTH, WINDOW_HEIGHT, BG_COLOR, WHITE, RED,
    MAX_MISSED, MAX_CONTENTS, CONTENT_SPAWN_RATE,
    MAIN_FONT, SCORE_FONT_SIZE
)

class GameManager:
    """Manages game state, scoring, and content."""

    def __init__(self):
        """Initialize the game manager."""
        self.reset_game()
        self.font = pygame.font.SysFont(MAIN_FONT, SCORE_FONT_SIZE)

    def reset_game(self):
        """Reset the game state to initial values."""
        self.contents = [Content()]
        self.score = 0
        self.missed_contents = 0
        self.game_over = False

    def update(self):
        """Update game state."""
        if self.game_over:
            return

        # Spawn new content
        if random.random() < CONTENT_SPAWN_RATE and len(self.contents) < MAX_CONTENTS:
            self.contents.append(Content())

        # Update content positions
        for content in self.contents:
            content.move()

        # Check for missed content
        for content in self.contents:
            if content.is_off_screen() and not content.clicked and not content.is_wrong:
                self.missed_contents += 1

        # Check game over condition
        if self.missed_contents >= MAX_MISSED:
            self.game_over = True

        # Remove off-screen content
        self.contents = [content for content in self.contents if not content.is_off_screen()]

    def handle_click(self, mouse_pos):
        """Handle mouse click events."""
        if self.game_over:
            return

        for content in self.contents:
            if content.contains_point(*mouse_pos) and not content.clicked:
                self.score += content.points
                content.clicked = True
                if content.is_wrong:
                    self.game_over = True

    def draw(self, screen):
        """Draw the game state."""
        screen.fill(BG_COLOR)

        # Draw all content
        for content in self.contents:
            content.draw(screen)

        # Draw score
        score_text = self.font.render(f'Score: {self.score}', True, WHITE)
        screen.blit(score_text, (10, 10))

        # Draw missed counter
        if not self.game_over:
            missed_text = self.font.render(f'Missed: {self.missed_contents}/{MAX_MISSED}', True, WHITE)
            screen.blit(missed_text, (10, 50))

        # Draw game over screen
        if self.game_over:
            self._draw_game_over(screen)

    def _draw_game_over(self, screen):
        """Draw the game over screen."""
        game_over_text = self.font.render('Game Over!', True, RED)
        final_score_text = self.font.render(f'Final Score: {self.score}', True, WHITE)
        restart_text = self.font.render('Press SPACE to restart', True, WHITE)

        screen.blit(
            game_over_text,
            (WINDOW_WIDTH//2 - game_over_text.get_width()//2, WINDOW_HEIGHT//2 - 60)
        )
        screen.blit(
            final_score_text,
            (WINDOW_WIDTH//2 - final_score_text.get_width()//2, WINDOW_HEIGHT//2)
        )
        screen.blit(
            restart_text,
            (WINDOW_WIDTH//2 - restart_text.get_width()//2, WINDOW_HEIGHT//2 + 60)
        )