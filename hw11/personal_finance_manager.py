from datetime import datetime
from transaction import Transaction,TransactionType
 
class PersonalFinanceManager:
    lst_transactions = []
    balance = 0

    @classmethod
    def add_transaction(cls, transaction: Transaction) -> None:
        """Add a new transaction to the personal finance manager."""
        if transaction.type == TransactionType.INCOME:
            cls.balance += transaction.amount
        elif transaction.type == TransactionType.EXPENSE:
            cls.balance -= transaction.amount
        else:
            raise ValueError("Invalid transaction type")
        
        dict_transaction={'type': transaction.type , 'date': transaction.date, 'amount': transaction.amount, 'category' :
                        transaction.category, 'description': transaction.description}
        cls.lst_transactions.append((dict_transaction, cls.balance))
        
    
    @classmethod
    def show_transactions(cls ,start_date:str=None,end_date:str=None) -> None:
        """View all transactions between two dates."""
        if start_date==None and end_date==None:#show all transactions
            
            for t in cls.lst_transactions:
                print(t[0],t[1])
        elif end_date==None:#user enter just start date, show transactions until now
            
            end_date=datetime.now()
        else:#user enter start_date and end_date
            
            for t in cls.lst_transactions:#show transaction between 2 dates entered
                transaction_date=t[0].get('date')
                if transaction_date>=start_date and transaction_date<=end_date:
                    print(t[0],t[1])

