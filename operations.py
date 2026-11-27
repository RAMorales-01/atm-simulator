import active_users as users

def select_transaction(selected_option, username):
    """Main hall for operations"""
    # Verify if user input is a valid option.
    # if it is valid, then linked func is called.
    action = actions.get(selected_option)
    
    if action:
        return action(username)
    else:
        return "invalid option."
    
def get_valid_amount(prompt):
    """Validates that typed amount is a positive number"""
    try:
        amount = float(input(prompt))
        
        if amount <= 0:
            return None
        else:
            return amount
    except ValueError:
        return None

def deposit(username):
    """Let the user add money to his/her balance"""
    amount = get_valid_amount("Please type the amount you wish to deposit: ")
    if not amount:
        return "Invalid amount. Please enter a positive number."
    
    users.active_users[username]['balance'] += amount
    users.active_users[username]['history'].append("deposit")
    return f"Deposit was successful. New Balance: {users.active_users[username]['balance']:.2f}"

def withdraw(username):
    """Let the user withdraw money form his/her balance"""
    amount = get_valid_amount("Please type the amount you wish to withdraw: ")
    if not amount:
        return "Invalid amount. Please enter a positive number."

    if amount > users.active_users[username]['balance']:
        return "!Insufficient funds.\n"
    
    users.active_users[username]['balance'] -= amount
    users.active_users[username]['history'].append("withdraw")
    return f"Withdraw was successful. New Balance: {users.active_users[username]['balance']:.2f}"    

def check_balance(username):
    """Let user see his/her current balance"""
    return f"Current balance: {users.active_users[username]['balance']:.2f}"

def check_transaction_history(username):
    """Shows to the user all the recent operations"""
    return f"Recent Transacctions: {users.active_users.get(username, {}).get('history', [])}"

actions = {
    "1": deposit,
    "2": withdraw,
    "3": check_balance,
    "4": check_transaction_history,
}
