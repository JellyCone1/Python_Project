# ---------------------------------|| FUNCTIONS ||---------------------------------


def create2DGrid():
    x = [[0 for _ in range(col)] for _ in range(row)]
    return x


def printGrid():
    for i in range(row):
        for j in range(col):
            print(grid[i][j], end=' ')
        print()


def printGrid():
    print(end='  ')
    for i in v:
        print(i, end=' ')
    print()
    for i in range(row):
        print(v[i], end=' ')
        for j in range(col):
            print(grid[i][j], end=' ')
        print()


def add_edge(src, dst):
    # row_major
    grid[v.index(src)][v.index(dst)] = 1


def neighbours(vertex):
    vertex_index = v.index(vertex)
    return [v[i] for i in range(len(grid[vertex_index])) if grid[vertex_index][i] == True]
    # for i in range(len(grid[v.index(vertex)])):
    #     if grid[v.index(vertex)][i] == True:
    #         neighbours.append(v[i])
    # print(neighbours)


def dfs(start):
    stack = [start]
    
    while len(stack) > 0:
        current = stack.pop()
        current_index = v.index(current)
        
        if not visited[current_index]:
            print(current, end=' ')
            visited[current_index] = True
            neighbour_list = neighbours(current)
            
            if neighbour_list:
                random.shuffle(neighbour_list)
                for neighbour in neighbour_list:
                    if not visited[v.index(neighbour)]:
                        stack.append(neighbour)


# ---------------------------------|| FUNCTIONS ||---------------------------------
# DFS using stack
import random

row, col = 5, 5
v = ['A', 'B', 'C', 'D', 'E']
visited = [False for _ in range(len(v))]

grid = create2DGrid()
# um.printGrid(grid, row, col)

add_edge('A', 'B')
add_edge('A', 'D')
add_edge('C', 'A')
add_edge('E', 'B')
add_edge('D', 'E')
add_edge('C', 'E')
add_edge('B', 'D')

printGrid()
# neighbours('A')

dfs('C')

