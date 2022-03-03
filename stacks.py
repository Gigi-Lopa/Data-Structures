class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item, *args):
        self.item = item
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def peek(self):

        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def show(self):
        return self.items

if __name__ == '__main__':
    sk = Stack()
    sk.push(5)
    print(sk.isEmpty())
    
