from datetime import datetime, date
from transaction.models import Transaction, TransactionType
from core.handlers import TransactionsFileHandler
# , BalanceFileHandler


class PersonalFinanceManager:

    __tlb_transaction = TransactionsFileHandler("storage/transactions.shelve")
    # __tlb_balance = BalanceFileHandler("storage/balance.shelve")

    @classmethod
    def get_all_transaction_from_file(cls):
        return cls.__tlb_transaction.get_all_transactions()

    @classmethod
    def add_transaction(cls, transaction: Transaction) -> None:
        """Add a new transaction to the personal finance manager."""
        # if transaction.type == TransactionType.INCOME:
        #     cls.__tlb_balance.set_overal_income_balance(transaction.amount)

        # elif transaction.type == TransactionType.EXPENSE:
        #     cls.__tlb_balance.set_overal_expence_balance(transaction.amount)
        # else:
        #     raise ValueError("Invalid transaction type")

        cls.__tlb_transaction.append_transaction(transaction)
        # print(cls.__tlb_balance.get_overal_income_balance() -
        #       cls.__tlb_balance.get_overal_expence_balance())

    @classmethod
    def show_transactions(cls, start_date: date = None, end_date: date = None) -> None:
        """View all transactions between two dates."""
        if start_date == None and end_date == None:  # show all transactions
            lst_result = cls.__tlb_transaction.get_all_transactions()
            print(
                *lst_result, sep="\n") if lst_result else print("No transaction added")
        elif end_date == None:  # user enter just start_date => show transactions until now
            end_date = datetime.now().date()
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            lst_result = cls.__tlb_transaction.search_transaction_by_date_range(
                start_date, end_date)
            print(
                *lst_result, sep="\n") if lst_result else print("No transaction in these two ranges of dates")
        else:  # user enter start_date and end_date
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            lst_result = cls.__tlb_transaction.search_transaction_by_date_range(
                start_date, end_date)
            print(
                *lst_result, sep="\n") if lst_result else print("No transaction in these two ranges of dates")

    @classmethod
    def report_overal_summary_in_date_range(cls, start_date: date = None, end_date: date = None) -> None:
        """report overall summary between two dates."""
        if start_date != None and end_date != None:  # show all transactions
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            dict_result = cls.__tlb_transaction.summary_report_between_two_dates_(
                start_date, end_date)
            if dict_result.get("income_transaction_count") == 0 and dict_result.get("expence_transaction_count") == 0:
                print("No Transaction added..")
            else:
                balance = dict_result["total_income"] - \
                    dict_result["total_expence"]
                # print(dict_result, f" balance : {balance}")
                print(
                    f"'total_income': {dict_result['total_income']}, 'income_category': {dict_result['income_category']}, 'total_expence': {dict_result['total_expence']}, 'expence_category': {dict_result['expence_category']}, balance : {balance}")
        else:
            raise Exception("two date should be entered..")
