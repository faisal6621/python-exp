import random

# 1: The if-else statement
x = int(input("Please enter an integer: "))
if x >= 0:  # notice no parentheses
    print(x, "is a positive number")
else:
    print(x, "is a negative number")

# 2: if-elif-else. The keyword 'elif' is short for 'else if'
randint = random.randint(1, 10)
guess = int(input("Guess a number 1 to 10: "))
if guess > randint:
    print("Your guess is higher")
elif guess < randint:
    print("Your guess is lower")
else:
    print("You guessed it right")
