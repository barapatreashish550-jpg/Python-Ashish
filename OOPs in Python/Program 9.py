# Base class
class Account:
    def __init__(self, name, acc_no, acc_type, balance):
        self.name = name
        self.acc_no = acc_no
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    def display_balance(self):
        print("Current Balance:", self.balance)


# Saving Account Class
class sav_acct(Account):
    def add_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance += interest
        print("Interest Added:", interest)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")


# Current Account Class
class cur_acct(Account):
    min_balance = 500
    penalty = 50

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def check_min_balance(self):
        if self.balance < self.min_balance:
            print("Minimum balance not maintained. Penalty imposed.")
            self.balance -= self.penalty


# Creating Saving Account
s = sav_acct("Rahul", 101, "Saving", 1000)
s.deposit(500)
s.add_interest(5)
s.withdraw(300)
s.display_balance()

print()

# Creating Current Account
c = cur_acct("Amit", 102, "Current", 600)
c.deposit(200)
c.withdraw(400)
c.check_min_balance()
c.display_balance()