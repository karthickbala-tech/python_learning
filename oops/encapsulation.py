'''Create a class for a Bank Account with the following private attributes:
Account number
Account holder name
Balance
Your tasks:
Use encapsulation to protect the data.
Provide public methods to:
Get account details
Deposit money
Withdraw money (ensure the balance cannot go negative)
Demonstrate the use of your class by creating an object and performing some deposits and withdrawals'''
class Bankaccount():
    
    def __init__(self,account_no,name):
        self.__account_no=account_no
        self.__name=name
        self.__balance=0
    def display(self):
        print(f"acoount no:{self.__account_no}\naccount holoder name:{self.__name}")
    def deposit(self,amount):
        self.__balance+=amount
        print(f"amount {self.__balance} deposited")
    def withdraw(self,amount):
        if amount>self.__class__balance:
            print(f"error: you only have a {self.__balance} ")
        elif amount<100:
            print('minimum withdraw amount is 100')
        else:
            self.__balance-=amount
            print(f"Current balance is {self.__balance}")
obj=Bankaccount(1234,'bala')
obj.display()
obj.deposit(5000)
obj.withdraw(2000)