class DynamicArray:
  def __init__(self, size):
    self.count = 0
    self.size = size

    self.storage = [None] * size

   # [None, None, None, None]
   # value: 1

  def append(self, value):
    if self.count == self.size:
      self.resize()

    self.storage[self.count] = value
    self.count += 1

   # [1, 2, 2, 3, 4]
  def insert(self, value, idx):
    # resize if we need
    if self.count == self.size:
      self.resize()

    # move everything over by one
    for i in range(self.count, idx, -1):
      self.storage[i] = self.storage[i - 1]

    self.storage[idx] = value

    self.count += 1

  def resize(self):
    self.size = self.size * 2

    # make a new array, which is double the size of the old array
    # [None, None, None, None, None, None, None, None]
    temp_storage = [None] * self.size

    # copy everything into the new array
    for idx in range(self.size // 2): # can also use self.count
      temp_storage[idx] = self.storage[idx]

    self.storage = temp_storage

arr = DynamicArray(2)
arr.append(1)
arr.append(1)
arr.append(1)
print(arr.storage)