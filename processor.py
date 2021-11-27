from os import name
from item import Item
from lockmanager import LockManager
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
        self.log()
        while self.exec():
            self.log()
        return

if __name__=="__main__":
    proc = Processor()
    proc.load("contoh.txt")
    proc.log()