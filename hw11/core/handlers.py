import shelve
from datetime import date
from transaction.models import Transaction, TransactionType


class TransactionsFileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_all_transactions(self):
        with shelve.open(self.file_path)as db:
            return list(db.values())

    def append_transaction(self, item: Transaction):
        with shelve.open(self.file_path)as db:
            db = db.update({str(item.id): item})

    def search_transaction_by_date_range(self, start_date: date, end_date: date):
        with shelve.open(self.file_path)as db:

            is_ransaction_in_range_of_date=lambda item:True if item.date >= start_date and item.date <= end_date else False
                    
            founded_lst=filter(is_ransaction_in_range_of_date, list(db.values()))                    
            return founded_lst

    def summary_report_between_two_dates_(self, start_date: date, end_date: date):
        with shelve.open(self.file_path)as db:
            total_income = 0
            total_expence = 0
            income_category = {}
            expence_category = {}

            item: Transaction
            for item in list(db.values()):

                if item.date >= start_date and item.date <= end_date:
                    if item.type == TransactionType.INCOME:
                        total_income += item.amount
                        income_category[item.category] = income_category.get(
                            item.category, 0)+1
                    elif item.type == TransactionType.EXPENSE:
                        total_expence += item.amount
                        expence_category[item.category] = expence_category.get(
                            item.category, 0)+1
            return {"total_income": total_income, "income_category": income_category, "total_expence": total_expence, "expence_category": expence_category}
