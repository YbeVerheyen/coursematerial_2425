class Averager:
    def __init__(self):
        self.list = []
    
    def add(self, value):
        self.list.append(value)

    def average(self):
        return sum(self.list) / len(self.list)
    
    def reset(self):
        self.list = []