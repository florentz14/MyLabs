# ------------------------------------------------------------ #
# File: buggy.py
# Date: 2026-04-15
# Author: Florentino
# Description: Bank account hierarchy exercise (fixed version).
# Explanation: Demonstrates inheritance, polymorphism and controlled
# attribute access. Uses a single-underscore `_balance` so subclasses
# can read it, and exposes a read-only `balance` property for callers.
# ------------------------------------------------------------ #


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(amount, "deposited.")

    def charge(self, amount):
        """Deduct a positive amount (fees, withdrawals, etc.)."""
        if amount > 0:
            self._balance -= amount
            print(amount, "charged.")

    def show_balance(self):
        print("Balance:", self._balance)

    def monthly_update(self):
        print("General account update")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def monthly_update(self):
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        print("Savings interest added.")


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance, fee):
        super().__init__(owner, balance)
        self.fee = fee

    def monthly_update(self):
        self.charge(self.fee)
        print("Checking account fee charged.")


if __name__ == "__main__":
    account1 = SavingsAccount("Maria", 1000, 0.05)
    account2 = CheckingAccount("John", 800, 20)

    for account in (account1, account2):
        account.monthly_update()
        account.show_balance()

    print("Maria's balance via property:", account1.balance)
