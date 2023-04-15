from datetime import datetime
from enum import Enum
from decimal import Decimal

class TransactionType(Enum):
    EXPENSE = "Expense"
    INCOME = "Income"

class Transaction():
    counter = 0
    def __init__(self, type: TransactionType, amount: str, date: str, category: str, description: str) -> None:
        self.amount = Decimal(amount)
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.type = type
        self.category = category
        self.description = description
        self.__class__.counter+=1
        self.id =self.__class__.counter
        
    def __str__(self) -> str:
        return f"{self.id}) type: {self.type.value}, date: {self.date}, amount: {self.amount}, category: {self.category}, description: {self.description}"
   

 