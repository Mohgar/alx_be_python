class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        initial_balance = 0

    def deposit(self, amount):
        return self.account_balance + amount

    def withdraw(self, amount):
        result = self.account_balance - amount
        if result > 0:
            return True
        else:
            result = self.account_balance
            return False

    def display_balance(self):
        print(f"the current balance is {self.account_balance}")








