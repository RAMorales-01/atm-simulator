import frontend as transaction
import operations as operation

def main():
	"""Begins the simulation for an ATM basic transactions"""
	current_user = transaction.username_login()

	if current_user:
		# Once the username has been validated successfully, next step is to validate the pin linked to the username.
		if transaction.pin_login(current_user):
			print(f"Welcome {current_user.title()}! now loading main menu...\n")
			
			while True:
				choice = transaction.transactions_screen(current_user)

				print(choice)

	else:
		print("\nTyped username is not registered in our database. Please contact the bank services to open an account.\n")

if __name__ == "__main__":
	main()
