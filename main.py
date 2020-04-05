#This is a tictactoe game

board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

maru = '○'
batsu = '☓'


def display_board():
    print(board[0], '|', board[1], '|', board[2], '|')
    print('-----------')
    print(board[3], '|', board[4], '|', board[5], '|')
    print('-----------')
    print(board[6], '|', board[7], '|', board[8], '|')
    print('\n')


display_board()
count_turn = 0
count_0 = 0
count_x = 0
match = True


# def match_check(list_check):
#     # for 0; 3 combinations
#     if 0 in list_check:
#         if 1 in list_check:
#             if 2 in list_check:
#                 print(list_check)
#                 print('you win')
#                 return False
#         if 3 in list_check:
#             if 6 in list_check:
#                 print(list_check)
#                 print('you win')
#                 return False
#
#         if 4 in list_check:
#             if 8 in list_check:
#                 print(list_check)
#                 print('you win')
#                 return False
#
#     if 1 in list_check:
#         if 4 in list_check:
#             if 7 in list_check:
#                 print(list_check)
#                 print('you win')
#                 return False
#
#     if 2 in list_check:
#         if 4 in list_check:
#             if 6 in list_check:
#                 print(list_check)
#                 print('you win')
#                 return False
#         if 5 in list_check:
#             if 8 in list_check:
#                 print(list_check)
#                 print('you win')
#                 return False
#
#     if 3 in list_check:
#         if 4 in list_check:
#             if 5 in list_check:
#                 print(list_check)
#                 print('you win')
#                 return False
#
#     if 6 in list_check:
#         if 7 in list_check:
#             if 8 in list_check:
#                 print(list_check)
#                 print('you win')
#                 return False
#     else:
#         return True
def match_check(list_check,player_turn):
    # 1
    if 0 in list_check and 1 in list_check and 2 in list_check:
        print(list_check)
        print('Player ' + player_turn + ' win')
        return False
    # 2
    if 0 in list_check and 3 in list_check and 6 in list_check:
        print(list_check)
        print('Player ' + player_turn + ' win')
        return False
    # 3
    if 0 in list_check and 4 in list_check and 8 in list_check:
        print(list_check)
        print('Player ' + player_turn + ' win')
        return False
    # 4
    if 1 in list_check and 4 in list_check and 7 in list_check:
        print(list_check)
        print('Player ' + player_turn + ' win')
        return False
    # 5
    if 2 in list_check and 4 in list_check and 6 in list_check:
        print(list_check)
        print('Player ' + player_turn + ' win')
        return False
    # 6
    if 2 in list_check and 5 in list_check and 8 in list_check:
        print(list_check)
        print('Player ' + player_turn + ' win')
        return False
    # 7
    if 3 in list_check and 4 in list_check and 5 in list_check:
        print(list_check)
        print('Player ' + player_turn + ' win')
        return False
    # 8
    if 6 in list_check and 7 in list_check and 8 in list_check:
        print(list_check)
        print('Player ' + player_turn + ' win')
        return False

    else:
        return True


def match_point(count, player_value):
    if count >= 3:
        list_check = []
        if player_value == maru:
            player_turn = '1'
        else:
            player_turn = '2'

        for i, j in enumerate(board):
            if j == player_value:
                list_check.append(i)

        return match_check(list_check, player_turn)

    else:
        return True


def spot_check(spot):
    if board[spot] == maru or board[spot] == batsu:
        print('Enter to different spot')
        return True
    else:
        return False


def reset_board():
    b = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]
    return b


while match:
    if match:
        if count_turn % 2 == 0:
            spot_0 = True
            while spot_0:
                ino = int(input('Player 1 : '))
                spot_0 = spot_check(ino)
                if spot_0 is not True:
                    board[ino] = maru
                    count_0 += 1
                    count_turn += 1
                    display_board()
                    match = match_point(count_0, maru)

        else:
            spot_x = True
            while spot_x:
                inx = int(input('Player 2 : '))
                spot_x = spot_check(inx)
                if spot_x is not True:
                    board[inx] = batsu
                    count_x += 1
                    count_turn += 1
                    display_board()
                    match = match_point(count_x, batsu)

    if not match:
        print('Do you want to continue game?')
        in_game = input('Enter q to quit game : ')
        if in_game != 'q':
            count_turn = 0
            count_0 = 0
            count_x = 0
            match = True
            board = reset_board()
            display_board()
