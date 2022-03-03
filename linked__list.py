class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class lists(object):
    def __init__(self):
        self.head = node() #HEAD IS THE BLOCK OF AN ITEM IN A LIST
    
    def append(self, newData):
        new_node = node(newData)
        cur =  self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def total(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def show(self):
        elements = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)

if __name__ == '__main__':
    
    lt = lists()
    lt.append(5)
    print(lt.total())
    