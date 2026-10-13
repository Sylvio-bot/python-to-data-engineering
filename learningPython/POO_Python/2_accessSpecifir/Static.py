class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            print(f"{self.owner}'s new balance: {self._balance}")
        else:
            print('Deposit amount must be positive.')

    #protected method : you can use it in the class itself and child
    def _is_valid_amount(self, amount):
        return amount > 0

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5

account = BankAccount("Alice", 500)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(3))
