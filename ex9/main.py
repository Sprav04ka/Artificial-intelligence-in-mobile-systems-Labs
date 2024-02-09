import random

print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)


def draw_board(board):
    print("-" * (len(board) + 4))
    for i in range(len(board)):
        print("|", end="")
        for j in range(len(board[i])):
            print(board[i][j], end=" | ")
        print("\n" + "-" * (len(board) + 4))


def take_input(player_token, board):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= len(board)**2:
            x = (player_answer - 1) // len(board)
            y = (player_answer - 1) % len(board)
            if str(board[x][y]) not in "XO":
                board[x][y] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до {}.".format(len(board)**2))


def take_computer_input(player_token, board):
    valid = False
    while not valid:
        player_answer = random.randint(1, len(board)**2)
        x = (player_answer - 1) // len(board)
        y = (player_answer - 1) % len(board)
        if str(board[x][y]) not in "XO":
            board[x][y] = player_token
            valid = True


def check_win(board):
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1),
                                            (2, 1)), ((0, 2), (1, 2), (2, 2)),
                 ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for each in win_coord:
        if board[each[0][0]][each[0][1]] == board[each[1][0]][each[1][1]] == board[each[2][0]][each[2][1]] != " ":
            return board[each[0][0]][each[0][1]]
    return False


def main():
    mode = int(
        input("Выберите режим игры (1 - игра 5x5, 2 - игра с компьютером): "))
    size = 5 if mode == 1 else 3
    board = [[" "]*size for _ in range(size)]
    counter = 0
    win = False
    first_move = "X" if random.randint(0, 1) == 0 else "O"
    if mode == 2 and first_move == "O":
        print("Компьютер делает первый ход.")
        take_computer_input("X", board)
        counter += 1
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            if mode == 2:
                take_computer_input("X", board)
            else:
                take_input("X", board)
        else:
            take_input("O", board)
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == size**2:
            print("Ничья!")
            break
    draw_board(board)


main()
input("Нажмите Enter для выхода!")
