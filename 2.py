import random


def rolling_a_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("First number is ", dice1)
    print("Second number is", dice2)
    dice3 = dice1+dice2
    return dice3

def playing_a_game():
    rolling = rolling_a_dice()
    if rolling == 7 or rolling == 11:
        print("You are a winner! The sum of the dice is ", rolling)
        return True

    elif rolling == 2 or rolling == 3 or rolling == 12:
        print ("You are losing! The sum of dice is ", rolling)
        return False

    else:
        print("The sum of dice is", rolling, "This is your goal nuber. ")
        goal = rolling
        while True:
            rolling = rolling_a_dice()
            if rolling == goal:
                print("You are a winner! The sum of the dice is",rolling)
                return True
            elif rolling == 7:
                print ("You are losing! The sum of dice is ", rolling)
                return False
            else:
                print("The sum of dice is", rolling, "Please roll again. ")

playing_a_game()