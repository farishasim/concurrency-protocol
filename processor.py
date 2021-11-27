from os import name
from item import Item
from lockmanager import LockManager
from operation import OP_WRITE
from transaction import Transaction


class Processor():

    def __init__(self):
        self.data = {}
        self.txns = {}
        self.lmgr = None
        return

    def load(self, filename):
        with open(filename, 'r') as f:
            n = int(f.readline())
            for i in range(n):
                line = f.readline()
                item = line.split('=')
                item = Item(item[0], int(item[1]))
                self.data[item.name] = item
            n = int(f.readline())
            for i in range(n):
                line = f.readline()
                txn = Transaction(line)
                self.txns[txn.name] = txn
            self.lmgr = LockManager(self.data)

    def log(self):
        for _, v in self.data.items():
            v.log()
        for _, v in self.txns.items():
            v.log()
        print()

    def run(self):
        while True:
            self.log()
            txn = self.choose_txn()
            if txn:
                print("execute : ", end=f"{txn.name}-")
                txn.next().log()
                print("\n")
                self.exec(txn)
            else :
                break
        return

    def exec(self, txn):
        op = txn.exec()
        item = op.item
        code = op.code
        if code == OP_WRITE:
            val = op.value
            self.data[item].set(val)

    def choose_txn(self):
        # override this method to choose appropriate txn
        # based on chosen algorithm
        # return txn, or 
        # return False (if all txn is done)
        return False

if __name__=="__main__":
    proc = Processor()
    proc.load("contoh.txt")
    proc.run()