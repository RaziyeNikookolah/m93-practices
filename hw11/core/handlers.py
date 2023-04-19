import shelve
from datetime import date
from functools import reduce
from typing import List, Dict

from transaction.models import Transaction, TransactionType


class TransactionsFileHandler:
    """
    A class for handling transactions data in a shelve file.

    Parameters:
        file_path (str): The path to the shelve file.

    Attributes:
        file_path (str): The path to the shelve file.

    """

    def __init__(self, file_path):
        self.file_path = file_path

    def get_all_transactions(self):
        """
        Get all transactions from the shelve file.

        Returns:
            List[Transaction]: A list of all transactions.

        """
        with shelve.open(self.file_path) as db:
            return list(db.values())

    def append_transaction(self, item: Transaction):
        """
        Append a transaction to the shelve file.

        Parameters:
            item (Transaction): The transaction to append.

        """
        with shelve.open(self.file_path) as db:
            db = db.update({str(item.id): item})

    def get_transactions_between_two_dates(
        self, start_date: date, end_date: date
    ) -> List[Transaction]:
        """
        Get all transactions that fall between two given dates.

        Parameters:
            start_date (date): The start date.
            end_date (date): The end date.

        Returns:
            List[Transaction]: A list of transactions that fall between the given dates.

        """

        with shelve.open(self.file_path) as db:
            return list(
                filter(
                    lambda trnsc: True
                    if start_date <= trnsc.date <= end_date
                    else False,
                    list(db.values()),
                )
            )

    def get_summary_report_between_two_dates(
        self, start_date: date, end_date: date
    ) -> Dict[str, any]:
        """
        Get a summary report of transactions that fall between two given dates.

        Parameters:
            start_date (date): The start date.
            end_date (date): The end date.

        Returns:
            Dict[str, any]: A dictionary containing the following keys:
                - total_income: The total income in the given period.
                - income_categories: A set of income categories in the given period.
                - total_expence: The total expense in the given period.
                - expence_categories: A set of expense categories in the given period.
                - balance: The difference between total income and total expense in the given period.
                - transaction_count: The total number of transactions in the given period.

        """
        transactions = self.get_transactions_between_two_dates(start_date, end_date)

        income_transactions = list(
            filter(
                lambda t: True if t.type == TransactionType.INCOME else False,
                transactions,
            )
        )

        expence_transactions = list(
            filter(
                lambda t: True if t.type == TransactionType.EXPENCE else False,
                transactions,
            )
        )

        income_categories = set(map(lambda t: t.category, income_transactions))
        expence_categories = set(map(lambda t: t.category, expence_transactions))

        total_income = reduce(lambda acc, t: acc + t.amount, income_transactions, 0)
        total_expence = reduce(lambda acc, t: acc + t.amount, expence_transactions, 0)

        balance = total_income - total_expence
        return {
            "total_income": total_income,
            "income_categories": income_categories,
            "total_expence": total_expence,
            "expence_categories": expence_categories,
            "balance": balance,
            "transaction_count": len(list(transactions)),
        }
