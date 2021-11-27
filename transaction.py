from typing import List
from item import Item
from operation import *

class Transaction():

    def __init__(self, schedule:str=None) -> None:
        self.ops:List[Operation] = []
        self.ptr = 0
        self.string = schedule
        if schedule != None:
            self.parse(schedule)
            return
        self.name = "NoName"
        return 

    def parse(self, schedule:str):
        sch = schedule.rstrip('\n').rstrip(';').split(':')
        self.name = sch[0]
        ops = sch[1].split(';')
        for op in ops:
            try:
                op = op.split('_')
                self.add(Operation(op[0], op[1]))
            except IndexError:
                self.add(Operation(op[0], ' '))

    def add(self, op):
        self.ops.append(op)

    def next(self):
        # return next operation
        try :
            op = self.ops[self.ptr]
            return op
        except IndexError:
            return False

    def isdone(self):
        return self.ptr == len(self.ops)

    def exec(self):
        # return next operation, increment pointer
        try :
            op = self.ops[self.ptr]
            self.ptr += 1
            return op
        except IndexError:
            return False

    def rollback(self):
        # reset pointer
        self.ptr = 0
    
    def log(self):
        print(self.name, end=": ")
        i = self.ptr;
        n = len(self.ops)
        if i==n:
            print("No more operation.", end="")
        while i < n:
            self.ops[i].log()
            i += 1
        print()
