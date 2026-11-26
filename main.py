import time
import frontend as transaction

def main():
	"""Begins the simulation for an ATM basic transactions"""
	# First search for the username exists in the dictionary
	current_user = transaction.username_login()

	if current_user:
		# Once the username has been validated successfully, next step is to validate the pin linked to the username.
		if transaction.pin_login(current_user):
			print(f"Welcome {current_user.title()}! now loading main menu...\n")
			time.sleep(3)
			transaction.transactions_screen(current_user)
	else:
		print("\nTyped username is not registered in our database.\n")

if __name__ == "__main__":
	main()
