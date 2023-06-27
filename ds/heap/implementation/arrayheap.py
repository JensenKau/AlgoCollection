from __future__ import annotations
from typing import List

class ArrayHeap:
    def __init__(self, array: List[int] = None) -> None:
        self.array = [None] * (len(array) + 1)
        self.size = len(array)
        
        for i in range(len(array)):
            self.array[i + 1] = array[i]
            
        self.__heapify()
    
    
    def __len__(self) -> int:
        return self.size
    
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    
    def __resize(self) -> None:
        temp = [None] * (len(self.array) * 2)
        
        for i in range(self.size + 1):
            temp[i] = self.array[i]
            
        self.array = temp
    
    
    def __smaller_child(self, index: int) -> int:
        if index * 2 + 1 <= self.size:
            if self.array[index * 2] <= self.array[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1
        else:
            return index * 2
        
    
    def __sink(self, index: int) -> None:
        while index * 2 <= self.size:
            smaller_child_index = self.__smaller_child(index)
                
            if self.array[index] > self.array[smaller_child_index]:
                self.array[index], self.array[smaller_child_index] = self.array[smaller_child_index], self.array[index]
                index = smaller_child_index
            else:
                break
    
    
    def __rise(self, index: int) -> None:
        while index > 1:
            if self.array[index] < self.array[index // 2]:
                self.array[index], self.array[index // 2] = self.array[index // 2], self.array[index]
                index = index // 2
            else:
                break
    
        
    def __heapify(self) -> None:
        for i in range(len(self.array) // 2, 0, -1):
            self.__sink(i)
    
    
    def insert(self, num: int) -> None:
        if self.size == len(self.array) - 1:
            self.__resize()
            
        self.size += 1
        self.array[self.size] = num
        
        self.__rise(self.size)
    
    
    def pop(self) -> int:
        if self.size == 0:
            raise ValueError("Heap is empty")
        
        output = self.array[1]
        
        self.array[1], self.array[self.size] = self.array[self.size], self.array[1]
        self.size -= 1 
        self.__sink(1)
        
        return output
    
    
    def peek(self) -> int:
        if self.size == 0:
            raise ValueError("Heap is empty")
        
        return self.array[1]
    
    
    def __str__(self) -> str:
        temp = [None] * self.size
        
        for i in range(len(temp)):
            temp[i] = self.array[i + 1]
            
        return f"[{', '.join(temp)}]"
    
    
if __name__ == "__main__":
    pass