from processor import Processor

class SerialProcessor(Processor):
    # Serial without concurrency

    def __init__(self):
        super().__init__()

    def start(self):
        names = self.txns.keys()
        for i in names:
            while True:
                if (self.txns[i].next()) :
                    self.log()
                    op = self.txns[i].exec()
                    print("execute: ", end="")
                    op.log()
                    print("\n")
                else:
                    break

if __name__=="__main__":
    proc = SerialProcessor()
    proc.load("contoh.txt")
    proc.start()