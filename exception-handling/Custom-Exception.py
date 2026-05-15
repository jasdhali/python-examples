class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance"""
    pass
def withdraw(amount,balance ):
    if amount > balance:
        raise InsufficientFundsError(f"Attempted to withdraw ${amount} from ${balance}")
    return balance - amount

try:
    withdraw(100,50)
except InsufficientFundsError as e:
    # Handle the custom error
    print(e)
