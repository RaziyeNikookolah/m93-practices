from datetime import datetime, date
from transaction.models import Transaction, TransactionType
from core.handlers import FileHandler


class PersonalFinanceManager:
    lst_transactions = []
    __db = FileHandler("storage/transactions.shelve")
    balance = 0

    @classmethod
    def get_all_transaction_from_file(cls):
        cls.lst_transactions = cls.__db.get_all_transactions()

    @classmethod
    def add_transaction(cls, transaction: Transaction) -> None:
        """Add a new transaction to the personal finance manager."""
        if transaction.type == TransactionType.INCOME:
            cls.balance += transaction.amount
        elif transaction.type == TransactionType.EXPENSE:
            cls.balance -= transaction.amount
        else:
            raise ValueError("Invalid transaction type")

        # dict_transaction={'type': transaction.type , 'date': transaction.date, 'amount': transaction.amount, 'category' :
        #                 transaction.category, 'description': transaction.description,'balance':cls.balance}
        # cls.lst_transactions.append(dict_transaction)
        cls.lst_transactions.append(transaction)
        cls.__db.append_transaction(transaction)

    @classmethod
    def show_transactions(cls, start_date: date = None, end_date: date = None) -> None:
        """View all transactions between two dates."""
        if start_date == None and end_date == None:  # show all transactions
            lst_result = cls.__db.get_all_transactions()
            print(*lst_result)
        elif end_date == None:  # user enter just start_date => show transactions until now
            end_date = datetime.now()
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            lst_result = cls.__db.search_transaction_by_date_range(
                start_date, end_date)
            print(*lst_result)
        else:  # user enter start_date and end_date
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            lst_result = cls.__db.search_transaction_by_date_range(
                start_date, end_date)
            print(*lst_result)
