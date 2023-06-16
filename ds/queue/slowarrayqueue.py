from __future__ import annotations
from typing import Any

class SlowArrayQueue:
    MIN_CAPACITY = 10
    
    def __init__(self, initial_capacity: int = MIN_CAPACITY) -> None:
        self.array = [None] * max(initial_capacity, self.MIN_CAPACITY)
        self.pointer = -1
    
    
    def __resize(self) -> None:
        temp = [None] * (len(self.array) * 2)
        
        for i in range(len(self.array)):
            temp[i] = self.array[i]
            
        self.array = temp
    
    
    def __len__(self) -> int:
        return self.pointer + 1
    
    
    def is_empty(self) -> bool:
        return self.pointer == -1
    
    
    def enqueue(self, value: Any) -> None:
        self.pointer += 1
        
        if self.pointer == len(self.array):
            self.__resize()
            
        self.array[self.pointer] = value
    
    
    def dequeue(self) -> Any:
        if self.pointer == -1:
            raise ValueError("Queue is empty")
        
        output = self.array[0]
        
        for i in range(1, self.pointer + 1):
            self.array[i - 1] = self.array[i]
            
        self.pointer -= 1
        
        return output
    
    
    def peek(self) -> Any:
        if self.pointer == -1:
            raise ValueError("Queue is empty")
        
        return self.array[self.pointer]
    
    
    def __str__(self) -> str:
        temp = [None] * (self.pointer + 1)
        
        for i in range(len(temp)):
            temp[i] = self.array[i]
        
        return f"[{', '.join(temp)}]"
    
    
if __name__ == "__main__":
    pass