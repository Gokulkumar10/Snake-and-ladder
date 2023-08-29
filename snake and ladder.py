import random

b = [' ' for _ in range(1, 36)]


def display():
    print('\n\t# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('\t#       #       #       #       #       #       #       #       #       #  END  #')
    print(f'\t#   {b[21]}   #   {b[22]}   #   {b[23]}   #   {b[24]}   #   {b[25]}   #   {b[26]}   #   {b[27]}   #   {b[28]}   #   {b[29]}   #   {b[30]}   #')
    print('\t#  21   #  LT4  #  SH2  #  SH3  #  25   #  26   #  SH4  #  28   #  29   #   30  #')
    print('\t# ^ ^ ^ # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #')
    print('\t#       #       #  LH4  #       #       #  ST4  #       #       #       #       #')
    print(f'\t#   {b[20]}   #   {b[19]}   #   {b[18]}   #   {b[17]}   #   {b[16]}   #   {b[15]}   #   {b[14]}   #   {b[13]}   #   {b[12]}   #   {b[11]}   #')
    print('\t#  20   #  19   #  18   #  SH1  #  LT1  #  15   #  LT2  #  13   #  12   #  LT3  #')
    print('\t# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ^ ^ ^ #')
    print('\t#       #  ST1  #       #  LH1  #  ST2  #       #  ST3  #  LH2  #  LH3  #       #')
    print(f'\t# START #   {b[2]}   #   {b[3]}   #   {b[4]}   #   {b[5]}   #   {b[6]}   #   {b[7]}   #   {b[8]}   #   {b[9]}   #   {b[10]}   #')
    print('\t#   1   #   2   #   3   #   4   #   5   #   6   #   7   #   8   #   9   #   10  #')
    print('\t# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #\n')


def dice():
    num = 0
    dice1 = input('Rotate the dice by enter r: ')
    if dice1 == 'r':
        num = random.randint(1, 6)
    else:
        print("Enter the r for rotate the dice.")
        dice()
    return num


def snake_ladder(c):
    snakes1 = [17, 23, 24, 27]
    snakes2 = [2, 5, 7, 15]
    ladders1 = [4, 8, 9, 18]
    ladders2 = [16, 14, 11, 22]
    if c in snakes1:
        i = snakes1.index(c)
        c = snakes2[i]
        print(f'\n!!!Player byte by snake so, start at Position {c} !!!')
    if c in ladders1:
        i = ladders1.index(c)
        c = ladders2[i]
        print(f'\n"""Player got a ladder so, up at Position {c}"""')
    return c


def player1(c):
    print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
    print('...Player 1 turn...')
    dice_num = dice()
    prev = c
    c += dice_num
    c = snake_ladder(c)
    b[prev] = ' '
    if c <= 30:
        b[c] = 'A'
        display()
        print(f'Dice = {dice_num}')
        print('Player 1 in Position: {}'.format(c))
        return c
    else:
        print('Range out of Board...')
        print(f'Dice = {dice_num}')
        b[prev] = 'A'
        display()
        return prev

def player2(d):
    print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
    print('\n...Player 2 turn...')
    dice_num = dice()
    print(f'Dice = {dice_num}')
    prev = d
    d += dice_num
    d = snake_ladder(d)
    b[prev] = ' '
    if d <= 30:
        b[d] = 'B'
        display()
        print(f'Dice = {dice_num}')
        print('Player 2 in Position: {}'.format(d))
        return d
    else:
        print('Range out of Board...')
        b[prev] = 'B'
        display()
        print(f'Dice = {dice_num}')
        return prev


if __name__ == '__main__':
    display()
    print('Player 1 as A in 1')
    print('Player 2 as B in 1')
    c = 1
    d = 1
    while True:
        prev1, prev2 = c, d
        c = player1(c)
        if c == 30:
            print(':::Player 1 is a Winner:::')
            break
        d = player2(d)
        if d == 30:
            print(':::Player 2 is a Winner:::')
            break
        # when clash
        if c == d:
            print('\n!!! Clashed !!!')
            if prev1 < prev2:
                d = 1
                b[d] = 'B'
                print('Player 2 start at 1')
            else:
                c = 1
                b[c] = 'A'
                print('Player 1 start at 1')
