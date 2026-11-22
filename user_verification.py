import active_users as users

def verify_username(username_input):
	"""Verify if the typed username is among registered users"""
	return username_input.lower() in users.active_users

def verify_pin(username_input, pin_input):
	"""Verify if the typed pin number is matches with the registered username"""
	correct_pin = users.active_users[username_input]['pin']
	return pin_input == correct_pin
