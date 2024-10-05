import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ')
word = random.choice(someWords)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    for _ in word:
        print('_', end=' ')
    print()

    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    flag = 0

    try:
        while chances > 0 and flag == 0:
            print()
            chances -= 1

            guess = input('Enter a letter to guess: ').lower()
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            if guess in word:
                letterGuessed += guess

            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                else:
                    print('_', end=' ')

            if Counter(letterGuessed) == Counter(word):
                print("\nThe word is: ", word)
                flag = 1
                print('Congratulations, You won!')
                break

        if chances <= 0 and Counter(letterGuessed) != Counter(word):
            print('\nYou lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print('\nBye! Try again.')
