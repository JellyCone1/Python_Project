import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
width, height = 600, 600
cell_size = 20
rows, columns = height // cell_size, width // cell_size

# Screen setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("DFS Maze Generation")
black, white, red = (0, 0, 0), (255, 255, 255), (255, 0, 0)

# Initialize grid
maze = [[0 for _ in range(columns)] for _ in range(rows)]

# DFS Function
def dfs(x, y):
    maze[y][x] = 1  # Mark cell as visited
    neighbors = [(x + dx, y + dy) for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]
                 if 0 <= x + dx < columns and 0 <= y + dy < rows and maze[y + dy][x + dx] == 0]
    random.shuffle(neighbors)

    for nx, ny in neighbors:
        # Visualize
        # Rect(left, top, width, height) -> Rect
        pygame.draw.rect(screen, white, (nx * cell_size, ny * cell_size, cell_size, cell_size))
        pygame.draw.rect(screen, red, (x * cell_size, y * cell_size, cell_size, cell_size))  # Current cell
        pygame.display.flip()
        pygame.time.wait(10)
        
        dfs(nx, ny)  # Recursive call

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # screen.fill(black)
    dfs(0, 0)  # Start DFS from top-left cell
    pygame.display.flip()
pygame.quit()
