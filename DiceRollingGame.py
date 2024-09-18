import random

while True:

    dice = input("Roll the dice? (y/n) ").lower()
    if dice == 'y':
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print(f"({dice_1},{dice_2})")

    elif dice == 'n':
        print("Thanks For Playing")
        break

    else:
        print("INVALID INPUT")


    