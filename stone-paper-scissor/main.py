rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
me = 0
pc = 0
while me < 5 and pc < 5:
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    a = int(input())
    if a == 0:
        print(rock)
    elif a == 1:
        print(paper)
    else:
        print(scissors)
    import random

    print("Computer chose:")
    b = random.randint(0, 2)
    if b == 0:
        print(rock)
    elif b == 1:
        print(paper)
    else:
        print(scissors)
    if (a == 0 and b == 0):
        print("Its a draw")
    elif (a == 0 and b == 1):
        print("You lose")
        pc = pc + 1
    elif (a == 0 and b == 2):
        print("You win")
        me = me + 1
    elif (a == 1 and b == 0):
        print("You win")
        me = me + 1
    elif (a == 1 and b == 1):
        print("Its a draw")
    elif (a == 1 and b == 2):
        print("You lose")
        pc = pc + 1
    elif (a == 2 and b == 0):
        print("You lose")
        pc = pc + 1
    elif (a == 2 and b == 1):
        print("You win")
        me = me + 1
    elif (a == 2 and b == 2):
        print("Its a draw")
    print(f"Your score is {me} and computer score is {pc}\n")
print(f"Game Over!\nFinal Results\nme = {me}\ncomputer = {pc}")
if me == 5:
    print("You win the game")
else:
    print("You lose the game")
print("_")
print("The repl has exited")
1
