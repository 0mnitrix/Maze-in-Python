import random

def generate_maze(rows=10, cols=10):
    maze = [['# '] * (2 * cols + 1) for _ in range(2 * rows + 1)]
    visited = [[False] * cols for _ in range(rows)]

    def carve(x, y):
        visited[y][x] = True
        maze[2 * y + 1][2 * x + 1] = '  '

        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < cols and 0 <= ny < rows and not visited[ny][nx]:
                maze[2 * y + 1 + dy][2 * x + 1 + dx] = ''
                carve(nx, ny)

    carve(0, 0)
    maze[1][0] = ' S '  
    maze[2 * rows - 1][2 * cols] = ' E ' 
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

maze = generate_maze()
print_maze(maze)
