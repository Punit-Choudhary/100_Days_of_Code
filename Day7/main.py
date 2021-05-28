# main.py

"""
Hangman Game

main.py -- contains game logic.
"""

import random


word_list = ['apple', 'ball', 'camel']
choosen_word = random.choice(word_list)

print(f"Choosen word is {choosen_word}.")

lives = 6

display = []
for _ in range(len(choosen_word)):
    display.append("_")

game_over = False

while not game_over:
    print(stages[lives])
    guess = input("Guess a letter: ").lower()

    for index in range(len(choosen_word)):
        letter = choosen_word[index]
    
        if letter == guess:
            display[index] = guess
    
    print(''.join(display))
    
    if guess not in choosen_word:
      lives -= 1
      print("You guessed it wrong")
      if lives == 0:
        print(f"You loose, it was {choosen_word}!")
        game_over = True

    if "_" not in display:
        print("You win!")
        game_over = True