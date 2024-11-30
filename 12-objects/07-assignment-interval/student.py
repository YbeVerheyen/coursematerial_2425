class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def is_empty(self):
        if self.lower > self.upper:
            return True
        return False
    
    def contains(self, value):
        if value >= self.lower and  value <= self.upper:
            return True
        return False
    
    def overlaps_with(self, other):
        if self.is_empty() or other.is_empty():
            return False
        if other.upper >= self.upper >= other.lower or self.lower <= other.upper <= self.upper:
            return True
        return False