board = [' '] * 9
selected = [0, 1, 2, 3, 4, 5, 6, 7, 8]
win = False


def display_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


def player_symbol():
    p1_symbol = ' '

    while p1_symbol not in ['o', 'x']:
        p1_symbol = input('Player1, enter your symbol [o or x]: ')
    if p1_symbol == 'o':
        p2_symbol = 'x'
    else:
        p2_symbol = 'o'
    return (p1_symbol, p2_symbol)


def player1_choice(selected):
    p1_choice = ''

    while p1_choice not in selected:
        p1_choice = int(input(f'Player1, enter your choice from the list {selected}: '))
    return int(p1_choice)


def player2_choice(selected):
    p2_choice = ''

    while p2_choice not in selected:
        p2_choice = int(input(f'Player2, enter your choice from the list {selected}: '))
    return int(p2_choice)


def update_board1(p1_symbol, p1_choice):
    board[p1_choice] = p1_symbol
    display_board(board)


def update_board2(p2_symbol, p2_choice):
    board[p2_choice] = p2_symbol
    display_board(board)


def game(board, p1_symbol, p2_symbol):
    if board[0] == board[1] == board[2] == p1_symbol:
        print('Congratulations! Player1, you won the game.')
        win = True
    elif board[0] == board[1] == board[2] == p2_symbol:
        print('Congratulations! Player2, you won the game.')
        win = True
    elif board[3] == board[4] == board[5] == p1_symbol:
        print('Congratulations! Player1, you won the game.')
        win = True
    elif board[3] == board[4] == board[5] == p2_symbol:
        print('Congratulations! Player2, you won the game.')
        win = True
    elif board[6] == board[7] == board[8] == p1_symbol:
        print('Congratulations! Player1, you won the game.')
        win = True
    elif board[6] == board[7] == board[8] == p2_symbol:
        print('Congratulations! Player2, you won the game.')
        win = True
    elif board[0] == board[3] == board[6] == p1_symbol:
        print('Congratulations! Player1, you won the game.')
        win = True
    elif board[0] == board[3] == board[6] == p2_symbol:
        print('Congratulations! Player2, you won the game.')
        win = True
    elif board[1] == board[4] == board[7] == p1_symbol:
        print('Congratulations! Player1, you won the game.')
        win = True
    elif board[1] == board[4] == board[7] == p2_symbol:
        print('Congratulations! Player2, you won the game.')
        win = True
    elif board[2] == board[5] == board[8] == p1_symbol:
        print('Congratulations! Player1, you won the game.')
        win = True
    elif board[2] == board[5] == board[8] == p2_symbol:
        print('Congratulations! Player2, you won the game.')
        win = True
    elif board[0] == board[4] == board[8] == p1_symbol:
        print('Congratulations! Player1, you won the game.')
        win = True
    elif board[0] == board[4] == board[8] == p2_symbol:
        print('Congratulations! Player2, you won the game.')
        win = True
    elif board[2] == board[4] == board[6] == p1_symbol:
        print('Congratulations! Player1, you won the game.')
        win = True
    elif board[2] == board[4] == board[6] == p2_symbol:
        print('Congratulations! Player2, you won the game.')
        win = True
    else:
        win = False
    return win


def play(board, selected, p1_symbol, p2_symbol, win):
    while not win:
        if len(selected) != 0:
            p1_choice = player1_choice(selected)
            selected.remove(p1_choice)
            update_board1(p1_symbol, p1_choice)
            win = game(board, p1_symbol, p2_symbol)
        else:
            print('Board is Full')
            win = True

        if len(selected) != 0 and not win:
            p2_choice = player2_choice(selected)
            selected.remove(p2_choice)
            update_board2(p2_symbol, p2_choice)
            win = game(board, p1_symbol, p2_symbol)
        else:
            print('Either Board is Full or Player1 won the game')
            win = True


p1_symbol, p2_symbol = player_symbol()
play(board, selected, p1_symbol, p2_symbol, win)
