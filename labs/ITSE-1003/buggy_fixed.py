class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(amount, "deposited.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(amount, "withdrawn.")

    def show_balance(self):
        print("Balance:", self.__balance)

    def get_balance(self):
        return self.__balance

    def monthly_update(self):
        print("General account update")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def monthly_update(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print("Savings interest added.")


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance, fee):
        super().__init__(owner, balance)
        self.fee = fee

    def monthly_update(self):
        self.withdraw(self.fee)
        print("Checking account fee charged.")


account1 = SavingsAccount("Maria", 1000, 0.05)
account2 = CheckingAccount("John", 800, 20)
accounts = [account1, account2]
for account in accounts:
    account.monthly_update()
    account.show_balance()
