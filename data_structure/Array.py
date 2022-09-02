class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, idx):
        if idx < self.length:
            return self.data[idx]
        else:
            raise Exception('index out of range')

    def insert(self, idx, val):
        if (idx < self.length) | (self.length == 0):
            length = self.length + 1
            next_idx = length - 1
            while next_idx > idx:
                self.data[next_idx] = self.data[next_idx - 1]
                next_idx -= 1
            self.data[idx] = val
            self.length = length
        else:
            raise Exception('index out of range')

    def delete(self, idx):
        assert idx < self.length, 'index out of range'
        while idx < self.length - 1:
            self.data[idx] = self.data[idx + 1]
            idx += 1
        del self.data[self.length - 1]
        self.length -= 1

    def pop(self):
        assert self.length > 0, 'cannot perform on empty array'
        val = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return val

    def push(self, val):
        self.data[self.length] = val
        self.length += 1



a = MyArray()

# a.pop()

a.insert(0, 1)
print(a.data)

a.insert(0, 2)
print(a.data)

a.insert(1, 3)
print(a.data)

a.get(0)

a.delete(1)
print(a.data)

a.delete(2)
print(a.length)

a.pop()
print(a.length)

a.push(4)
print(a.data)