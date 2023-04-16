from datetime import datetime
from enum import Enum
from decimal import Decimal
import itertools


class TransactionType(Enum):
    EXPENSE = "Expense"
    INCOME = "Income"


class Transaction():

    def __init__(self, type: TransactionType, amount: Decimal, date: str, category: str, description: str) -> None:
        self.amount = Decimal(amount)
        self.date = datetime.strptime(date, '%Y-%m-%d').date()
        self.type = type
        self.category = category
        self.description = description
        dt = datetime.now()
        self.id = datetime.timestamp(dt)

    def __str__(self) -> str:
        return f"type: {self.type.value}, date: {self.date}, amount: {self.amount}, category: {self.category}, description: {self.description}"


# t1 = Transaction("Expence", 200, '2023-04-05',
#                  "house rent", "monthly expence ..")

# t2 = Transaction("Expence", 200, '2023-04-05',
#                  "house rent", "monthly expence ..")
# print(t1.id)
# print(t2.id)
