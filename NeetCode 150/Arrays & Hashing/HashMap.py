class Node:

    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.map = [Node(0) for i in range(1000)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.map) # Fetching the key
        current = self.map[index] 

        while current.next:
            if current.next.key == key: # If key exist, put value
                current.next.value = value
                return
            current = current.next
        
        current.next = Node(key,value) # Adding the key,value pair

    def get(self, key: int) -> int:
        index = key % len(self.map) # Fetching the key
        current = self.map[index]

        while current.next:
            current = current.next
            if current.key == key:
                return current.value
        return -1


    def remove(self, key: int) -> None:
        index = key % len(self.map)
        current = self.map[index]

        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)