import random

cards = ["Ace",2,3,4,5,6,7,8,9,10,"Joker","King","Queen"]
l = len(cards)

class Blackjack:

    def __init__(self):
        print("Welcome to Blackjack")
        self.a = [cards[random.randint(0,l-1)], cards[random.randint(0,l-1)]]
        self.d = [cards[random.randint(0,l-1)], cards[random.randint(0,l-1)]]
        self.sum = 0
        self.deal = 0
        print(f"You have : {self.a}")
        print(f"The dealer has : [{self.d[0]},something]")

    def calculate(self):
        for i in self.a:
            if i=="Ace" and self.sum<=11:
                self.sum+=11
            elif i=="Ace" and self.sum>11:
                self.sum+=1
            elif i=="Joker" or i=="King" or i=="Queen":
                self.sum+=10
            else:
                self.sum+=i

    def me(self):
        self.calculate()
        while self.sum<17:
            c= input("Press s for Stand / Press h for Hit : \n")
            if c=="s":
                print(f"The dealer has : {self.d}")
                break
            if c=="h":
                self.sum = 0
                self.a.append(cards[random.randint(0,l-1)])
                self.calculate()

        if self.sum == 21:
            print(f"You have : {self.a}")
            print("The match is yours. You hit a blackjack")
        elif self.sum>21:
            print(f"You have : {self.a}")
            print("You got busted loser")
        else:
            print("Your turn ends")
            self.dealing()

    def dealsum(self):
        for i in self.d:
            if i=="Ace" and self.deal<=11:
                self.deal+=11
            elif i=="Ace" and self.deal>11:
                self.deal+=1
            elif i=="Joker" or i=="King" or i=="Queen":
                self.deal+=10
            else:
                self.deal+=i

    def dealing(self):
        print(f"The dealer has : {self.d}")
        self.dealsum()
        while self.deal<17:
            self.d.append(cards[random.randint(0,l-1)])
            self.deal = 0
            self.dealsum()
            print(f"The dealer has : {self.d}")

        if self.deal == 21:
            print("You lost. The dealer hit a blackjack")
        elif self.deal>21:
            print("You won by luck. The dealer has been busted")
        else:
            print("Dealer turn ends")
            self.death_round()

    def death_round(self):
        if self.sum == self.deal:
            print("Money has been returned. It's a draw.")
        elif self.sum > self.deal:
            print("You won the round.")
        else:
            print("Haha. You lost it")

flag = True
while flag:
    user = Blackjack()
    user.me()
    choi = input("press y for playing again / press n for leaving the game: \n")
    if choi == "n":
        flag = False


