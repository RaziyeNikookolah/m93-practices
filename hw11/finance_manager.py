from transaction import Transaction,TransactionType

class PersonalFinanceManager:
    
    lst_transactions=list()
    balance=0
    
    @classmethod
    def add_transaction(cls,transaction:Transaction)-> None:
        
        print(TransactionType.INCOM.value)
        if transaction.type.value==TransactionType.INCOM.values():
            cls.balance+=transaction.amount
        elif transaction.type.value==TransactionType.EXPENCE.values():
            cls.balance-=transaction.amount
        else:
            raise Exception("Invalid transaction type")
        
        cls.lst_transactions.append((transaction,cls.balance))
    
    @classmethod
    def show_transactions(cls)-> None:
        for t in cls.lst_transactions:
            print(t) 
            
t1=Transaction(TransactionType.INCOME,10000,'2020-01-02 11:30','salary','Teaching math')
t2=Transaction(TransactionType.EXPENCE,2000,'2021-01-02 12:30','tuition','Programming bootcamp')    
    
PersonalFinanceManager.add_transaction(t1)
PersonalFinanceManager.add_transaction(t2)
PersonalFinanceManager.show_transactions()
