import random

level_step = {
    'h': 5,
    'm': 10,
    'e': 15
}



def play():
    number= random.randint(1,100)
    while True :
        level= input("SELECT LEVEL:\ntype 'h' for HARD\n type 'm' for MIDIUM\ntype 'e' for EASY\n").lower()
        try:
            steps_granted= level_step[level]
            break
        except KeyError:
            print("Invalid Input!")

    print(steps_granted)
    for i in range(steps_granted, 0, -1):
        print(f"You have {i} attempts")
        while True:
            try :
                user_chose= int(input("Guess A Number: "))
                break
            except ValueError:
                print("Not a number! You're asked to guess a NUMBER!!!")

        if user_chose == number:
            return("CONGO!! you won!!!")
        elif user_chose > number:
            print("Guess lesser number")
        elif user_chose < number:
            print("Guess higher number")
        
    return f"You Loose!!!\n The exact number was {number}"
    

wish= input("WELCOME IN GUESS THE NUMBER GAME !!!\nStart play!\n'y' for continue or 'n' for not\n")
while wish == 'y':
    print(play())
    wish = input("RPLAY??\n'y' for continue or 'n' for not\n")

else:
    if wish == "n":
        print("Bye...")
    else:
        print("Invalid Input! Bye...")

