#- - - Password generator - - -
#By: Susllike

import random

FILENAME = "words.txt"
CHARACTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+,./[]{}~`'")

with open(FILENAME) as file_object:
	LINES = file_object.readlines()

def weak_password():
	"""Generates a password from 1 to 3 words, separated by '_'."""
	password = ""
	for _ in range(random.randint(2, 4)):
		password += random.choice(LINES).strip()+"_"
	return password

def medium_password():
	"""Generates a password from 4 to 7 pieces, with each piece being either a character or a word, separated by either nothing or '_'."""
	big_list = [LINES, CHARACTERS]
	password = ""
	for _ in range(random.randint(4, 7)):
		list_choice = random.choice(big_list)
		password += random.choice(list_choice).strip() + random.choice(["", "_", "-"])
	return password

def strong_password(length):
	"""Generates a password just from individual characters, with the length of 30 or more."""
	password = ""
	for _ in range(length):
		password += random.choice(CHARACTERS)
	return password

print("--- Password generator ---")

while True:
	strength = input("What kind of password would you like?\n'w' = weak\n'm' = medium strength\n's' = strong\n> ").lower()
	if strength == "w" or strength == "weak":
		print(f"Here is your password: {weak_password()}")
		quit()
	elif strength == "m" or strength == "medium":
		print(f"Here is your password: {medium_password()}")
		quit()
	elif strength == "s" or strength == "strong":
		while True:
			length = input("How long do you want it to be? ")
			try:
				length = int(length)
			except:
				print("Invalid input, please try again.")
				continue

			if length < 30:
				print("Weak or medium password option is recommended for that length.")
				break
			else:
				print(f"Here is your password: {strong_password(length)}")
				quit()