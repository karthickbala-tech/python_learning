#Write a class BankAccount with methods deposit, withdraw, and check_balance.
class Bankaccount():
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"deposit{ amount}")
        else:
            print("Deposit amount must be positive.")   
    def withdraw(self,amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.") 
        else:
            self.balance-=amount
            print(f"withdraw {amount}")
        
    def check_balance(self):
        print(f"corrent balance {self.balance}")
    
obj = Bankaccount()
obj.deposit(5000)
obj.withdraw(200)
obj.check_balance() 