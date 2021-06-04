# Guess the Number game

"""
Guess the Number Game
Levels : 'easy' -- 10 attempts
         'hard' -- 5  attempts
"""

import art
import  random

logo = art.logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def difficulty():
    choice = input("Choose difficulty. Type 'easy' or 'hard': ")
    
    if choice == 'easy':
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS


def check_answer(guess, number, attempts):
    '''Checks answer against user's guess. Returns the number of attempts remaining.'''
    if guess > number:
        print("Too High!")
        return attempts - 1
    elif guess < number:
        print("Too Low!")
        return attempts - 1
    else:
        print(f"You got it! The number was {number}.")

def game():
    print(logo)
    print("Welcome to the 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)

    attempts = difficulty()

    guess = 0

    while guess != number:
        print(f"You have {attempts} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, number, attempts)

        if attempts == 0:
            print("You've run out of guesses, you lose!")
        elif guess != number:
            print("Guess again!")

game()
