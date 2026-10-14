class bankAccount:
    def __init__(self, account_number: int, balance: float):
        self.__account_number = account_number
        self.__balance = balance

    #setter and getter methods for account_number
    def set_account_number(self, account_number):
        self.__account_number = account_number
    
    @property #makes get_account_number a variable of the account that I can call when printing the values
    def get_account_number(self):
        return self.__account_number

    #setter and getter methods for balance
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else: 
            print("Warning! The balance must not be a negative number.") #returns a warning message when the user attempts to make the balance negative

    @property
    def get_balance(self):
        return self.__balance

account1 = bankAccount(12012, 6761) #creates an account

print("Account 1")
print(f"Account Number: {account1.get_account_number}")
print(f"Balance: {account1.get_balance}")

print("")

print("Update balance to -100")
account1.set_balance(-100) #attemps to set the balance to a negative number
print(f"Account Number: {account1.get_account_number}")
print(f"Balance: {account1.get_balance}")
