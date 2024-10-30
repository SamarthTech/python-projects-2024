import random
from words_and_steps import hangman_steps, word_list


chosen_word= random.choice(word_list)


word_to_choose= '_' * len(chosen_word)
word_to_choose_list= list(word_to_choose)

print(f"Word to choose: {word_to_choose}")

index=0
while  "_" in word_to_choose_list and index < len(hangman_steps) - 1 :
    letter= input("Guess a letter: ")    
    matched= False
    for each in range(len(chosen_word)):
        if chosen_word [each] == letter:
            word_to_choose_list [each] = letter
            matched= True

    if matched == False:
        index+=1 
    
    new_str= ''.join(word_to_choose_list)
    print(f"Word to choose: {new_str} ")
    print(hangman_steps[index])
    print(f"*******You're left with {5 - index}/6 steps********")



if index == len(hangman_steps) - 1:
    print(f"****No Steps Are Left!!!You Loose A Life! The Exact Word Was '{chosen_word}'****")
else:


    print("***You Win!!!***")
