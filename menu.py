from single import single_player
from multi import multiplayer
def display_menu():
    while True:
        print("Welcome to FAAAHH! games - Please select a option:")
        print("1. Single Player"
              "\n2. Multiplayer"
              "\n3. Exit")
        choice= input("Enter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                print("Starting Single Player mode...")
                single_player()
                break
            elif choice == 2:
                print("Starting Multiplayer mode...")
                multiplayer()
                break
            elif choice == 3:
                print("Exiting the game. Goodbye!")
                exit()
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")