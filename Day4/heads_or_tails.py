# Heads or Tails

"""
Python program to tell Heads or Tails randomly.
"""

from random import randint

a = randint(0, 1)

if a == 0:
    print("Tails")
else:
    print("Heads")