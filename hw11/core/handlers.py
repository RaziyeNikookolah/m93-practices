import shelve
from datetime import date
from functools import reduce
from typing import List, Dict

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

    def get_transactions_between_dates(self, start_date: date, end_date: date):
        with shelve.open(self.file_path)as db:
            is_ransaction_in_range_of_date=lambda item:True if item.date >= start_date and item.date <= end_date else False                    
            transactions=filter(is_ransaction_in_range_of_date, list(db.values()))                    
            return transactions

    # def get_transactions_between_dates(self, start_date: date, end_date: date) -> List[Transaction]:
    #     with shelve.open(self.file_path) as db:
    #         transactions = list(db.values())
    #         return [t for t in transactions if start_date <= t.date <= end_date]

    def summary_report_between_two_dates(self, start_date: date, end_date: date) -> Dict[str, any]:
        transactions = self.get_transactions_between_dates(
            start_date, end_date)
        
        income_transactions = list(map(
            lambda transc: transc.category if transc.type == TransactionType.INCOME 
                                            else ..., transactions))   
        # income_transactions = [
        #     t for t in transactions if t.type == TransactionType.INCOME]
        
        expence_transactions= list(map(
            lambda transc: transc.category if transc.type == TransactionType.EXPENCE 
                                            else ..., transactions))        
        # expence_transactions = [
        #     t for t in transactions if t.type == TransactionType.EXPENCE]
        
        income_categories = set(
            map(lambda transc: transc.category, income_transactions))
        # income_categories = set([t.category for t in income_transactions])
        
        expence_categories = set(
            map(lambda transc: transc.category, expence_transactions))
        # expence_categories = set([t.category for t in expence_transactions])
        
        total_income = reduce(lambda acc, t: acc +
                              t.amount, income_transactions, 0)
        total_expence = reduce(lambda acc, t: acc +
                               t.amount, expence_transactions, 0)
        balance = total_income - total_expence
        return {"total_income": total_income, "income_categories": income_categories, "total_expence": total_expence, "expence_categories": expence_categories, "balance": balance}


