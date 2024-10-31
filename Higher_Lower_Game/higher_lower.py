import game_data
import random


def select_data():
    data_box= game_data.datas
    data_index = random.randint(0, len(data_box)-1)
    data= data_box[data_index]
    return data


def compare(dataA, dataB, guessing):
    first_follower= dataA["follower_count"]
    second_follower= dataB["follower_count"]
    if first_follower > second_follower:
        if guessing == 'higher':
            return True
        else:
            return False
    elif first_follower < second_follower:
        if guessing == 'lower':
            return True
        else:
            return False
      
def console_enemy(enemy):
    return f"{enemy['name']}, from {enemy['country']}\n description : {enemy['description']}"

def play():
    gameover=False
    score= 0
    dataB = select_data()

    while not gameover:
        dataA= dataB
        dataB= select_data()
        while dataA == dataB:
            dataB= select_data()
        print(f"ENEMY1:{console_enemy(dataA)}")
        print("V/S")
        print(f"ENEMY2:{console_enemy(dataB)}")

        guessing = input("\n'ENEMY1' is 'higher' or 'lower' than 'ENEMY2'?\n What are you guessing? ").lower()
        if guessing == 'higher' or guessing == 'lower':
            if not compare(dataA,dataB,guessing):
                gameover=True
                print("\n" * 100)
            else:
                score+=1
                print("\n" * 100)
                print(f"You're Right! Your score: {score}")
                
        else:
            print("\n" * 100)
            

    print(f"You're Wrong! Your score: {score}")

dis='y'
while dis == 'y':
    print("Welcome To HIGHER-LOWER Game!!")
    play()
    dis= input("Play again?: Type 'y' for yes 'n' for no").lower()
    print("\n" * 100)
