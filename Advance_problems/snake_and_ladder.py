import random


def roll_dice():
    return random.randint(1,6)

def check_options():
    return random.choice(['No play','Ladder','Snake'])

def game():
    player_position=0
    dice_value=roll_dice()
    options=check_options()
    if(options=='No play'):
        pass
    elif(options=='Ladder'):
        player_position+=dice_value
    else:
        player_position-=dice_value
    if(player_position<0):
        player_position=0
    return player_position


if __name__ == '__main__':
    print(game())
