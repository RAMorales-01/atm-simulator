import os
from enum import StrEnum
import user_verification as verify
import operations as operation

class Option(StrEnum):
	DEPOSIT = "1"
	WITHDRAW = "2"
	BALANCE = "3"
	HISTORY = "4"
	EXIT = "5"

def clear_display():
	"""Clears terminal"""
	os.system('cls' if os.name == 'nt' else 'clear')

def username_login():
	"""Takes input for username login"""
	clear_display()

	print("Welcome to your ATM")
	username = input("Please enter your username: ").lower()

	if verify.verify_username(username): #if username is in the database, the same username is returned.
		return username
	else:
		return None

def pin_login(username):
	"""Takes input for PIN number associated to verified username, after 3 failed attempts program is terminated."""
	attempts = 0
	max_attempts = 3

	clear_display()

	print(f"Good day {username}")

	while attempts < max_attempts:
		print(f"Please enter your pin number (Attempt {attempts + 1}/{max_attempts})")
		pin = input(": ")

		if verify.verify_pin(username, pin): # validates pin input belongs to the registered username. 

			clear_display()

			print("PIN verified successfully!")
			return True
		else: # if pin input is typed wrong or is incorrect.
			attempts += 1
			remaining = max_attempts - attempts

			if remaining > 0:
				print(f"\nIncorrect PIN. You have {remaining} attempt(s) left.")

	clear_display()

	print("\nMaximum attempts reached. Session terminated, please contact bank security.\n")
	return False

def transactions_screen(username):
	"""Displays operation options after username and pin has been validated"""
	while True:
		print(f"Account holder: {username.title()}\n")
		print(
			f"{Option.DEPOSIT}- Deposit\n"
			f"{Option.WITHDRAW}- Withdraw\n"
			f"{Option.BALANCE}- Check balance\n"
			f"{Option.HISTORY}- Check transaction history\n"
			f"{Option.EXIT}- Exit"
		)
		
		choice = input("Select option: ")

		if choice == Option.EXIT:
			break
		else:
			requested_op = operation.select_transaction(choice, username)
			print(f"\n-- {requested_op} -\n")

	clear_display()
	print("\nThank you for using your ATM, Have a nice day!\n")
	
