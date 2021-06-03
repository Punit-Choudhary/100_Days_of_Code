# BlackJack Game main file

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import art
import os

logo = art.logo

def clear():
    _ = os.system("cls")

def deal_card():
    '''Returns a random card from deck!'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def compare(user_score, computer_score):
    '''Compare score of user and computer and declare the winner'''
    if user_score > 21:
        return "You went over. You loose 😒"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has BlackJack 😱"
    elif user_score == 0:
        return "Win with a BlackJack 😎"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😠"

def calculate_score(cards):
    '''Returns score calculated from cards.'''

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)


def game():

    print(logo)

    user_cards = []
    computer_cards = []
    gameover = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not gameover:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\tYour cards: {user_cards}, current score: {user_score}")
        print(f"\tOpponent's first card: {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            gameover = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == 'y':
                user_cards.append(deal_card())
            else:
                gameover = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"\tYour final hand: {user_cards}, final score: {user_score}")
    print(f"\tOpponent's final hand: {computer_cards}, final score: {computer_score}")
    print(f"\n\t{compare(user_score, computer_score)}")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    game()