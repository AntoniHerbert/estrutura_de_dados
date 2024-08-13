class Deque:
    def __init__ (self):
        self.A = []
        self.count = 0

    def isEmpty(self):
        return self.count == 0
    
    def add_front(self):
        if not self.isEmpty():
            return self.A.pop()
        
    def remove_rear(self):
        if not self.isEmpty():
            return self.A.pop(0)
