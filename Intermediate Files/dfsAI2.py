import pygame
import random

# Constants for grid size and screen dimensions
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 50
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE
wall_thickness = 1
tick_rate = 30

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Generation using DFS")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Directions for neighbor lookup
DIRECTIONS = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0)
}

# Define the grid cell with walls
class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {"UP": True, "DOWN": True, "LEFT": True, "RIGHT": True}
        self.visited = False

    # Draw the walls of the cell
    def draw(self):
        x1, y1 = self.x * CELL_SIZE, self.y * CELL_SIZE
        if self.walls["UP"]:
            pygame.draw.line(screen, WHITE, (x1, y1), (x1 + CELL_SIZE, y1), wall_thickness)
        if self.walls["DOWN"]:
            pygame.draw.line(screen, WHITE, (x1, y1 + CELL_SIZE), (x1 + CELL_SIZE, y1 + CELL_SIZE), wall_thickness)
        if self.walls["LEFT"]:
            pygame.draw.line(screen, WHITE, (x1, y1), (x1, y1 + CELL_SIZE), wall_thickness)
        if self.walls["RIGHT"]:
            pygame.draw.line(screen, WHITE, (x1 + CELL_SIZE, y1), (x1 + CELL_SIZE, y1 + CELL_SIZE), wall_thickness)

    # Highlight the cell (optional, for visualization)
    def highlight(self, color):
        x1, y1 = self.x * CELL_SIZE, self.y * CELL_SIZE
        pygame.draw.rect(screen, color, (x1, y1, CELL_SIZE, CELL_SIZE))

# Initialize the grid
grid = [[Cell(col, row) for col in range(COLS)] for row in range(ROWS)]

# Get the neighbors of a cell
def get_unvisited_neighbors(cell):
    neighbors = []
    for direction, (dx, dy) in DIRECTIONS.items():
        nx, ny = cell.x + dx, cell.y + dy
        if 0 <= nx < COLS and 0 <= ny < ROWS and not grid[ny][nx].visited:
            neighbors.append((direction, grid[ny][nx]))
    return neighbors

# Remove walls between two cells
def remove_walls(current, next_cell, direction):
    if direction == "UP":
        current.walls["UP"], next_cell.walls["DOWN"] = False, False
    elif direction == "DOWN":
        current.walls["DOWN"], next_cell.walls["UP"] = False, False
    elif direction == "LEFT":
        current.walls["LEFT"], next_cell.walls["RIGHT"] = False, False
    elif direction == "RIGHT":
        current.walls["RIGHT"], next_cell.walls["LEFT"] = False, False

# DFS Maze Generation Algorithm
def dfs_maze_generation():
    stack = []
    current_cell = grid[0][0]
    current_cell.visited = True
    stack.append(current_cell)

    while len(stack) > 0:
        # Highlight the current cell
        current_cell.highlight(BLUE)
        pygame.display.flip()

        # Get unvisited neighbors
        neighbors = get_unvisited_neighbors(current_cell)
        if neighbors:
            # Choose a random neighbor
            direction, next_cell = random.choice(neighbors)
            
            # Remove the wall between current and next cell
            remove_walls(current_cell, next_cell, direction)
            
            # Mark the next cell as visited and push to stack
            next_cell.visited = True
            stack.append(next_cell)

            # Move to the next cell
            current_cell = next_cell
        else:
            # Backtrack
            current_cell = stack.pop()

        # Draw the grid
        screen.fill(BLACK)
        for row in grid:
            for cell in row:
                cell.draw()
        clock.tick(tick_rate)  # Limit the frame rate
    
    # Return True when maze generation is complete
    return True


def main():
    running = True
    maze_generated = False  # Flag to track maze generation state

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not maze_generated:
            maze_generated = dfs_maze_generation()  # Run maze generation once

        # Draw the final maze
        screen.fill(BLACK)
        for row in grid:
            for cell in row:
                cell.draw()
        grid[0][0].highlight(BLUE)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
