import active_users as users

def select_transaction(selected_option, username):
    """Main connection for the operations"""
    action = actions.get(selected_option)
    
    if action:
        return action(username)
    else:
        return "invalid option."

def deposit(username):
    """Let the user add money to his/her balance"""
    print("\nPlease type the amount you wish to deposit")
    amount = int(input(": "))

    current_balance = users.active_users[username]['balance']
    new_balance = current_balance + amount
    users.active_users[username]['history'].append("deposit")
    return new_balance

def withdraw(username):
    """Let the user withdraw money form his/her balance"""
    print("\nPlease type the amount you wish to withdraw")
    amount = int(input(": "))

    current_balance = users.active_users[username]['balance']

    if amount > current_balance:
        return "!Insufficient funds.\n"
    else:
        users.active_users[username]['balance'] -= amount
        users.active_users[username]['history'].append("withdraw")
        return f"Withdraw was successful. New Balance: {users.active_users[username]['balance']}"    

def check_balance(username):
    """Let user see his/her current balance"""
    current_balance = users.active_users[username]['balance']
    return current_balance

def check_transaction_history(username):
    """Shows to the user all the recent operations"""
    return users.active_users.get(username, {}).get('history', [])

actions = {
    "1": deposit,
    "2": withdraw,
    "3": check_balance,
    "4": check_transaction_history,
}
