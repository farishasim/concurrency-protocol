class Item():

    def __init__(self, name=None, val=None) -> None:
        self.name = name
        self.val = val
        return

    def set(self, val):
        self.val = val
        return 
    
    def get(self):
        return self.val

    def log(self):
        print(f"{self.name}: {self.val}")