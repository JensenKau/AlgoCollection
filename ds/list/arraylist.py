from __future__ import annotations
from typing import Any

class ArrayList:
    MIN_CAPACITY = 10
    
    def __init__(self, initial_capacity: int = MIN_CAPACITY) -> None:
        self.array = [None] * max(self.MIN_CAPACITY, initial_capacity)
        self.pointer = -1
        
        
    def __is_max(self) -> bool:
        return self.pointer >= len(self.array) - 1
    
    
    def __resize(self) -> None:
        temp = [None] * (len(self.array) * 2)
        
        for i in range(len(self.array)):
            temp[i] = self.array[i]
            
        self.array = temp
    
        
    def __getitem__(self, index: int) -> Any:
        if index >= 0 and index <= self.pointer:
            return self.array[index]
        
        raise IndexError("Index out of range")
    
    
    def __setitem__(self, index: int, value: Any) -> None:
        if index >= 0 and index <= self.pointer:
            self.array[index] = value
        else:
            raise IndexError("Index out of range")
        
        
    def __contains__(self, value: Any) -> bool:
        for i in range(self.pointer + 1):
            if value == self.array[i]:
                return True
        return False
    
    
    def __len__(self) -> int:
        return self.pointer + 1
    
    
    def is_empty(self) -> bool:
        return self.pointer == -1
    
    
    def append(self, value: Any) -> None:
        if self.__is_max():
            self.__resize()
        
        self.pointer += 1
        self.array[self.pointer] = value
    
    
    def insert(self, index: int, value: Any) -> None:
        if self.__is_max():
            self.__resize()
        
        if index >= 0 and index <= self.pointer + 1:
            current_index = self.pointer + 1
            
            while current_index > index:
                self.array[current_index] = self.array[current_index - 1]
                current_index -= 1
                
            self.pointer += 1
            self.array[index] = value 
        else:
            raise IndexError("Index out of range")
    
    
    def remove(self, value: Any) -> None:
        found = False
        
        i = 0
        while i <= self.pointer:
            if found:
                self.array[i - 1] = self.array[i]
            else:
                if value == self.array[i]:
                    found = True
            
            i += 1
            
        if found:
            self.pointer -= 1
    
    
    def remove_at(self, index: int) -> Any:
        if index >= 0 and index <= self.pointer:
            i = index
            while i < self.pointer:
                self.array[i] = self.array[i + 1]
                i += 1
                
            self.pointer -= 1
            
        else:
            raise IndexError("Index out of range")
    
        
    def __str__(self) -> str:
        temp = [None] * (self.pointer + 1)
        
        i = 0
        while i <= self.pointer:
            temp[i] = str(self.array[i])
            i += 1
            
        return f"[{', '.join(temp)}]"
        
        
if __name__ == "__main__":
    pass