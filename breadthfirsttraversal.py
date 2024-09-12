import queue as q

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root != None:
            cur = self.root
            while cur != None:
                if data < cur.data:
                    if cur.left != None:
                        cur = cur.left
                    else:
                        cur.left = Node(data)
                        break
                elif data > cur.data:
                    if cur.right != None:
                        cur = cur.right
                    else:
                        cur.right = Node(data)
                        break
        else:
            self.root = Node(data)
    def bfs_traversal(self):
        if self.root == None:
            return None
        res = []
        queue = q.Queue()
        queue.enqueue(self.root)
        cur = queue.dequeue()
        while cur != None:
            res.append(cur.data)
            if cur.left != None:
                queue.enqueue(cur.left)
            if cur.right != None:
                queue.enqueue(cur.right)
            cur = queue.dequeue()
        return res

bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(9)
bst.insert(4)
bst.insert(6)
res = bst.bfs_traversal()
print(res)

