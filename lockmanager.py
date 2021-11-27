from item import Item

class LockManager():

    def __init__(self, items:dict) -> None:
        # initiate lock_table
        self.table = dict.fromkeys(items.keys(), 0)
        return

    def lock(self, txn, item):
        if self.table[item] :
            return False
        self.table[item] = txn
        return True
    
    def unlock(self, item):
        self.table[item] = False
        return

