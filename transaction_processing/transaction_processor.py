from .transaction import Transaction
class TransactionProcessor:
    def process_transaction(transaction):
        if transaction.transaction_type == "deposit":
            transaction.account.deposite(transaction.amount)
        elif transaction.transaction_type == "withdraw":
            transaction.account.withdraw(transaction.amount)
        else:
            print("Invalid transaction type")