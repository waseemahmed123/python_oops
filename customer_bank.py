import sys
class Customer:
    """Customer class with Bank Operations...."""
    bankname="Waseem Bank"
    def __init__(self,name:str,balance:float=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("Balance after deposit:",self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient Funds can perform this operation")
            sys.exit()
        self.balance=self.balance-amt
        print("Balance after Deposit:",self.balance)
        
        
print("Welcome to",Customer.bankname)
name=input("Enter your Name:")
balance=float(input("Enter your balance:"))
c=Customer(name,balance)
while True:
    print("d-Deposit\nw-Withdraw\ne-Exit")
    option =input("Choose your Option:")
    if option=="d" or option=="D":
        amt=float(input("Enter amount:"))
        c.deposit(amt)
    elif option=="w" or option=="W":        
        amt=float(input("Enter amount"))
        c.withdraw(amt)
    elif option=="e" or option=="E":
        print("Thanks for Banking")
        sys.exit()
    else:
        print("Invalid Option")  