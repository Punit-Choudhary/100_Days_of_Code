# main.py

"""
Hangman Game

main.py -- contains game logic.
"""

import random
import words
import art

word_list = words.word_list
stages = art.stages
logo = art.logo
choosen_word = random.choice(word_list)

print(logo)

lives = 6

display = []
for _ in range(len(choosen_word)):
    display.append("_")

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    if guess not in display:
      for index in range(len(choosen_word)):
        letter = choosen_word[index]
        
        if letter == guess:
          display[index] = guess
    else:
      print(f"You have already guessed {guess}")
    
    if guess not in choosen_word:
      lives -= 1
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      if lives == 0:
        print(f"You loose, it was {choosen_word}!")
        game_over = True
    
    print(' '.join(display))

    if "_" not in display:
        print("You win!")
        game_over = True
    
    print(stages[lives])