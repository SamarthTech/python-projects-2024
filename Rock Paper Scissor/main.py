import random

def display_instructions():
    print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
          + "Rock vs Paper -> Paper wins\n"
          + "Rock vs Scissors -> Rock wins\n"
          + "Paper vs Scissors -> Scissors wins\n")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice:\n1 - Rock\n2 - Paper\n3 - Scissors\n"))
            if choice in [1, 2, 3]:
                return choice
            print('Enter a valid choice please ☺:')
        except ValueError:
            print('Invalid input. Please enter a number.')

def get_computer_choice():
    return random.randint(1, 3)

def get_choice_name(choice):
    return {1: 'Rock', 2: 'Paper', 3: 'Scissors'}[choice]

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "DRAW"
    if (user_choice == 1 and comp_choice == 2) or (user_choice == 2 and comp_choice == 1):
        return 'Paper'
    if (user_choice == 1 and comp_choice == 3) or (user_choice == 3 and comp_choice == 1):
        return 'Rock'
    if (user_choice == 2 and comp_choice == 3) or (user_choice == 3 and comp_choice == 2):
        return 'Scissors'
    return get_choice_name(user_choice)

def play_game():
    display_instructions()
    while True:
        user_choice = get_user_choice()
        user_choice_name = get_choice_name(user_choice)
        print('User choice is:', user_choice_name)
        
        comp_choice = get_computer_choice()
        comp_choice_name = get_choice_name(comp_choice)
        print("Computer choice is:", comp_choice_name)
        print(user_choice_name, 'vs', comp_choice_name)

        result = determine_winner(user_choice, comp_choice)

        if result == "DRAW":
            print("<== It's a tie! ==>")
        elif result == user_choice_name:
            print("<== User wins! ==>")
        else:
            print("<== Computer wins! ==>")

        if input("Do you want to play again? (Y/N) ").lower() == 'n':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
