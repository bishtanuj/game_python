# import the required package
import random

# welcome message
print("**********************************************************************")
print("!! Welcome to the number guess game !!")

# Rules of the game
print("**********************************************************************")
print("RULE: If you guessed the right number than you will win else loose...")
print("**********************************************************************")

# save the random number in a variable
random_number = int(random.randint(1, 10))

# scanning the number input by the user
number = int(input("Guess and enter the number in range between 1 to 10: "))
if number < 0 or number > 10:
    print("Sorry! Kindly enter the number in range between 1 to 10")
else:
    print("Number guessed by computer:", random_number)
    if number == random_number:
        print("Congratulations!")
    else:
        print("Sorry! You loose")
