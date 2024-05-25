import random


def rolldice():
    dice_dict = {
        1:("---",
           "-1-",
           "---",),
        2:("---",
           "-2-",
           "---",),
        3:("---",
           "-3-",
           "---",),
        4:("---",
           "-4-",
           "---",),
        5:("---",
           "-5-",
           "---",),
        6:("---",
           "-6-",
           "---",)
        }
    roll = input(" roll dice ?? tes or no")

    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)

        print("dice roller {} and {}".format(dice1,dice2))
        print("\n".join(dice_dict[dice1]))
        print("\n".join(dice_dict[dice2]))

        roll = input("roll again ???")

    
