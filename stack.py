class Stack:
    def __init__(self):
        self.Elements = []

    def push(self, value):
        self.Elements.append(value)

    def pop(self):
        return self.Elements.pop()
    
    def empty(self):
        return len(self.Elements) == 0
    
    def show(self):
        for value in reversed(self.Elements):
            print(value)


# Insert value at bottom
def BottomInsert(s, value):
    if s.empty():
        s.push(value)   # call push method
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)

# Reverse the stack
def Reverse(s):
    if s.empty():
        return
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)


stk = Stack()
stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)
stk.push(50)


print("Origial stack")
stk.show()

print("\nStack after reversing")
Reverse(stk)
stk.show()
