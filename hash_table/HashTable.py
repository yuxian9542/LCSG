class HashTable:
    def __init__(self, size: int) -> None:
        self.buffer = [[] for i in range(size)]
        self.m = size

    @staticmethod
    def _search_from_list(lst: list, key):
        for idx, key_val_pair in enumerate(lst):
            if key_val_pair[0] == key:
                return idx
        return -1

    def _get_idx(self, key):
        hash_key = hash(key) % self.m
        key_idx = self._search_from_list(self.buffer[hash_key], key)
        return hash_key, key_idx

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