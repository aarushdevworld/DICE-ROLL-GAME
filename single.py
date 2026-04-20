import random as r
from roll import roll_dice
def single_player():
    while True:
        print("Single Player mode selected.")
        dice_value = roll_dice()
        print(f"You rolled a {dice_value}!")
        play_again = input("Do you want to play again? (yes(y)/no(n)): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break