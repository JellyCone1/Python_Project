import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)  # Highlight color for mask

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Learning About Masks")

# Load subject image
subject = pygame.image.load("subject.png").convert_alpha()
subject_rect = subject.get_rect()

# Create mask
subject_mask = pygame.mask.from_surface(subject)

# Convert mask to a visible surface
mask_image = subject_mask.to_surface(setcolor=RED, unsetcolor=(0, 0, 0, 0))  # Red mask, transparent background
mask_image.set_colorkey((0, 0, 0))  # Make black transparent

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Draw subject and mask image
    screen.blit(subject, (subject_rect.x, subject_rect.y))  # Uncomment to show subject
    screen.blit(mask_image, (subject_rect.x, subject_rect.y))  # Draw mask at correct position

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
