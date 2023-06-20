from __future__ import annotations
from typing import Any

class ArrayQueue:
    MIN_CAPACITY = 10
    
    def __init__(self, initial_capacity: int = MIN_CAPACITY) -> None:
        self.array = [None] * max(initial_capacity, self.MIN_CAPACITY)
        self.tail = 0
        self.head = 0
        
        
    def _resize(self) -> None:
        temp = [None] * (len(self.array) * 2)
        
        for i in range(1, len(temp)):
            temp[i] = self.array[(self.tail + i) % len(self.array)]
            
            if (self.tail + i) % len(self.array) == self.head:
                self.head = i
                self.tail = 0
                break
        
        self.array = temp
    
    
    def __len__(self) -> int:
        if self.head > self.tail:
            return self.head - self.tail
        elif self.head < self.tail:
            return self.head - (self.tail - len(self.array) - 1)
        
        return 0
    
    
    def is_empty(self) -> bool:
        return self.head == self.tail
    
    
    def enqueue(self, value: Any) -> None:        
        if (self.head + 1) % len(self.array) == self.tail:
            self._resize()
            
        self.head = (self.head + 1) % len(self.array)
        
        self.array[self.head] = value
    
    
    def dequeue(self) -> Any:
        if self.head == self.tail:
            raise ValueError("Queue is empty")
        
        self.tail = (self.tail + 1) % len(self.array)
        
        return self.array[self.tail]
    
    
    def peek(self) -> Any:
        if self.head == self.tail:
            raise ValueError("Queue is empty")
        
        return self.array[(self.tail + 1) % len(self.array)]
    
    
    def __str__(self) -> str:
        temp = [None] * len(self)
        
        for i in range(len(temp)):
            temp[i] = self.array[(self.tail + i + 1) % len(self.array)]
        
        return f"[{', '.join(temp)}]"
    
    
if __name__ == "__main__":
    pass