import turtle
import random

WALL = 1
PATH = 0

player_pos = [1, 1]

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
    maze[1][0] = PATH
    maze[height - 2][width - 1] = PATH
    return maze

def draw_cell(t, x, y, size, color):
    t.clear()
    t.goto(x * size - 200, 200 - y * size)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def draw_maze(maze, cell_size=20):
    turtle.bgcolor("black")
    drawer = turtle.Turtle()
    drawer.speed(0)
    drawer.penup()
    drawer.hideturtle()

    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == WALL:
                draw_square(drawer, x, y, cell_size, "white")
            elif (x, y) == (0, 1):
                draw_square(drawer, x, y, cell_size, "blue")
            elif (x, y) == (len(maze[0]) - 1, len(maze) - 2):
                draw_square(drawer, x, y, cell_size, "red")

def draw_square(t, x, y, size, color):
    t.goto(x * size - 200, 200 - y * size)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.pendown()
        t.forward(size)
        t.right(90)
    t.penup()
    t.end_fill()

def move_player(dx, dy):
    global player_pos
    x, y = player_pos
    nx, ny = x + dx, y + dy

    if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze):
        if maze[ny][nx] == PATH:
            player_pos = [nx, ny]
            draw_cell(player, nx, ny, cell_size, "green")

            if (nx, ny) == (len(maze[0]) - 1, len(maze) - 2):
                print("Вы дошли до выхода!")
                turtle.bye()

def bind_keys():
    turtle.listen()
    turtle.onkey(lambda: move_player(0, -1), "Up")
    turtle.onkey(lambda: move_player(0, 1), "Down")
    turtle.onkey(lambda: move_player(-1, 0), "Left")
    turtle.onkey(lambda: move_player(1, 0), "Right")

# Параметры запуска
width, height = 21, 21
cell_size = 20
maze = generate_maze(width, height)
draw_maze(maze, cell_size)

# Игрок
player = turtle.Turtle()
player.speed(0)
player.penup()
player.hideturtle()

# Отрисовать начальное положение игрока
draw_cell(player, player_pos[0], player_pos[1], cell_size, "green")

bind_keys()
turtle.done()
