class BankAccount:
    balance = []
    int_rate = 0.01
    def __init__(self, int_rate = 0.01, account_balance = 0):
        self.account_balance = account_balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        if self.account_balance < amount:
            print('Insufficient funds: Charging a $5 fee')
            self.account_balance -= 5
            return self
        else:
            self.account_balance -= amount
            return self
    def display_account_info(self):
        print('Balance: ' + str(self.account_balance))
    def yield_interest(self):
        if self.account_balance > 0:
            x = self.account_balance
            x *= 0.01
            self.account_balance += x
            return self
        else:
            pass

Adrien = BankAccount()
John = BankAccount()

Adrien.deposit(50).withdraw(5).yield_interest().display_account_info()
John.deposit(100).withdraw(5).yield_interest().display_account_info()