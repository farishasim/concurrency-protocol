from item import Item
from transaction import Transaction

class LockManager():

    def __init__(self, items:dict) -> None:
        # initiate lock_table
        self.table = dict.fromkeys(items.keys(), 0)
        return

    def lock(self, txn:Transaction, item):
        if self.table[item] :
            return False
        self.table[item] = txn
        return True
    
    def unlock(self, item):
        self.table[item] = False
        return

    def unlockall(self, txn):
        for item, tx in self.table.items():
            if tx == txn:
                self.unlock(item)

