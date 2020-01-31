# '''
# Linked List hash table key/value pair
# '''
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
    self.count = 0
    self.capacity = capacity  # Number of buckets in the hash table
    self.storage = [None] * capacity
    self.ll = None

  def _hash(self, key):
    '''
    Hash an arbitrary key and return an integer.

    You may replace the Python hash with DJB2 as a stretch goal.
    '''

    def hash(key):
      total = 0

      for char in key:
        val = ord(char)
        total += val

      # print(total)
      return total

    # this line is stupid shit
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
    # self.capacity = capacity  # Number of buckets in the hash table
    # self.storage = [None] * capacity
    '''
    Store the value with the given key.

    Hash collisions should be handled with Linked List Chaining.

    Fill this in.
    '''
    if self.count == self.capacity:
      self.resize()

    hashedIndex = self._hash_mod(key)

    if self.storage[hashedIndex] != None:
      print('Warning: collision')

    self.storage[hashedIndex] = value
    self.count += 1

    if self.ll == None:
      self.ll = LinkedPair(key, value)
    else:
      current = self.ll
      while current.next is not None:
        current = current.next

      current.next = LinkedPair(key, value)

  def remove(self, key):
    '''
    Remove the value stored with the given key.

    Print a warning if the key is not found.

    Fill this in.
    '''
    pass

  def retrieve(self, key):
    '''
    Retrieve the value stored with the given key.

    Returns None if the key is not found.

    Fill this in.
    '''
    hashedIndex = self._hash_mod(key)

    if self.storage[hashedIndex] != None:
      return self.storage[hashedIndex]
    else:
      return None

  def resize(self):
    '''
    Doubles the capacity of the hash table and
    rehash all key/value pairs.

    Fill this in.
    '''
    self.capacity = self.capacity * 2

    temp_storage = [None] * self.capacity

    # unshit this if i have time later
    for idx in range(self.capacity // 2):
      temp_storage[idx] = self.storage[idx]

    self.storage = temp_storage

if __name__ == "__main__":
  ht = HashTable(2)

  ht.insert('bob', 10)
  ht.insert('joe', 11)

  ht.insert('ada', 12)

  print(ht.storage)
  print(ht.ll.next.value)

  # print(ht._hash_mod('bob'))
  # print(ht._hash_mod('boo'))
  # ht.insert("line_1", "Tiny hash table")
  # ht.insert("line_2", "Filled beyond capacity")
  # ht.insert("line_3", "Linked list saves the day!")

  # print("")

  # # Test storing beyond capacity
  # print(ht.retrieve("line_1"))
  # print(ht.retrieve("line_2"))
  # print(ht.retrieve("line_3"))

  # # Test resizing
  # old_capacity = len(ht.storage)
  # ht.resize()
  # new_capacity = len(ht.storage)

  # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

  # # Test if data intact after resizing
  # print(ht.retrieve("line_1"))
  # print(ht.retrieve("line_2"))
  # print(ht.retrieve("line_3"))

  # print("")
