"""Content class module for the TikTok-style game."""

import random
import pygame
from config import (
    WINDOW_WIDTH, CONTENT_WIDTH, CONTENT_HEIGHT,
    CONTENT_SPEED, WHITE, RED, WRONG_CONTENT_RATE,
    GOOD_CONTENT_POINTS, BAD_CONTENT_POINTS,
    CONTENT_FONT_SIZE, MAIN_FONT
)

class Content:
    """Represents a content block in the game that players need to interact with."""
    
    def __init__(self):
        """Initialize a new content block with random properties."""
        self.width = CONTENT_WIDTH
        self.height = CONTENT_HEIGHT
        self.x = (WINDOW_WIDTH - self.width) // 2
        self.y = WINDOW_HEIGHT
        self.speed = CONTENT_SPEED
        self.is_wrong = random.random() < WRONG_CONTENT_RATE
        self.color = RED if self.is_wrong else (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )
        self.clicked = False
        self.points = BAD_CONTENT_POINTS if self.is_wrong else GOOD_CONTENT_POINTS

    def move(self):
        """Move the content block upward."""
        self.y -= self.speed

    def is_off_screen(self):
        """Check if the content block has moved off the screen."""
        return self.y + self.height < 0

    def contains_point(self, x, y):
        """Check if a point (x, y) is within the content block."""
        return (
            self.x <= x <= self.x + self.width and
            self.y <= y <= self.y + self.height
        )

    def draw(self, surface):
        """Draw the content block on the given surface."""
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        if not self.clicked:
            points_text = str(self.points)
            font = pygame.font.SysFont(MAIN_FONT, CONTENT_FONT_SIZE)
            text = font.render(points_text, True, WHITE)
            text_rect = text.get_rect(
                center=(self.x + self.width//2, self.y + self.height//2)
            )
            surface.blit(text, text_rect)