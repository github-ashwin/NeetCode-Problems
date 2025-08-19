class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arraylist = [0]*capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arraylist[i]

    def set(self, i: int, n: int) -> None:
        self.arraylist[i]=n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arraylist[self.length] = n
        self.length+=1

    def popback(self) -> int:
        val = self.arraylist[self.length - 1]
        self.length -= 1
        return val


    def resize(self) -> None:
        self.capacity = 2*self.capacity
        new_arr = [0]*self.capacity
        for i in range(self.length):
            new_arr[i] = self.arraylist[i]
        self.arraylist = new_arr


    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity