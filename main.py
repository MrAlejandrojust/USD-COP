import random


def main():
    print('''
___________________________
|                          |
|   Double Six Dice Game   |
|__________________________|
    ''')

    player_username1 = input('Please enter your Username: ')

    # Assignment Variables Player1
    dice1 = 0
    dice2 = 0
    count1 = 0

    # Player1 Number Of Attempts
    while dice1 & dice2 != 6:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        count1 = count1 + 1

    print(count1, 'attempts')

    player_username2 = input('Please enter your Username: ')

    # Assignment Variables Player2
    dice1 = 0
    dice2 = 0
    count2 = 0

    # Player2 Number Of Attempts
    while dice1 & dice2 != 6:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        count2 = count2 + 1

    print(count2, 'attempts')

    # Comparison, Winner Player
    if count1 > count2:
        print(player_username2, 'has won, you lucky')
    elif count1 == count2:
        print('Draw')
    else:
        print(player_username1, 'has won, you lucky')


if __name__ == '__main__':
    main()
