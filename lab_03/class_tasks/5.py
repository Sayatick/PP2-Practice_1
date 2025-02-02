class Bank_Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, quantity):
        if quantity > 0:
            self.balance += quantity
            print(f"Mr. {self.owner} your balance now: {self.balance} tg")
        else:
            print("Negative value!!!")
    
    def withdraws(self, quantity):
        if 0 > quantity:
            print("Negative value!!!")
        elif self.balance >= quantity:
            self.balance -= quantity
            print(f"Mr. {self.owner} your balace was decreased to {self.balance} tg")
        else:
            print("Your balance is lower than you want to withdraw!!!")
            
account = Bank_Account("Sayat")
account.deposit(100000)
account.withdraws(12300)
account.withdraws(100230)
account.withdraws(19956)

        