class Account :
    def __init__(self,acc_number, name, balance):
        self.acc_number = acc_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("You don't have enough money!")
    def check_balance(self):
        print(f"Account {self.acc_number} balance: {self.balance}")