# Blind Auction

import art
import os

def clear():
    _ = os.system("cls")

logo = art.logo

print(logo)

close = False

bids = {}

def find_highest_bid(bids):
    highest = float('-inf')

    for name in bids:
        amount = bids[name]

        if amount > highest:
            highest = amount
            winner = name
    print(logo)
    print(f"The winner is {winner} with a bid of ₹{highest}")

while not close:
    name = input("What's your name? ")
    bid = int(input("Enter bid amount ₹"))

    bids[name] = bid

    choice = input("Are there any other bidders? Type 'yes' or 'no' ")

    if choice == "no":
        close = True
    clear()

find_highest_bid(bids)