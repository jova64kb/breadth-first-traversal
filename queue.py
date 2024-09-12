class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Queue:
    def __init__(self):
        self.front = None
    def enqueue(self, data):
        item = Node(data)
        if self.front != None:
            cur = self.front
            while cur.next != None:
                cur = cur.next
            cur.next = item
        else:
            self.front = item
    def dequeue(self):
        if self.front != None:
            data = self.front.data
            self.front = self.front.next
            return data
        else:
            return None
    def peek(self):
        return None if self.front == None else self.front.data

