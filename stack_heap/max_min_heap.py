class MaxHeap:
    def __init__(self):
        self.heap = []
        self.map = {}
        self.len = -1

    def swap(self, pos):
        child = pos
        while child != 0:
            parent = (child - 1) // 2
            if self.heap[parent] < self.heap[child]:
                temp = self.heap[parent]
                self.heap[parent] = self.heap[child]
                self.heap[child] = temp
                self.map[self.heap[parent]] = parent
                self.map[self.heap[child]] = child
                child = parent
            else:
                break

    def heapify(self, pos):
        child_1 = pos * 2 + 1
        child_2 = pos * 2 + 2
        while True:
            if child_1 > self.len:
                return
            elif child_1 == self.len:
                max_child = child_1
            else:
                max_child = self.map[max([self.heap[child_1], self.heap[child_2]])]
            if self.heap[pos] > self.heap[max_child]:
                return
            else:
                pos_val = self.heap[pos]
                child_val = self.heap[max_child]
                self.map[pos_val] = max_child
                self.map[child_val] = pos
                temp = self.heap[pos]
                self.heap[pos] = self.heap[max_child]
                self.heap[max_child] = temp
                pos = max_child
                child_1 = pos * 2 + 1
                child_2 = pos * 2 + 2

    def insert(self, val):
        self.heap.append(val)
        self.len += 1
        self.map[val] = self.len
        self.swap(self.len)

    def delete(self, val):
        if val in self.map:
            pos = self.map[val]
            self.map[self.heap[-1]] = pos
            del self.map[val]
            self.heap[pos] = self.heap[-1]
            self.heap.pop()
            self.len -= 1
            if self.len > 0:
                self.heapify(pos)

    def decrease_key(self, val1, val2):
        pos = self.map[val1]
        self.heap[pos] = val2
        del self.map[val1]
        self.map[val2] = pos
        if val1 > val2:
            self.heapify(pos)
        elif val1 < val2:
            self.swap(pos)

    def get_max(self):
        return self.heap[0]


a = MaxHeap()
a.insert(10)
a.insert(8)
a.insert(9)
a.insert(5)
a.insert(2)
a.insert(7)

a.decrease_key(10, 6)