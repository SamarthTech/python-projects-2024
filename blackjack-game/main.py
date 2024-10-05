import random

cards= [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand= []
dealer_hand= []

def card_dist():
    for _ in range (2):
        player_hand.append(random.choice(cards))
        dealer_hand.append(random.choice(cards))

def calc_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if sum(hand) > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def result(player_score , dealer_score):
    if player_score == dealer_score:
        print("THE GAME IS DRAW!!! 😊")
    elif dealer_score == 0:
        print("BLACKJACK!!! Dealer wins!! 🥺")
    elif player_score == 0:
        print("BLACKJACK!!! YOU WIN 1.5 X YOUR BET!! 🤩")
    elif player_score > 21:
        print("YOU EXCEED 21!!You loose your bet! 😭")
    elif dealer_score > 21:
        print("DEALER EXCEEDS 21!!You win your bet! 🥳")
    elif player_score > dealer_score:
        print("YOU WIN YOUR BET!!!! 🥳")
    else:
        print("YOU LOOSE YOUR BET!!!! 😭")


def play_game():
    card_dist()
    gameover= False
    while not gameover:
        player_score = calc_score(player_hand)
        print(f"Your cards: {player_hand}. Total in your hand: {player_score}")
        print(f"Dealer's first hand has: {dealer_hand[0]} ")
        if player_score > 21 or player_score == 0:
            gameover= True
        else: 
            dis= input("Wish to add card? Type 'y'! If not? Type 'n'!\n").lower()
            if dis == 'y':
                player_hand.append(random.choice(cards))
            else:
                gameover= True

    dealer_score= calc_score(dealer_hand)
    while dealer_score != 0 and dealer_score <= 17:
        dealer_hand.append(random.choice(cards))
        dealer_score= calc_score(dealer_hand)
    print(f"Dealer's final hand is {dealer_hand}. Total in his hand: {dealer_score}")
    result(player_score, dealer_score)

dis= input("Play balckjack game?: 'y' for continue or 'n' for not:\n")
while dis == 'y':
    play_game()
    dis= input("Play balckjack game?: 'y' for continue or 'n' for not:\n")
    dealer_hand= []
    player_hand= []



    






    


