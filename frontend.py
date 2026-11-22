import os
from enum import StrEnum
import user_verification as verify

class Option(StrEnum):
	DEPOSIT = "1"
	WITHDRAW = "2"
	BALANCE = "3"
	EXIT = "4"

def clear_display():
	"""Clears terminal display"""
	os.system('cls' if os.name == 'nt' else 'clear')

def username_login():
	"""Takes input for username login"""
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

	while attempts < max_attempts:
		print(f"\nPlease enter your pin number (Attempt {attempts + 1}/{max_attempts})")
		pin = input(": ")

		if verify.verify.pin(username, pin): # validates pin input belongs to the registered username. 
			print("PIN verified successfully!")
			return True
		else: # if pin input is typed wrong or is incorrect.
			attempts += 1
			remaining = max_attempts + attempts

			if remaining > 0:
				print(f"Incorrect PIN. You have {remaining} attempt(s) left.")

	print("\nMaximum attempts reached. Session terminated, please contact bank security.")
	return False

def transactions_screen(username):
	"""Displays operation options after username and pin has been validated"""
	clear_display()
	print(f"User: {username.title()}\n")
	print(
		f"{Option.DEPOSIT}1- Deposit\n"
		f"{Option.WITHDRAW}2- Withdraw\n"
		f"{Option.BALANCE}3- Check balance\n"
		f"{Option.EXIT}4- Exit"
	)

	return input(": ")


	
