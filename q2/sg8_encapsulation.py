#gumagawa ng class which is bankAccount, serves as the blueprint for instantiating actual accounts
class bankAccount: 
    def __init__(self, account_number: int, balance: float): #init=initialize new bank account with account number as integer and balance as float
        self.__account_number = account_number #stores account number, very protected private property because of two underscore
        self.__balance = balance #stores balance, very protected private property because of two underscore

    #setter method for account number, allows the account number to be set to a different value
    def set_account_number(self, account_number):
        self.__account_number = account_number #updates account number with the new value
    
    @property #makes get_account_number easier to access like an attribute
    def get_account_number(self): #getter method that gets account number
        return self.__account_number #returns the actual account number

    #setter method for balance, allows balance to be increased or decreased
    def set_balance(self, balance):
        if balance >= 0: #checks whether the new increased or decreased balance is positive or 0
            self.__balance = balance #returns the actual balance if it is positive
        else: 
            print("Warning! The balance must not be a negative number.") #returns a warning message when the user attempts to make the balance negative

    @property #makes get_balance easier to access like an attribute
    def get_balance(self): #retrieves account balance
        return self.__balance #returns actual balance

account1 = bankAccount(12012, 6761) #creates a bankAccount object named account1, defining its account number and balance

print("Account 1") 
print(f"Account Number: {account1.get_account_number}") #retrieves and prints acocunt number
print(f"Balance: {account1.get_balance}") #retrieves and prints balance

print("")

print("Update balance to -100") 
account1.set_balance(-100) #attemps to set the balance to a negative number, which should trigger a warning
print(f"Account Number: {account1.get_account_number}") #retrives and prints the account number again
print(f"Balance: {account1.get_balance}") #retrives and prints the balance again to show that it should stay the same since the balance must not be negative
