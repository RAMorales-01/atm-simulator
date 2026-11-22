import active_users as users

def deposit(username):
    """Let the user add money to his/her balance"""
    pass

def withdraw(username):
    """Let the user withdraw money form his/her balance"""
    pass

def check_balance(username):
    """Let user see his/her current balance"""
    current_balance = users.active_users[username]['balance']
    return current_balance

def check_transaction_history(username):
    """Shows to the user all the recent operations"""
    pass

def operations(current_balance, selected_operation):
    """Adds or Subtracts, Shows current balance and history of all recent transactions"""
    pass

actions = {
    "1": deposit,
    "2": withdraw,
    "3": check_balance,
    "4": check_transaction_history,
}
