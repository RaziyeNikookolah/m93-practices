from datetime import datetime, date
from transaction.models import Transaction, TransactionType
from core.handlers import TransactionsFileHandler


class PersonalFinanceManager:
    __db = TransactionsFileHandler("storage/transactions.shelve")

    @classmethod
    def view_all_transactions(cls):
        return cls.__db.get_all_transactions()

    @classmethod
    def add_transaction(cls, transaction: Transaction) -> None:
        """Add a new transaction to the personal finance manager."""

        cls.__db.append_transaction(transaction)

    @classmethod
    def view_transactions_between_two_dates(
        cls, start_date: date = None, end_date: date = None
    ) -> None:
        """View all transactions between two dates."""
        if start_date == None and end_date == None:
            raise Exception("Two dates required")

        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        transactions = cls.__db.get_transactions_between_two_dates(start_date, end_date)

        not transactions and print("No transaction added in this range of dates")
        print(*transactions, sep="\n")

    @classmethod
    def view_summary_report_between_two_dates(
        cls, start_date: date = None, end_date: date = None
    ) -> None:
        """report overall summary between two dates."""
        if start_date != None and end_date != None:  # show all transactions
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            transactions_info = cls.__db.get_summary_report_between_two_dates(
                start_date, end_date
            )
            print()
            for key, value in transactions_info.items():
                print(f"{key:25} {value}")

            not transactions_info.get("transaction_count") and print(
                "No Transaction added in this range of dates.."
            )

        else:
            raise Exception("Two date should be entered..")
