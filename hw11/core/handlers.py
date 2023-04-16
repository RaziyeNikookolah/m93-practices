import shelve
from datetime import date
from transaction.models import Transaction, TransactionType


class FileHandler:
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
            founded_lst = []
            for item in list(db.values()):
                if item.date >= start_date and item.date <= end_date:
                    founded_lst.append(item)
            return founded_lst

    def summary_report_between_two_dates_(self, start_date: date, end_date: date):
        with shelve.open(self.file_path)as db:
            founded_lst = []
            total_income = 0
            total_expence = 0
            income_category = {}
            expence_category = {}
            income_transaction_count = 0
            expence_transaction_count = 0

            item: Transaction
            for item in list(db.values()):

                if item.date >= start_date and item.date <= end_date:
                    if item.type == TransactionType.INCOME:
                        total_income += item.amount
                        income_category[item.category] = income_category.get(
                            item.category, 0)+1
                        income_transaction_count += 1
                    elif item.type == TransactionType.EXPENSE:
                        total_expence += item.amount
                        expence_category[item.category] = expence_category.get(
                            item.category, 0)+1
                        expence_transaction_count += 1
            return {"total_income": total_income, "income_category": income_category, "income_transaction_count": income_transaction_count, "total_expence": total_expence, "expence_category": expence_category, "expence_transaction_count": expence_transaction_count}
    # def get_all_values(self):
    #     with shelve.open(self.file_path)as db:
    #         return list(db.values())

    # def remove(self, key):
    #     with shelve.open(self.file_path)as db:
    #         if key in db.keys():
    #             del db[key]
    #             return True
    #         else:
    #             return False
