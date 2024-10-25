signDictionary = []
for i in range(9):
    signDictionary.append(' ')

def print_board():
    board = f"""
     {signDictionary[0]} | {signDictionary[1]} | {signDictionary[2]}
    ---|---|---
     {signDictionary[3]} | {signDictionary[4]} | {signDictionary[5]} 
    ---|---|---
     {signDictionary[6]} | {signDictionary[7]} | {signDictionary[8]} 
    """
    print(board)

index_list = []
def take_input(playerName):
    while True:
        x = int(input(f'{playerName}: '))
        x -= 1
        if 0 <= x < 10:
            if x in index_list:
                print('This spot is blocked')
                continue
            index_list.append(x)
            return x
        print('Please enter a valid number between 1 and 9')

def calculate_result(player_1, player_2):
    if signDictionary[0] == signDictionary[1] == signDictionary[2] == 'X' or signDictionary[3] == signDictionary[4] == signDictionary[5] == 'X' or signDictionary[6] == signDictionary[7] == signDictionary[8] == 'X' or signDictionary[0] == signDictionary[3] == signDictionary[6] == 'X' or signDictionary[1] == signDictionary[4] == signDictionary[7] == 'X' or signDictionary[2] == signDictionary[5] == signDictionary[8] == 'X' or signDictionary[0] == signDictionary[4] == signDictionary[8] == 'X' or signDictionary[2] == signDictionary[4] == signDictionary[6] == 'X':
        print(f'{player_1} wins!')
        quit('Thank you for playing the game!')
    elif signDictionary[0] == signDictionary[1] == signDictionary[2] == 'O' or signDictionary[3] == signDictionary[4] == signDictionary[5] == 'O' or signDictionary[6] == signDictionary[7] == signDictionary[8] == 'O' or signDictionary[0] == signDictionary[3] == signDictionary[6] == 'O' or signDictionary[1] == signDictionary[4] == signDictionary[7] == 'O' or signDictionary[2] == signDictionary[5] == signDictionary[8] == 'O' or signDictionary[0] == signDictionary[4] == signDictionary[8] == 'O' or signDictionary[2] == signDictionary[4] == signDictionary[6] == 'O':
        print(f'{player_2} wins!')
        quit('Thank you for playing the game!')

def main():
    print('Welcome to the tic tac toe game!')
    player_1 = input('Input your name for Player 1: ')
    player_2 = input('Input your name for Player 2: ')
    print(f'Thank you, {player_1} and {player_2}. Now, let\'s start playing!')
    
    print(f"{player_1}'sign will be - X")
    print(f"{player_2}'sign will be - O")
    print('Enter any key to start the game : ')

    print_board( )

    for i in range(9):
        if i % 2 == 0:
            index = take_input(player_1)
            signDictionary[index] = 'X'
        else:
            index = take_input(player_2)
            signDictionary[index] = 'O'

        print_board()
        calculate_result(player_1, player_2)

    print('This is a tie, nobody won!')
main()

