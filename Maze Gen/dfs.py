# In a Conventional Adjaceny matrix, you would look if a link exist between the two nodes
# But here, by default, en edge exists beteen all 4 directions of a vertex for every vertex that is not at the edge or outside the screen


import pygame
import random
import sys

width, height = 1000, 800

# um.printGrid(grid, rows, columns)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("DFS Maze Generation")
clock = pygame.time.Clock()
tick_rate = 30
recursion_limit = 1500
sys.setrecursionlimit(recursion_limit)

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

cell_size = 50
rows, columns = height//cell_size, width//cell_size
wall_thickness = 1
scaling = 1.0

directions = {
    "UP": (0, -1), 
    "DOWN": (0, 1), 
    "LEFT": (-1, 0), 
    "RIGHT": (1, 0)
}  # Because the origin is at top left of the screen and going down means moving positive y coords


class Cell:
    def __init__(self, x, y):
        # Basic Attributes of a Cell
        self.x = x
        self.y = y
        self.walls = {"UP": True, "DOWN": True, "LEFT": True, "RIGHT": True}
        self.visited = False

    def draw(self):
        # Start Position
        x1, y1 = self.x*cell_size, self.y*cell_size
        if self.walls["UP"]:
            pygame.draw.line(screen, BLACK, (x1, y1), (x1 + cell_size, y1), wall_thickness)
        if self.walls["DOWN"]:
            pygame.draw.line(screen, BLACK, (x1, y1 + cell_size), (x1 + cell_size, y1 + cell_size), wall_thickness)
        if self.walls["LEFT"]:
            pygame.draw.line(screen, BLACK, (x1, y1), (x1, y1 + cell_size), wall_thickness)
        if self.walls["RIGHT"]:
            pygame.draw.line(screen, BLACK, (x1 + cell_size, y1), (x1 + cell_size, y1 + cell_size), wall_thickness)

    def highlight(self, color):
        x1, y1 = self.x * cell_size, self.y * cell_size
        # cell = pygame.Rect(x1, y1, cell_size, cell_size)
        offset = (cell_size/2)*(1-scaling)
        pygame.draw.rect(screen, color, (x1 + offset, y1 + offset, cell_size*scaling, cell_size*scaling))


grid = [[Cell(cols, row) for cols in range(columns)] for row in range(rows)]


def get_unvisited_neighbours(cell):
    neighbours = []
    for direction, (dx, dy) in directions.items():
        nx, ny = cell.x + dx, cell.y + dy
        if 0 <= nx < columns and 0 <= ny < rows and not grid[ny][nx].visited:
            neighbours.append((direction, grid[ny][nx]))
    return neighbours


# Remove walls between 2 cells
def remove_walls(current, next, direction):
    if direction == "UP":
        current.walls["UP"], next.walls["DOWN"] = False, False
    elif direction == "DOWN":
        current.walls["DOWN"], next.walls["UP"] = False, False
    elif direction == "LEFT":
        current.walls["LEFT"], next.walls["RIGHT"] = False, False
    elif direction == "RIGHT":
        current.walls["RIGHT"], next.walls["LEFT"] = False, False

# Generate the Maze
def dfs_maze_gen():
    stack = []
    current_cell = grid[0][0]
    current_cell.visited = True
    stack.append(current_cell)

    while len(stack) > 0:
        current_cell.highlight(BLUE)
        pygame.display.flip()

        # Get Unvisited Neighbours of current cell
        neighbours = get_unvisited_neighbours(current_cell)
        if neighbours:
            # Choose Random Neighbour
            direction, next_cell = random.choice(neighbours)
            
            # Remove its walls to make a path
            remove_walls(current_cell, next_cell, direction)
            
            next_cell.visited = True
            stack.append(next_cell)

            # Move to the next cell
            current_cell = next_cell
        else:
            # Backtrack
            current_cell = stack.pop()

        screen.fill(WHITE)
        for cell in stack:
            cell.highlight(YELLOW)

        for row in grid:
            for cell in row:
                cell.draw()
        clock.tick(tick_rate)

    return True


start = grid[0][0]
end = grid[-1][-1]
wall_cycle = ["UP", "RIGHT", "DOWN", "LEFT"]
path = []


# recursive
def dfs_solver_rec(current: Cell):
    global path
    screen.fill(WHITE)
    draw_path(RED)

    for row in grid:
        for cell in row:
            cell.draw()
    clock.tick(tick_rate)
    pygame.display.flip()
    print(f"Visiting Cell: ({current.x}, {current.y})")  # Debugging Output

    if current == end:
        print("Maze Solved!")
        path.append(current)
        return True
    
    current.visited = True
    path.append(current)

    for direction in wall_cycle:
        if not current.walls[direction]:        
            dx, dy = directions[direction]
            nx, ny = current.x + dx, current.y + dy

            if 0 <= nx < columns and 0 <= ny < rows:
                neighbour = grid[ny][nx]
                if not neighbour.visited:
                    if dfs_solver_rec(neighbour):
                        return True
    
    # Backtracking if no valid path is found
    print(f"Backtracking from Cell: ({current.x}, {current.y})")
    path.pop()
    return False


# stack
def dfs_solver_stk(start: Cell):
    # global path
    global stack
    stack = [start]
    start.visited = True
    # print(f"Visiting Cell: ({current.x}, {current.y})")  # Debugging Output
    
    while stack:
        current = stack[-1]
        # path.append(current)

        if current == end:
            print("Maze Solved!")
            return True
        
        unvisited_neighbours = []
        for direction in wall_cycle:
            if not current.walls[direction]:        
                dx, dy = directions[direction]
                nx, ny = current.x + dx, current.y + dy

                if 0 <= nx < columns and 0 <= ny < rows:
                    neighbour = grid[ny][nx]
                    if not neighbour.visited:
                        unvisited_neighbours.append((direction, neighbour))
        
        if unvisited_neighbours:
            _, next_cell = random.choice(unvisited_neighbours)
            next_cell.visited = True
            stack.append(next_cell)
        else:
            stack.pop()

        # Draw Updates
        screen.fill(WHITE)
        # draw_path(RED)
        for cell in stack:
            cell.highlight(RED)
        for row in grid:
            for cell in row:
                cell.draw()


        pygame.display.flip()
        clock.tick(tick_rate)

    return False


def draw_path(color):
    for cell in path:
        cell.highlight(color)


def main():
    running = True
    maze_generated = False  # Flag to track maze generation state
    maze_solved = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not maze_generated:
            maze_generated = dfs_maze_gen()

        
        if not maze_solved:
            # Reset visited flags before solving
            for row in grid:
                for cell in row:
                    cell.visited = False
            # dfs_solver_rec(start)           # -> ENABLE FOR RECURSION
            dfs_solver_stk(start)         # -> ENABLE FOR STACK BASED
            maze_solved = True

        
        screen.fill(WHITE)
        # draw_path(GREEN)                    # -> ENABLE FOR RECURSION
        for cell in stack:                # -> ENABLE FOR STACK BASED
            cell.highlight(RED)           # -> ENABLE FOR STACK BASED
        for row in grid:
            for cell in row:
                cell.draw()
        
        # grid[0][0].highlight(BLUE)
        
        
        pygame.display.flip()
    
    pygame.quit()
    

if __name__ == "__main__":
    main()
