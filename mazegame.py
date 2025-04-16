import random

def generate_maze(rows=10, cols=10):
    maze = [[' # '] * (2 * cols + 1) for _ in range(2 * rows + 1)]
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
import turtle

def draw_cell(t, x, y, size, color):
    t.goto(x * size - 200, 200 - y * size)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.pendown()
        t.forward(size)
        t.right(90)
    t.penup()
    t.end_fill()

def draw_maze(maze, cell_size=20):
    turtle.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.hideturtle()

    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 1:  # WALL
                draw_cell(t, x, y, cell_size, "white")

