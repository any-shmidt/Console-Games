import random

board = [' '] * 9
print(board)

play_game = True
turn = 1 #очередь, смена игрока

def get_board(board):
    print(board[0], end = '|')
    print(board[1], end = '|')
    print(board[2])
    print('-+-+-')
    
    print(board[3], end = '|')
    print(board[4], end = '|')
    print(board[5])
    print('-+-+-')
    
    print(board[6], end = '|')
    print(board[7], end = '|')
    print(board[8])
    
get_board(board)

def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'

def sign_choice():    # выбор X или 0 для игрока, который ходит первым
    correct_sign_choice = False
    while not correct_sign_choice:
        sign = input('Выберите букву - X или 0: ').upper()
        if sign.upper() not in 'X0':
            print('enter the X or 0')
        else:
            correct_sign_choice = True
            return sign
        
def player_input():    # ход игрока, выбор клеточки
    correct_choice = False
    while not correct_choice:
        choice = input('Ваш ход (свободная клеточка 1-9): ')
        try:
            choice = int(choice)
        except:
            print('enter the number')
            continue
        index_choice = int(choice) - 1
        if choice >= 1 and choice <= 9:
            if board[index_choice] == ' ':
                board[index_choice] = sign
                correct_choice = True
            else:
                print('Эта клеточка уже занята')
        else:
            print('введите число от 1 до 9')

def is_winner(board, sign):
    return (board[0] == sign and board[1] == sign and board[2] == sign) or\
           (board[3] == sign and board[4] == sign and board[5] == sign) or\
           (board[6] == sign and board[7] == sign and board[8] == sign) or\
           (board[0] == sign and board[3] == sign and board[6] == sign) or\
           (board[1] == sign and board[4] == sign and board[7] == sign) or\
           (board[2] == sign and board[5] == sign and board[8] == sign) or\
           (board[0] == sign and board[4] == sign and board[8] == sign) or\
           (board[2] == sign and board[4] == sign and board[6] == sign)

def drawn_game(is_winner):    # ничья
    if board.count(' ') == 0:
        return True
        
while play_game:
    
    sign = sign_choice()
    
    if sign == 'x'.upper():
        first_player = 'X'
        second_player = '0'
    else:
        first_player = '0'
        second_player = 'X'
        
    while turn <= 10:
        if turn % 2 != 0:
            sign = first_player
            print(f'Ваш ход, вы ходите {first_player}')
            player_input()
            turn += 1

            if is_winner(board, sign):
                play_game = False
                get_board(board)
                print(f'Победил {sign}')
                break
            if drawn_game(is_winner):
                play_game = False
                get_board(board)
                print('Drawn game')
                break

        print(board)

        get_board(board)
        print(turn)
        
        if turn % 2 == 0:
            sign = second_player
            print(f'Ваш ход, вы ходите {second_player}')
            player_input()
            turn +=1

            if is_winner(board, sign):
                play_game = False
                get_board(board)
                print(f'Победил {sign}')
                break
            if drawn_game(is_winner):
                play_game = False
                get_board(board)
                print('Drawn game')
                break

        print(board)
        get_board(board)
        print(turn)