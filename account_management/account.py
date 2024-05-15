class Account:
    def __init__(self,account_number,customer,balance=0.0):
        self.account_number=account_number
        self.customer=customer
        self.balance=balance

    def deposite(self,amount):
        self.balance+=amount
        return self.balance
    def withdrow(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            return self.balance
        else:
            print("Insuffitient Funds")
            return None
    def get_balance(self):
        return self.balance

