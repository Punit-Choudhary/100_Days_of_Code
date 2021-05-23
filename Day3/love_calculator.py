# Love Calculator

"""
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.
"""

print("\3 \3 \3 \3 \3 \3 Love Calculator \3 \3 \3 \3 \3 \3 \3\n")

person1 = input("Enter your name: ").lower()
person2 = input("Enter his/her name: ").lower()

t = person1.count("t") + person2.count("t")
r = person1.count("r") + person2.count("r")
u = person1.count("u") + person2.count("u")
e = person1.count("e") + person2.count("e")

l = person1.count("l") + person2.count("l")
o = person1.count("o") + person2.count("o")
v = person1.count("v") + person2.count("v")


true = t + r + u + e
love = l + o + v + e

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your L\3ve score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your L\3ve score is {score}, you are alright together.")
else:
    print(f"Your L\3ve score is {score}.")