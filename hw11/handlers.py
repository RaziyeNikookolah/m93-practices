import shelve
from datetime import date
from transaction import Transaction

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_all_transactions(self):
        with shelve.open(self.file_path)as db:
            return list(db)

    def append_transaction(self, item:Transaction):
        with shelve.open(self.file_path)as db:
            db = db.update({item.id:item})

    def search_transaction_by_date_range(self, start_date:date,end_date:date):
        with shelve.open(self.file_path)as db:
            founded_lst=[]
            for item in list(db):               
                if item.get["date"] >=start_date and item.get["date"]<=end_date:
                    founded_lst.append(item)
            return founded_lst

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