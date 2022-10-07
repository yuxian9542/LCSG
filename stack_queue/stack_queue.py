import gc


class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


class Stack:
    def __init__(self):
        self.head = None

    def push(self, val):
        node = Node(val, self.head)
        self.head = node

    def pop(self):
        if self.head is None:
            raise Exception('Cannot pop from an empty stack')
        cur = self.head
        self.head = cur.next
        del cur
        gc.collect()

    def print(self):
        cur = self.head
        prt = ''
        while cur is not None:
            prt += str(cur.val) + ' -> '
            cur = cur.next
        print(prt)


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        node = Node(val, None)
        if self.tail is not None:
            self.tail.next = node
        self.tail = node
        if self.head is None:
            self.head = node

    def dequeue(self):
        if self.head is None:
            raise Exception('cannot dequeue from an empty queue')
        if self.head == self.tail:
            del self.head
            self.head = None
            self.tail = None
        else:
            cur = self.head
            self.head = cur.next
            del cur
        gc.collect()

    def print(self):
        cur = self.head
        prt = ''
        while cur is not None:
            prt += str(cur.val) + ' -> '
            cur = cur.next
        print(prt)


s = Stack()
s.push(2)
s.push(4)
s.print()
s.pop()
s.print()

q = Queue()
q.enqueue(5)
q.dequeue()
q.print()
q.enqueue(7)
q.enqueue(9)
q.print()
