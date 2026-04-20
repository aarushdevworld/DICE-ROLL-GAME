from roll import roll_dice
def multiplayer():
    print("Multiplayer mode selected.")
    player1_name = input("Enter name for Player 1: ")
    player2_name = input("Enter name for Player 2: ")
    print(f"{player1_name} and {player2_name}, get ready to roll the dice!")
    while True:
        input(f"{player1_name}, press Enter to roll the dice...")
        player1_roll = roll_dice() 
        print(f"{player1_name} rolled a {player1_roll}!")
        input(f"{player2_name}, press Enter to roll the dice...")
        player2_roll = roll_dice()
        print(f"{player2_name} rolled a {player2_roll}!")
        if player1_roll > player2_roll:
            print(f"{player1_name} wins!")
        elif player2_roll > player1_roll:
            print(f"{player2_name} wins!")
        else:
            print("It's a tie!")
        play_again = input("Do you want to play again? (yes(y)/no(n)): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break