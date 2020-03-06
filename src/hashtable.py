# remove and resize aren't adapted to ll stuff, but tests are 
# passing as they were b4 the ll refactor

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

  def _hash(self, key):
    '''
    Hash an arbitrary key and return an integer.

    You may replace the Python hash with DJB2 as a stretch goal.
    '''

    def hash(key):
      total = 0

      prime = 5831
      for char in key:
        val = ord(char)
        total += val * prime

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

# o(n) if there's a clash and something has to be added to an existing ll
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
      print('Collision: creating or adding to LL')

      # update value thats not in an ll yet
      if not isinstance(self.storage[hashedIndex], LinkedPair) and self.storage[hashedIndex][0] == key:
        self.storage[hashedIndex] = (key, value)  

      # if ll is necessary to resolve a clash but ll doesnt exist yet
      elif not isinstance(self.storage[hashedIndex], LinkedPair):
        # create a ll for this area using existing values
        # then add the new key and val to it, too

        ll = LinkedPair(self.storage[hashedIndex][0], self.storage[hashedIndex][1])        
        self.storage[hashedIndex] = ll
        ll.next = LinkedPair(key, value)

      # if an ll exists in this location and we need to update a node within it
      else:
        # the ll
        current = self.storage[hashedIndex]
        while current is not None:
          if current.key == key:
            break
          current = current.next

        # if current.next == None, add new thing to the next property

        if current.next == None and current.key != key:
          current.next = LinkedPair(key, value)
        else:
          nextNode = current.next
          current.key = key
          current.value = value
          current.next = nextNode

    else:
      self.storage[hashedIndex] = (key, value)
      self.count += 1

  def remove(self, key):
    '''
    Remove the value stored with the given key.

    Print a warning if the key is not found.

    Fill this in.
    '''
    hashedIndex = self._hash_mod(key)

    if self.storage[hashedIndex] != None:
      self.storage[hashedIndex] = None
    else:
      print('key not found')

# clashes are o(n), otherwise o(1)
# if i dont consider the loop in the hash func
  def retrieve(self, key):
    '''
    Retrieve the value stored with the given key.

    Returns None if the key is not found.

    Fill this in.
    '''
    hashedIndex = self._hash_mod(key)

    if self.storage[hashedIndex] != None:
      # if its a ll i need to loop through it to find the specific key

      if isinstance(self.storage[hashedIndex], LinkedPair):
        current = self.storage[hashedIndex]
        while current.key != key:
          current = current.next

        return current.value

      else:
        return self.storage[hashedIndex][1]
    else: 
      return None

  def resize(self):
    '''
    Doubles the capacity of the hash table and
    rehash all key/value pairs.

    Fill this in.
    '''

    # 
    self.capacity = self.capacity * 2

    temp_storage = [None] * self.capacity

    # unshit this if i have time later
    for idx in range(self.capacity // 2):
      # print('l', self.storage)

      if self.storage[idx] is not None:
        hashedIndex = self._hash_mod(self.storage[idx][0])

        if temp_storage[hashedIndex] != None:
          print('Warning: collision resize')

        temp_storage[hashedIndex] = (self.storage[idx][0], self.storage[idx][1])

      # rehash here.
      # temp_storage[idx] = self.storage[idx]

    self.storage = temp_storage

if __name__ == "__main__":
  ht = HashTable(2)

  # # ll = LinkedPair('bob', 3)
  # # print(isinstance(ll, LinkedPair))

  ht.insert('bob', 10)
  ht.insert('joe', 11)
  ht.insert('ada', 12)
  ht.insert('ada', 13)
  print(ht.storage)
  # print(ht.retrieve('ada'))

  # see all keys in an index that is an ll
  current = ht.storage[2]
  while current is not None:
    print(current.key, current.value)
    current = current.next

  # ht.resize()


  # print(ht.storage)

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

# [x, None, None, x]
# 