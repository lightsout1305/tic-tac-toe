def welcome():
    print()
    print("Welcome to the Tic-tac-toe game!")
    print()
    print("The main goal is to fill up the field with the winning combination of X or 0")
    print()
    print("The one who fills it up the first wins!")
    print()
    print("You have to input two coordinate figures: "
          "the first one indicates the string,"
          "the second one indicates the column")
    print()
    print("Let's get started!")
    print()


welcome()


def show_field():
    print("   | 0 | 1 | 2 |")
    print("----------------")
    for i, row in enumerate(tictactoe_field):
        row_str = f" {i} | {' | '.join(row)} | "
        print(row_str)
        print("----------------")


def ask_for_cord():
    while True:
        coodinates = input("Your turn: ").split()
        if len(coodinates) != 2:
            print("Type two digits")
            continue

        x, y = coodinates
        if not(x.isdigit()) and not(y.isdigit()):
            print("Type digits")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Type coordinates ranging 0 to 2")
            continue

        if tictactoe_field[x][y] != " ":
            print("Space is blocked")
            continue

        return x, y


def check_win():
    win_comb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for comb in win_comb:
        symbols = []
        for a in comb:
            symbols.append(tictactoe_field[a[0]][a[1]])
        if symbols == ["X", "X", "X"]:
            print("X won!")
            return True
        if symbols == ["O", "O", "O"]:
            print("O won!")
            print()
            return True
    return False


tictactoe_field = [[" "] * 3 for i in range(3)]


def game():
    num = 0
    while True:
        num += 1

        show_field()

        if num % 2 == 1:
            print("Type X")
        else:
            print("Type O")

        x, y = ask_for_cord()

        if num % 2 == 1:
            tictactoe_field[x][y] = "X"
        else:
            tictactoe_field[x][y] = "O"

        if check_win():
            break

    if num == 9:
        print("It's a draw")


game()









