import random

# Scanning the lottery number
number = int(input("Enter a number between 1 and 10: "))

# Getting the winning number
winningNumber = random.randint(1, 10)

# Printing the lottery number of user
print("Your Number:", number)

# Printing the winning number with conclusion
print("The Winning Number:", winningNumber)
if number == winningNumber:
    print("Congratulations! You won.")
else:
    print("Better Luck Next Time!")
