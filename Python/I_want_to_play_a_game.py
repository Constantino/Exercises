from sys import argv 
import random

options = {"piedra":1,"papel":2,"tijeras":3,1:"piedra",2:"papel",3:"tijeras"}
user_choice = 0

try:
	input_value = raw_input("Type your option: ").lower().strip()
	user_choice = options[input_value]

	computer_choice = random.randint(1,3)

	print "user: ",options[user_choice]
	print "computer: ",options[computer_choice]

	if user_choice==computer_choice:
		print "Empate"
	elif user_choice == 3 and computer_choice == 2:
		print "You win!"
	elif user_choice == 2 and computer_choice == 1:
		print "You win!"
	elif user_choice == 1 and computer_choice == 3:
		print "You win!"
	else:
		print "You lose!"

except:
	print "Invalid option."