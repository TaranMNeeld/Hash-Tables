# '''
# Linked List hash table key/value pair
# '''
import hashlib


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        index = self._hash_mod(key)
        pair = LinkedPair(key, value)
        if self.storage[index] is None:
            self.count += 1
            self.storage[index] = pair
        else:
            current = self.storage[index]
            if current.key == key:
                current.value = pair.value
                return
            while current.next is not None:
                current = current.next
                if current.key == key:
                    current.value = pair.value
                    return
            current.next = pair
        if self.count >= self.capacity:
            self.resize()

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            current = self.storage[index]
            if key == current.key:
                self.storage[index] = current.next
                return
            while current.next is not None:
                prev = current
                current = current.next
                if key == current.key:
                    prev.next = current.next
                    return
            return 'Item does not exist'

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            current = self.storage[index]
            if key == current.key:
                return current.value
            while current.next is not None:
                current = current.next
                if key == current.key:
                    return current.value
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.count = 0
        old_storage = self.storage.copy()
        self.capacity *= 2
        self.storage = [None] * self.capacity
        for item in old_storage:
            if item is not None:
                self.insert(item.key, item.value)
                current = item
                while current.next is not None:
                    current = current.next
                    self.insert(current.key, current.value)


if __name__ == "__main__":
    ht = HashTable(2)
    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    ht.insert("line_1", "overwritten")
    ht.insert("line_4", "Tiny hash table")
    ht.insert("something", "Linked list saves the day!")
    ht.insert("line_6", "hello!")
    ht.insert("line_7", "Linked list saves the day!")
    ht.insert("line_8", "testing!")
    ht.insert("something", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
