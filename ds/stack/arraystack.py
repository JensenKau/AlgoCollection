from __future__ import annotations
from typing import Any

class ArrayStack:
    MIN_CAPACITY = 10
    
    def __init__(self, intitial_capacity: int = MIN_CAPACITY) -> None:
        self.array = [None] * max(intitial_capacity, self.MIN_CAPACITY)
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
    
    
    def push(self, value: Any) -> None:
        self.pointer += 1
        
        if self.pointer == len(self.array):
            self.__resize()
            
        self.array[self.pointer] = value
    
    
    def pop(self) -> Any:
        if self.pointer == -1:
            raise ValueError("Stack is empty")
        
        temp = self.array[self.pointer]
        self.pointer -= 1 
        
        return temp
    
    
    def peek(self) -> Any:
        if self.pointer == -1:
            raise ValueError("Stack is empty")
        
        return self.array[self.pointer]
    
    
    def __str__(self) -> str:
        temp = [None] * (self.pointer + 1)
        
        for i in range(len(temp)):
            temp[i] = str(self.array[i])
            
        return f"[{', '.join(temp)}]"
    

if __name__ == "__main__":
    pass