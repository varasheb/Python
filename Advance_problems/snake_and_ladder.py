import random

WINNING_POSITION = 100

def roll_dice():
    return random.randint(1, 6)

def check_options():
    return random.choice(['No play', 'Ladder', 'Snake'])

def game():
    players = [1, 2]
    player_positions = {1: 0, 2: 0}
    dice_rolls = {1: 0, 2: 0}
    player1_positions = [(0, 0)]
    player2_positions = [(0, 0)]
    winning_player = None

    while True:
        for player in players:
            while True:
                dice_value = roll_dice()
                options = check_options()
                dice_rolls[player] += 1

                if options == 'No play':
                    break
                elif options == 'Ladder':
                    if player_positions[player] + dice_value <= WINNING_POSITION:
                        player_positions[player] += dice_value
                        if player_positions[player] == WINNING_POSITION:
                            winning_player = player
                            break
                else:
                    player_positions[player] -= dice_value
                    if player_positions[player] < 0:
                        player_positions[player] = 0
                    break

                if player == 1:
                    player1_positions.append((dice_value, player_positions[player]))
                else:
                    player2_positions.append((dice_value, player_positions[player]))

        if winning_player:
            break

    if winning_player == 1:
        return 1, player1_positions, player2_positions, dice_rolls
    else:
        return 2, player1_positions, player2_positions, dice_rolls

if __name__ == '__main__':
    player1 = input('Enter the name of player 1: ')
    player2 = input('Enter the name of player 2: ')
    player, player1_positions, player2_positions, dice_rolls = game()
    print(f"Number of times dice was rolled for {player1} to win: {dice_rolls[1]}")
    print(f"Number of times dice was rolled for {player2} to win: {dice_rolls[2]}")
   
    if player == 1:
        print(f"{player1} won the game!")
    else:
        print(f"{player2} won the game!")
