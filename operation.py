OP_READ='R'
OP_WRITE='W'
OP_COMMIT='C'

class Operation:

    def __init__(self, opcode, cmd:str) -> None:
        self.op = opcode
        item = cmd.split('=')
        self.item = item[0]
        if self.op==OP_WRITE:
            self.value = int(item[1])
        return
    
    def log(self):
        if self.op == OP_COMMIT:
            print(f"{self.op}", end=";")
        elif self.op == OP_READ:
            print(f"{self.op}({self.item})", end=";")
        else:
            print(f"{self.op}({self.item}={self.value})", end=";")