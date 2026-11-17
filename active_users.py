# active users to verified
active_users = {
	'alex': {
		'pin': '5683',
		'balance': 800.00,
		'history': []
		},
	'omar': {
		'pin': '5560',
		'balance':450.00,
		'history': []
		},
	'carlos': {
		'pin': '2308',
		'balance': 399.00,
		'history': []
		},
	'israel': {
		'pin': '5613',
		'balance': 2000.00,
		'history': []
		}
}

# For testing purpose only.
if __name__ == "__main__":
	for outer_key, inner_dict in active_users.items():
		print("========================")
		print(f"{outer_key.title()}: \n")

		for inner_key, value in inner_dict.items():
			print(f"{inner_key.title()}: {value}")
		print("\n")
