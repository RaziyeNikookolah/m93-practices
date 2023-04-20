from datetime import datetime, date
from transaction.models import Transaction, TransactionType
from core.handlers import TransactionsFileHandler
from core.exceptions import RequiredDateError


class PersonalFinanceManager:
    __db = TransactionsFileHandler("storage/transactions.shelve")

    @classmethod
    def view_all_transactions(cls):
        """Get all the transactions stored in the personal finance manager.

        Returns:
            List[Transaction]: List of all the transactions stored in the manager.
        """
        return cls.__db.get_all_transactions()

    @classmethod
    def add_transaction(cls, transaction: Transaction) -> None:
        """Add a new transaction to the personal finance manager.

        Args:
            transaction (Transaction): The transaction object to be added.

        Returns:
            None
        """

        cls.__db.append_transaction(transaction)

    @classmethod
    def view_transactions_between_two_dates(
        cls, start_date: date = None, end_date: date = None
    ) -> None:
        """View all transactions between two dates.

        Args:
            start_date (date, optional): The start date of the range. Defaults to None.
            end_date (date, optional): The end date of the range. Defaults to None.

        Raises:
            RequiredDateException: If both start_date and end_date are None.

        Returns:
            None
        """
        if start_date == None and end_date == None:
            raise RequiredDateError()

        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        transactions = cls.__db.get_transactions_between_two_dates(start_date, end_date)

        not transactions and print("No transaction added in this range of dates")
        print(*transactions, sep="\n")

    @classmethod
    def view_summary_report_between_two_dates(
        cls, start_date: date = None, end_date: date = None
    ) -> None:
        """View the summary report of all the transactions between two dates.

        Args:
            start_date (date, optional): The start date of the range. Defaults to None.
            end_date (date, optional): The end date of the range. Defaults to None.

        Raises:
            RequiredDateException: If either start_date or end_date is None.

        Returns:
            None
        """
        if start_date != None and end_date != None:
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            transactions_info = cls.__db.get_summary_report_between_two_dates(
                start_date, end_date
            )
            print()
            if transactions_info.get("transaction_count"):
                for key, value in transactions_info.items():
                    print(f"{key:25} {value}")

            not transactions_info.get("transaction_count") and print(
                "No Transaction added in this range of dates.."
            )
            print()
        else:
            raise RequiredDateError()
