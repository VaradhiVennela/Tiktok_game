"""Game configuration and constants."""

# Window Settings
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600

# Colors
BG_COLOR = (20, 20, 20)
WHITE = (255, 255, 255)
RED = (255, 50, 50)

# Game Settings
FPS = 60
CONTENT_SPAWN_RATE = 0.02  # 2% chance per frame
WRONG_CONTENT_RATE = 0.2   # 20% chance for wrong content
MAX_CONTENTS = 5
MAX_MISSED = 5

# Content Settings
CONTENT_WIDTH = 300
CONTENT_HEIGHT = 150
CONTENT_SPEED = 3

# Scoring
GOOD_CONTENT_POINTS = 10
BAD_CONTENT_POINTS = -50

# Font Settings
MAIN_FONT = 'Arial'
SCORE_FONT_SIZE = 32
CONTENT_FONT_SIZE = 20