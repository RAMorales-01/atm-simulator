import user_verification as verify

def main():
	print("Welcome to your ATM")
	username = input("Please type your username: ")

	if verify.verify_username(username):
		print(f"\nWelcome {username}!")
	else:
		print("\nSorry it seems that your username is not correct, please try again.")

if __name__ == "__main__":
	main()
