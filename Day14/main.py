# main.py -- contain code for Higher Lower game

import os
import random
from art import logo, vs
from game_data import data


def clear():
    '''function to clear screen'''
    _ = os.system("cls")


def get_data():
    '''Formats the data into printable format'''
    dict_ = random.choice(data)

    text = dict_['name'] + ', ' + dict_['description'] + ', from ' + dict_[
        'country']
    follower_count = dict_['follower_count']

    return text, follower_count


def get_answer(follower_A, follower_B, guess):
    '''Return boolean value after verifying the answer'''
    if follower_A > follower_B:
        return guess == 'A'
    else:
        return guess == 'B'


def play():
    clear()
    print(logo)
    game_active = True
    score = 0
    A, follower_A = get_data()
    B, follower_B = get_data()

    while game_active:
        A, follower_A = B, follower_B
        while B == A:
            B, follower_B = get_data()

        print(f"Compare A: {A}")
        print(vs)
        print(f"Compare B: {B}")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        is_correct = get_answer(follower_A, follower_B, guess)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_active = False
            print(f"Sorry, that's wrong. Final score: {score}")


play()
