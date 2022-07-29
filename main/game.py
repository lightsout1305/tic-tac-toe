import tictactoe


def try_again():
    while True:
        again = input('Do you want to play again?\n ')
        if again == 'Yes'.lower():
            from importlib import reload
            reload(tictactoe)
        else:
            print('Goodbye!')
            break


try_again()

