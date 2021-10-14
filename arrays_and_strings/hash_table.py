
#############################################################################
################## This is my implementation of Hashtable ###################
# deck is used as a linked list takes O(1) for insertion and deleting; retreival or searching element takes O(n)
from collections import deque


class hashTable():
    def __init__(self):
        self._len_items = 5
        self._items = [None] * self._len_items

    def _hashing(self, key=None):
        try:
            hash_value = self._convert_text_int(
                key) if type(key) == str else int(key)
            return hash_value % self._len_items
        except TypeError:
            raise TypeError(f"{key} isn't valid")

    def _convert_text_int(self, text):
        return sum(ord(char) for char in text)

    def insert(self, key, value):
        index = self._hashing(key)

        if self._items[index] is None:
            self._items[index] = deque()
            self._items[index].append([key, value])
        elif self._items[index][0][0] == key:
            self._items[index][0][1] = value

        else:
            # store both key and value into linked list node
            # do we insert only value or both value and key
            self._items[index].append([key, value])

    def get(self, key):
        index = self._hashing(key)
        if self._items[index]:
            for i in self._items[index]:
                if i[0] == key:
                    return i[1]
                else:
                    return None
        else:
            print("No values have assigned yet")

    def delete(self, key):
        index = self._hashing(key)
        for i in range(len(self._items[index])):
            if self._items[index][i][0] == key:
                del self._items[index][i]
            else:
                return None


if __name__ == "__main__":
    # s = "any word"
    ht = hashTable()
    ht.insert('mohamed tarek', 500)
    ht.insert('mohamed taek', 5000)
    ht.insert(' taek', 3)
    print(ht._items)
    #  x = [None] * 6
    #  x[3] = '5'
    #  print(x)
