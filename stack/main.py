class Stack:
    def __init__(self):
        self.items = [] 

    #2.  Check if stack is empty
    def isEmpty(self):
        return self.items == []

    #3.  Push new items to the top of stack
    def push(self, data):
        self.items.append(data)

    #4. Popping data off of the stack 
    def pop(self):
        return self.items.pop()

    #5. Returning size of the stack 
    def size(self):
        return len(self.items)

#1. Instantiate an object from class Stack 
pancakes = Stack()

#2. push to top of stack 
pancakes.push(1)

#3. returning the size of stack
print(pancakes.size()) # return 1 

#4. check if its empty if there's no stuff inside it
print(pancakes.isEmpty()) # False

#5. check if its empty if there's stuff inside it
pancakes.push("CSin3") #pushing CSin3 to the top
pancakes.push(100.2) #pushing 100.2 to the top
print(pancakes.isEmpty()) #False

#6. check the top of stack 
print(pancakes.size()) # return back a 3
print(pancakes.pop()) # 100.2 
print(pancakes.size()) # return back a 2
