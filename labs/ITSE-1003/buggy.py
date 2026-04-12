class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        # Ignora amount ≤ 0: deposit(-fee) no descuenta la comisión.
        if amount > 0: #lack of : after if statement
            self.__balance += amount
            print(amount, "deposited.")

    def show_balance(self):
        print("Balance:", self.__balance)

    def monthly_update(self):
        print("General account update")


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def monthly_update(self):
        # __balance aquí es mangling de la subclase, no el saldo de BankAccount.
        interest = self.__balance * self.interest_rate
        self.deposit(interest)
        print("Savings interest added.")


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance, fee):
        super().__init__(owner, balance)
        self.fee = fee

    def monthly_update(self):
        # deposit(-fee) no pasa el if amount > 0 del padre.
        self.deposit(-self.fee)
        print("Checking account fee charged.")


account1 = SavingsAccount("Maria", 1000, 0.05)
account2 = CheckingAccount("John", 800, 20)

accounts = [account1, account2]

# lack of : after for statement
for account in accounts:
    account.monthly_update()
    account.show_balance()

# __balance mangled: no accesible desde fuera → AttributeError.
print(account1.__balance)
