import random

value_AI = random.randint(1,101)#let computer pick a random number
guess_Human = None
attempt = 0#keep the number of attempts to guess the number

while guess_Human != value_AI:
	guess_Human = int(input("Type your guess between 1 and 100:\n"))

	if type(guess_Human) == int:
		guess_Human = int(guess_Human)

	if guess_Human == value_AI:
		print("Congratz !")
	elif guess_Human < value_AI:
		print("My number is bigger, try again..")
	else: 
		#guess_Human > value_AI
		print("I have something smaller in my mind, try again..")
	attempt += 1
	

print("It took you " + str(attempt) + " tries to find it.")
