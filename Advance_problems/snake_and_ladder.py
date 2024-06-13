import random


def roll_dice():
    return random.randint(1,6)
def game():
    player_position=0
    dice_value=roll_dice()
    player_position=dice_value
    return player_position


if __name__ == '__main__':
    print(game())
