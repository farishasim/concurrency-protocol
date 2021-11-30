from random import randint
from typing import Dict, List
import sys

from lockmanager import LockManager
from operation import OP_COMMIT, OP_READ, OP_WRITE
from processor import Processor
from transaction import Transaction

class SimpleLockProcessor(Processor):
    
    def __init__(self, filename):
        super().__init__(filename)
        self.locker = LockManager(self.data)
        self.QUEUE:List[Transaction] = []
        self.WAIT:Dict[Transaction,List[Transaction]] = {}
        self.COMMIT:List[Transaction] = []

    def test_txn(self, txn):
        # check if txn can get all required lock
        # or if txn is a single read/write request
        for op in txn.ops:
            if op.code == OP_WRITE or op.code == OP_READ:
                holder = self.locker.table[op.item]
                if holder != 0 and holder != txn:
                    print(self.WAIT)
                    self.WAIT[holder].append(txn)
                    return False
        
        for op in txn.ops:
            if op.code != OP_COMMIT:
                self.locker.lock(txn, op.item)
        self.QUEUE.append(txn)
        self.WAIT[txn]=[]
        return True

    def choose_txn(self):
        txns = list(self.txns.keys())
        rand = randint(0, len(txns)-1)
        txn:Transaction = self.txns[txns[rand]]

        if len(self.COMMIT) == len(self.txns):
            return False

        if txn in self.QUEUE:
            can_exec = txn not in self.COMMIT
        else :
            can_exec = self.test_txn(txn)

        for _, waited in self.WAIT.items():
            if txn in waited:
                can_exec = False

        if can_exec:
            if txn.next().code == OP_COMMIT:
                self.COMMIT.append(txn)
                self.WAIT.pop(txn)
                self.locker.unlockall(txn)
            return txn 

        return self.choose_txn()

if __name__=="__main__":
    proc = SimpleLockProcessor(sys.argv[1])
    proc.run()