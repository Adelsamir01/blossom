from linkedlists import LinkedList
from Node import Node
class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]
  def hash(self, key):
    return sum(key.encode())
  def compressor(self, hash_code):
    return hash_code % self.array_size
  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    payload = Node([key,value])
    list_at_array = self.array[array_index]
    key_found = False
    for i in list_at_array:
      if i[0] == key:
        i[1] = value
        key_found = True
        break
    if key_found == False:
      list_at_array.insert(payload)

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    list_at_index = self.array[array_index]
    key_found = False
    for i in list_at_index:
      if i[0] == key:
        return i[1]
        key_found = True
        break
    if key_found == False:
      return None

from blossom_lib import flower_definitions
blossom = HashMap(len(flower_definitions))
for i in flower_definitions:
  blossom.assign(i[0], i[1])

print(blossom.retrieve('daisy'))