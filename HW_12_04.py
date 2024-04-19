class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Error: The balance cannot be negative.")
        else:
            self._balance = value

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} units. Current balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} units. Current balance: {self.balance}")
        else:
            print("Error: Insufficient funds.")

account = BankAccount(100)
print("Initial balance:", account.balance)

account.deposit(50)
account.withdraw(30)
account.withdraw(150)

print("Final balance:", account.balance)