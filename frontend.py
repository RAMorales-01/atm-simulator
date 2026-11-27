import os
import time
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
	print("Welcome to your ATM simulation")
	username = input("Please enter your username: ").lower()

	if verify.verify_username(username): 
		return username
	else:
		return None

def pin_login(username):
	"""Takes input for PIN number associated to verified username."""
	# After 3 failed attempts to enter the correct pin, the program ends.
	attempts = 0
	max_attempts = 3 

	while attempts < max_attempts:
		clear_display()
		print(f"Please enter your pin number (Attempt {attempts + 1}/{max_attempts})")
		pin = input(": ")

		if verify.verify_pin(username, pin): # validates pin input associated to username. 
			clear_display()
			print("PIN verified successfully!")
			return True
		else: 
			attempts += 1
			remaining = max_attempts - attempts

			if remaining > 0:
				print(f"\nIncorrect PIN. You have {remaining} attempt(s) left.")
				time.sleep(3)

	clear_display()

	print("Maximum attempts reached. account blocked, please contact bank customer services.\n")
	return False

def transactions_screen(username):
	"""Displays operation options after username and pin has been validated"""
	while True:
		clear_display()
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
			clear_display()
			requested_op = operation.select_transaction(choice, username)
			print(f"-- {requested_op} -\n")
			input("Press ENTER to continue...")

	clear_display()
	print("Thank you for using your ATM, Have a nice day!\n")
	
