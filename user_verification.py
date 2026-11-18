import active_users as username

def verify_username(username_input):
	"""Verify if the typed username is among registered users"""
	if username_input.lower() in username.active_users:
		return True
	else:
		return False

