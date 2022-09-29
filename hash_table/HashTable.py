class Node:
    def __init__(self, key, value, next=None):
        self._key = key
        self.value = value
        self.next = None

    @property
    def key(self):
        return self._key


class HashTable:
    def __init__(self, size: int) -> None:
        self.buffer = [None for i in range(size)]
        self.m = size

    @staticmethod
    def _search_from_list(lst: Node, key):
        count = -1
        cur = lst
        while cur is not None:
            count += 1
            if cur.key == key:
                return count, cur.value
            else:
                cur = cur.next
        return -1, None

    def _get_idx(self, key):
        hash_key = hash(key) % self.m
        key_idx, val = self._search_from_list(self.buffer[hash_key], key)
        return hash_key, key_idx, val

    def insert(self, key, val) -> None:
        hash_key, key_idx = self._get_idx(key)
        if key_idx >= 0:
            self.buffer[hash_key][key_idx] = (key, val)
        else:
            self.buffer[hash_key].append((key, val))

    def find(self, key):
        hash_key, key_idx = self._get_idx(key)
        if key_idx == -1:
            return False, None
        else:
            return True, self.buffer[hash_key][key_idx][1]

    def delete(self, key):
        hash_key, key_idx = self._get_idx(key)
        if key_idx == -1:
            raise Exception("key does not exist")
        else:
            _ = self.buffer[hash_key].pop(key_idx)

    def print(self):
        for i in self.buffer:
            print(i)


ht = HashTable(5)

ht.insert(3, 7)
ht.insert('a', 1)

ht.print()

ht.insert(3, 4)
ht.print()

ht.find(3)
ht.find(5)

ht.delete(3)
ht.print()