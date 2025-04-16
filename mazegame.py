import turtle
import random

WALL = 1
PATH = 0

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
    maze[1][0] = PATH       # вход
    maze[height - 2][width - 1] = PATH  # выход
    return maze

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
            if maze[y][x] == WALL:
                draw_cell(t, x, y, cell_size, "white")

# Запуск
if __name__ == "__main__":
    width, height = 21, 21
    cell_size = 20
    maze = generate_maze(width, height)
    draw_maze(maze, cell_size)
    turtle.done()
