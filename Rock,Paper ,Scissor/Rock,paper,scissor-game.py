#Rock paper scissor game
import random

choices=["rock","paper","scissor"]

running=True
while running:

    computer=random.choice(choices)
    play =None
    while play not in choices:
        play=input("rock, paper or scissor?").lower()

    print("computer: "+computer)
    print("player: "+play)

    if play==computer:
        print("tie")
    elif play=="rock":
        if computer == "scissor":
            print("You win")
        if computer == "paper":
            print("Computer wins")
    elif play=="scissor":
        if computer=="rock":
            print("Computer wins")
        if computer=="paper":
            print("You win")
    elif play=="paper":
        if computer=="rock":
            print("You win")
        if computer=="scissor":
            print ("Computer wins")

    if not input("Play again?(y/n):").lower()=="y":
        running=False

print("Thank you for playing!")

