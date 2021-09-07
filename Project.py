# import random module
import random

#Introduction to the "rules" of the game
print("Winning Rules of the Rock paper scissor game as follows:")
print("Rock vs paper: paper wins")
print("Rock vs scissor: Rock wins")
print("paper vs scissor: scissor wins")

#Let's Play
while True:
	print("Enter choice:")
	print("1. Rock")
	print("2. paper")
	print("3. scissor")
	
	# take the input from user
	choice = int(input("User turn: "))

	# looping until user enter invalid input
	while choice > 3 or choice < 1:
		choice = int(input("\n\n\t\t\t!! Enter Valid Input !!"))
		

	# initialize value of choice_name variable
	# corresponding to the choice value
	if choice == 1:
		choice_name = 'Rock'
	elif choice == 2:
		choice_name = 'paper'
	else:
		choice_name = 'scissor'
		
	# print user choice
	print("User Choice: " + choice_name)
	print("\n\nComputer Turn.......")

	# Computer chooses randomly any number
	# among 1 , 2 and 3. Using randint method
	# of random module
	comp_choice = random.randint(1, 3)
	
	# looping until comp_choice value
	# is equal to the choice value
	while comp_choice == choice:
		comp_choice = random.randint(1, 3)

	# initialize value of comp_choice_name
	# variable corresponding to the choice value
	if comp_choice == 1:
		comp_choice_name = 'Rock'
	elif comp_choice == 2:
		comp_choice_name = 'paper'
	else:
		comp_choice_name = 'scissor'
		
	print("Computer Choice: " + comp_choice_name)

	print(choice_name + " V/s " + comp_choice_name)

	# condition for winning
	if((choice == 1 and comp_choice == 2) or
	(choice == 2 and comp_choice ==1 )):
		print("\npaper wins! ", end = "")
		result = "paper"
		
	elif((choice == 1 and comp_choice == 3) or
		(choice == 3 and comp_choice == 1)):
		print("\nRock wins! ", end = "")
		result = "Rock"
	else:
		print("\nscissor wins! ", end = "")
		result = "scissor"

	# Printing either user or computer wins
	if result == choice_name:
		print("\n\nUser wins :) HURRAY!! " + "\nWell Done!")
	else:
		print("\n\nComputer wins")
		print("Let's play once again!")
		
	print("Do you want to play again? (Y/N)")
	ans = input()


	# if user input n or N then condition is True
	if ans == 'n' or ans == 'N':
		break
	
# after coming out of the while loop
# we print thanks for playing
print("\nThanks for playing!" + " Hope you enjoyed it :) ")
