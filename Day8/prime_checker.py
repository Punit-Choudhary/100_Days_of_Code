# Prime Checker

"""
Prime Number : Numbers that can only be cleanly divided by itself and 1.

"""
def prime_checker(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
    
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

number = int(input("Check this number: "))
prime_checker(number)