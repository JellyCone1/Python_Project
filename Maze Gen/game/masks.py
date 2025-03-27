# Masks and Pixel Perfect Collision Detection
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Learning About Masks")

# Load the Image, get the rectangle from the image and form a mask from surface
# Then Project the mask to_surface()
subject = pygame.image.load("subject.png").convert_alpha()
subject_rect = subject.get_rect()   
subject_mask = pygame.mask.from_surface(subject)
mask_image = subject_mask.to_surface()
subject_rect.topleft = (250, 250)

'''
pygame object for representing images
Surface((width, height), flags=0, depth=0, masks=None) -> Surface
Surface((width, height), flags=0, Surface) -> Surface
'''
glow = pygame.Surface((10, 10))
glow.fill(RED)
glow_mask = pygame.mask.from_surface(glow)

# game loop
running = True
while running:
    screen.fill(BLACK)

    # Get Mouse Coordinates
    mouse_coords = pygame.mouse.get_pos()

    # Draw Mask Image
    # screen.blit(subject, (subject_rect.x, subject_rect.y))
    screen.blit(mask_image, (0, 0))
    screen.blit(subject, subject_rect)
    screen.blit(glow, mouse_coords)

    # Check Mask Overlap || Collision Detection
    if subject_mask.overlap(glow_mask, (mouse_coords[0] - subject_rect.topleft[0], mouse_coords[1] - subject_rect.topleft[1])):
        col = RED
    else:
        col = GREEN

    glow.fill(col)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()