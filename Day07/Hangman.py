import os
from Hangman_words import word_list
from Hangman_art import stages
from Hangman_art import logo
import random

print(logo)

chosen_word=random.choice(word_list)
chosen_word_len=len(chosen_word)

display=["_"]*chosen_word_len

lives=6

end_of_game=False

while not end_of_game:

    guess=input("Guess a letter:").lower()

    os.system('cls')

    print(logo)

    print(f"Your Guess: {guess}")

    if guess in display:
        print(f"You have already guessed {guess}, Please enter a different letter")

    for position in range(chosen_word_len):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter

    if guess not in chosen_word:
        print(f"{guess} is not in the letter, You lose a Life")
        lives-=1
        if lives==0:
            end_of_game=True
            print("You Lose")

    print(f' '.join(display))        

    if "_" not in display:
        end_of_game=True
        print("You Win")

    if lives<6:
        print(stages[lives])