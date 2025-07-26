class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)] # HashSet using LinkedList

    def add(self, key: int) -> None:
        index = key % len(self.set) # Getting the index value of the key
        current = self.set[index] # Getting the current node

        while current.next:
            if current.next.key == key: # Checking for duplicate
                return 
            current = current.next # Reaching the last node(key) in the index
        
        current.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % len(self.set) # Getting the index value of the key
        current = self.set[index]

        while current.next:
            if current.next.key == key:
                current.next = current.next.next # Shifting the key to next
                return
            current = current.next

    def contains(self, key: int) -> bool:
        index = key % len(self.set) # Getting the index value of the key
        current = self.set[index]

        while current.next:
            if current.next.key == key: # Checking if the key exist
                return True
            current = current.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)