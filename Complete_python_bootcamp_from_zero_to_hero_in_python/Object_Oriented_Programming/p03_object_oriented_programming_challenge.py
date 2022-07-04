class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, dep_amt):
        self.balance += dep_amt
        return 'Deposit Accepted'

    def withdrawal(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            return 'Withdrawal Accepted'
        else:
            return 'Funds Unavailable'

    def __str__(self):
        return f'Account owner: {self.name}\nAccount balance: ${self.balance}'

acct1 = Account('Jose', 100)

print(acct1.name)
print(acct1.balance)
print(acct1.deposit(50))
print(acct1)
print(acct1.withdrawal(75))
print(acct1)
print(acct1.withdrawal(500))
print(acct1)
