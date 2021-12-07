def hash_func(key):
    return ord(key[0]) % 10


class HashTable:
    def __init__(self):
        self.table = [None] * 10

    def set(self, key, value):
        self.table[hash_func(key)] = value

    def get(self, key):
        return self.table[hash_func(key)]


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


class ChainedHashTable(HashTable):
    def __init__(self, key, data):
        super().__init__(key, data)

    def save_data(data, value):
        index_key = get_key(data)
        hash_address = hash_function(index_key)
        if hash_table[hash_address] != 0:
            for index in range(hash_address, len(hash_table)):
                if hash_table[index] == 0:
                    hash_table[index] = [index_key, value]
                    return
                elif hash_table[index][0] == index_key:
                    hash_table[index][1] = value
                    return
        else:
            hash_table[hash_address] = [index_key, value]

    def read_data(data):
        index_key = get_key(data)
        hash_address = hash_function(index_key)

        if hash_table[hash_address] != 0:
            for index in range(hash_address, len(hash_table)):
                if hash_table[index] == 0:
                    return None
                elif hash_table[index][0] == index_key:
                    return hash_table[index][1]
        else:
            return None


# Test code

ht = ChainedHashTable()
ht.set('hello', 1)
ht.set('hello2', 2)
ht.set('hello3', 3)
ht.set('hello4', 4)

print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')
print()

ht.set('hello2', 5)

print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')