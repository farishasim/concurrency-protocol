OP_READ='R'
OP_WRITE='W'
OP_COMMIT='C'

class Operation:

    def __init__(self, opcode, cmd:str) -> None:
        self.code = opcode
        item = cmd.split('=')
        self.item = item[0]
        if self.code == OP_WRITE:
            self.value = int(item[1])
        return
    
    def log(self):
        if self.code == OP_COMMIT:
            print(f"{self.code}", end=";")
        elif self.code == OP_READ:
            print(f"{self.code}({self.item})", end=";")
        else:
            print(f"{self.code}({self.item}={self.value})", end=";")