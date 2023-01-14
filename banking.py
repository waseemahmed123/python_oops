class Account:
    def __init__(self,name,balance,min_balance):
        self.name=name
        self.balance=balance
        self.min_balance=min_balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance-amount>=self.min_balance:
            self.balance-=amount
        else:
            print("Sorry,Insufficient Funds")
    def printStatement(self):
        print("Account Balance:",self.balance)
class Current(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=-1000)
    def __str__(self):
        return"{}'s Current Account with Balance :{}".format(self.name,self.balance)
class Savings(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance=0)
    def __str__(self):
        return "{}'s Savings Account with Balance :{}".format(self.name,self.balance)
c=Savings("Waseem",10000)
print(c)
c.deposit(5000)
c.printStatement()
c.withdraw(16000)
print(c)
        