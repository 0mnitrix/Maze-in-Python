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
    maze[1][0] = PATH  # старт
    maze[height - 2][width - 1] = PATH  # выход
    return maze

def print_maze(maze, start, end):
    for y in range(len(maze)):
        row = ''
        for x in range(len(maze[0])):
            if (x, y) == start:
                row += 'S'
            elif (x, y) == end:
                row += 'E'
            elif maze[y][x] == WALL:
                row += '#'
            else:
                row += ' '
        print(row)

def get_user_input():
    while True:
        try:
            width = int(input("Введите ширину лабиринта (нечётное число ≥ 11): "))
            height = int(input("Введите высоту лабиринта (нечётное число ≥ 11): "))
            if width >= 11 and height >= 11 and width % 2 == 1 and height % 2 == 1:
                return width, height
            else:
                print("Размеры должны быть нечётными и ≥ 11.")
        except ValueError:
            print("Введите целые числа.")

if __name__ == "__main__":
    width, height = get_user_input()
    maze = generate_maze(width, height)
    start = (0, 1)
    end = (width - 1, height - 2)

    print("\nСгенерированный лабиринт:\n")
    print_maze(maze, start, end)
