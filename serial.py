from processor import Processor
from operation import *

class SerialProcessor(Processor):
    # Serial without concurrency
    
    def choose_txn(self):
        for i, txn in self.txns.items():
            if txn.isdone():
                continue
            return txn
        return False

if __name__=="__main__":
    proc = SerialProcessor("contoh.txt")
    proc.run()