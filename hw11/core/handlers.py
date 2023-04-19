import shelve
from datetime import date
from functools import reduce
from typing import List, Dict

from transaction.models import Transaction, TransactionType


class TransactionsFileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_all_transactions(self):
        with shelve.open(self.file_path) as db:
            return list(db.values())

    def append_transaction(self, item: Transaction):
        with shelve.open(self.file_path) as db:
            db = db.update({str(item.id): item})

    def get_transactions_between_two_dates(
        self, start_date: date, end_date: date
    ) -> List[Transaction]:
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
