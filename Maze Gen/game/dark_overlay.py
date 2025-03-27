import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Radial Light Effect")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Background layer (the layer to reveal)
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(WHITE)  # Example: A white background

# Dark overlay
dark_overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
dark_overlay.fill((0, 0, 0, 200))  # Semi-transparent black

# Light mask (circular gradient)
light_radius = 100
light_mask = pygame.Surface((light_radius * 2, light_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(light_mask, (0, 0, 0, 0), (light_radius, light_radius), light_radius)
pygame.draw.circle(light_mask, (0, 0, 0, 255), (light_radius, light_radius), light_radius, width=1)
light_mask.set_colorkey((0, 0, 0, 255))  # Make the circle transparent

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Clear screen
    screen.blit(background, (0, 0))

    # Draw dark overlay
    screen.blit(dark_overlay, (0, 0))

    # Draw light mask at mouse position
    screen.blit(light_mask, (mouse_x - light_radius, mouse_y - light_radius))

    # Update display
    pygame.display.flip()
    clock.tick(60)
