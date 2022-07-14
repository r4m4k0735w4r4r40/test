class Number:
    def __init__(self,num):
        self.num = num
    def __repr__(self):
        return self.num
    def __len__(self):
        return len(str(self.num))