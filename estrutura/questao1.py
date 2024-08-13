class Stack:
    def __init__(self):
        self.A = []
        self.count = 0

    def push(self, data):
        self.A.append(data)
        self.count+=1
    
    def pop(self):
        if self.count == 0:
            return None
        self.count-=1
        return self.A.pop()
    
    def peek(self):
        return None if self.count == 0 else self.A[-1]
    
    def isEmpty (self):
        return self.count == 0


def printInstructions(op1, op2, c, register):
    op = {
        "*" : "MT",
        "/" : "DV",
        "+" : "AD",
        "-" : "SB",
    }

    print(f"LD {op1}")
    print(f"{op.get(c)} {op2}")
    print(f"ST {register}")

def writeInstructions(postfix):
    stack = Stack()

    for c in postfix:
        if c in "*/+-":
            op2 = stack.pop()
            op1 = stack.pop()
            TEMPn = "TEMP"+str(stack.count)
            stack.push(TEMPn)
            printInstructions(op1, op2, c, TEMPn)
        else:
            stack.push(c)


writeInstructions("ABC*+DE-/")