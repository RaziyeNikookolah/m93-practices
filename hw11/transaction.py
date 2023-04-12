from datetime import datetime
from enum import Enum

class TransactionType(Enum):
    EXPENCE="Expence"
    INCOME="Income"

class Transaction():
    def __init__(self,type:TransactionType,amount: int,date:datetime,category:str,description:str)->None:
        self.amount=amount
        self.date=date
        self.type=type
        self.category=category
        self.description=description
        
    def __str__(self) -> str:
        return f"type: {self.type.value}, date: {self.date}, amount: {self.amount}, category :{self.category}, description: {self.description}"

        

# t1=Transaction(TransactionType.INCOME,10000,'2020-01-02 11:30','salary','Teaching math')
# t2=Transaction(TransactionType.EXPENCE,2000,'2021-01-02 12:30','tuition','Programming bootcamp')    
    
# print(t1)
# print(t2) 
 