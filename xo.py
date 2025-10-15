import random

# Рандомный выбор первого хода, можно было бы сделать например камень-ножницы-бумага, но что имеем.
turn = random.randint(0, 1)
# Создание карты
MAP = [['-' for j in range(3)] for i in range(3)]


# Вывод карты
def printMap():
    col = 0
    print(' ', 0, 1, 2)
    for i in MAP:
        print(col, *i)
        col += 1


# Обработка хода крестиков
def xTurn():
    global turn
    print("Ход крестика.")
    x = int(input("Введите поле по горизонтали: "))
    y = int(input("Введите поле по вертикали: "))
    if MAP[x][y] == '-':
        MAP[x][y] = "x"
    else:
        print("Поле занято!")
    printMap()
    turn = not turn


# Обработка хода ноликов
def oTurn():
    global turn
    print("Ход нолика.")
    x = int(input("Введите поле по горизонтали: "))
    y = int(input("Введите поле по вертикали: "))
    if MAP[x][y] == "-":
        MAP[x][y] = "o"
    else:
        print("Поле занято!")
    printMap()
    turn = not turn


# Функция запуска
def run():
    printMap()

    # Вывод, того, кто первый ходит
    if turn:
        print("Первый крестик.\n")
    else:
        print("Первый нолик.\n")
    # Цикл сравнений
    while True:
        if turn:
            xTurn()

        else:
            oTurn()

        # Проверка победы крестиков
        if any([
            all([
                MAP[0][0] == 'x',
                MAP[0][1] == 'x',
                MAP[0][2] == 'x'
            ]),
            all([
                MAP[1][0] == 'x',
                MAP[1][1] == 'x',
                MAP[1][2] == 'x'
            ]),
            all([
                MAP[2][0] == 'x',
                MAP[2][1] == 'x',
                MAP[2][2] == 'x'
            ]),
            all([
                MAP[0][0] == 'x',
                MAP[1][1] == 'x',
                MAP[2][2] == 'x'
            ]),
            all([
                MAP[2][0] == 'x',
                MAP[1][1] == 'x',
                MAP[0][2] == 'x'
            ]),
            all([
                MAP[0][0] == 'x',
                MAP[1][0] == 'x',
                MAP[2][0] == 'x'
            ]),
            all([
                MAP[0][1] == 'x',
                MAP[1][1] == 'x',
                MAP[2][1] == 'x'
            ]),
            all([
                MAP[0][2] == 'x',
                MAP[1][2] == 'x',
                MAP[2][2] == 'x'
            ]),
        ]):
            print("Крестики WIN!")
            break

        # Проверка победы ноликов
        if any([
            all([
                MAP[0][0] == 'o',
                MAP[0][1] == 'o',
                MAP[0][2] == 'o'
            ]),
            all([
                MAP[1][0] == 'o',
                MAP[1][1] == 'o',
                MAP[1][2] == 'o'
            ]),
            all([
                MAP[2][0] == 'o',
                MAP[2][1] == 'o',
                MAP[2][2] == 'o'
            ]),
            all([
                MAP[0][0] == 'o',
                MAP[1][1] == 'o',
                MAP[2][2] == 'o'
            ]),
            all([
                MAP[2][0] == 'o',
                MAP[1][1] == 'o',
                MAP[0][2] == 'o'
            ]),
            all([
                MAP[0][0] == 'o',
                MAP[1][0] == 'o',
                MAP[2][0] == 'o'
            ]),
            all([
                MAP[0][1] == 'o',
                MAP[1][1] == 'o',
                MAP[2][1] == 'o'
            ]),
            all([
                MAP[0][2] == 'o',
                MAP[1][2] == 'o',
                MAP[2][2] == 'o'
            ]),
        ]):
            print("Нолики WIN!")
            break

        # Проверка на заполненое поле
        if all([
            "-" not in MAP[0],
            "-" not in MAP[1],
            "-" not in MAP[2],
        ]):
            print("Ничья")
            break


# Инициализация
run()
