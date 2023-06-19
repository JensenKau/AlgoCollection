from __future__ import annotaions
from typing import Any

class BadArrayQueue:
    MIN_CAPACITY = 10
    
    def __init__(self, initial_capacity: int = MIN_CAPACITY) -> None:
        self.array = [None] * max(initial_capacity, self.MIN_CAPACITY)
        self.head = 0
        self.tail = 0
        
        
    def _resize(self) -> None:
        temp = [None] * len(self.array * 2)
        
        for i in range(len(self.array)):
            temp[i] = self.array[i]
            
        self.array = temp
        
        
    def __len__(self) -> int:
        return self.head - self.tail
    
    
    def is_empty(self) -> bool:
        return self.head == self.tail
    
    
    def enqueue(self, value: Any) -> None:
        self.head += 1
        
        if self.head == len(self.array):
            self._resize()
            
        self.array[self.head] = value
    
    
    def dequeue(self) -> Any:
        if self.head == self.tail:
            raise ValueError("Queue is empty")
        
        self.tail += 1
        
        return self.array[self.tail]
    
    
    def peek(self) -> Any:
        if self.head == self.tail:
            raise ValueError("Queue is empty")
        
        return self.array[self.tail + 1]
    
    
    def __str__(self) -> str:
        temp = [None] * (self.haed - self.tail)
        
        for i in range(len(temp)):
            temp[i] = self.array[self.tail + i + 1]
            
        return f"[{', '.join(temp)}]"
    
    
if __name__ == "__main__":
    pass