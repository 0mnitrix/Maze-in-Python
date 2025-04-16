import turtle
import random
import time

WALL = 1
PATH = 0
VISITED = 2

def generate_maze(width, height):
    maze = [[WALL for _ in range(width)] for _ in range(height)]

    def carve(x, y):
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1:
                if maze[ny][nx] == WALL:
                    maze[ny][nx] = PATH
                    maze[y + dy // 2][x + dx // 2] = PATH
                    carve(nx, ny)

    maze[1][1] = PATH
    carve(1, 1)
    maze[1][0] = PATH  # вход
    maze[height - 2][width - 1] = PATH  # выход
    return maze

def draw_maze(maze, cell_size=20):
    turtle.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.hideturtle()

    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == WALL:
                draw_cell(t, x, y, cell_size, "white")

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

def solve_maze(maze, x, y, end_x, end_y, cell_size, t):
    if x == end_x and y == end_y:
        draw_cell(t, x, y, cell_size, "green")
        return True

    if maze[y][x] != PATH:
        return False

    maze[y][x] = VISITED
    draw_cell(t, x, y, cell_size, "blue")
    time.sleep(0.02)

    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x
