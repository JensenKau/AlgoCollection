from __future__ import annotations
from typing import Any

class LinkedList:
    class LinkedNode:
        def __init__(self, item: Any = None, next: LinkedList.LinkedNode = None) -> None:
            self.item = item
            self.next = next
        
    
    def __init__(self) -> None:
        self.root = None
        self.tail = None
        self.size = 0
    
    
    def __getitem__(self, index: int) -> Any:
        if index >= 0 and index < self.size:
            i = 0
            current = self.root
            while i <= index:
                if i == index:
                    return current.item
                i += 1
                current = current.next
        
        raise IndexError("Index out of range")
    
    
    def __setitem__(self, index: int, value: Any) -> None:
        if index >= 0 and index < self.size:
            i = 0
            current = self.root
            while i <= index:
                if i == index:
                    current.item = value
                i += 1
                current = current.next
        else:
            raise IndexError("Index out of range")
    
    
    def __contains__(self, value: Any) -> bool:
        current = self.root
        
        while self.root is not None:
            if current.item == value:
                return True
            current = current.next
            
        return False
    
    
    def __len__(self) -> int:
        return self.size
    
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    
    def append(self, value: Any) -> None:
        temp = LinkedList.LinkedNode(value)
        
        if self.root is None:
            self.root = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
            
        self.size += 1
    
    
    def insert(self, index: int, value: Any) -> None:
        if index == self.size:
            self.append(value)
        elif index >= 0 and index < self.size:
            temp = LinkedList.LinkedNode(value)
            
            if index == 0:
                temp.next = self.root
                self.root = temp
            else:
                i = 0
                current = self.root
                while i < index:
                    if i == index - 1:
                        temp.next = current.next
                        current.next = temp
                        break
                    i += 1
                    current = current.next
            self.size += 1
        else:
            raise IndexError("Index out of range")
    
    
    def remove(self, value: Any) -> None:
        if self.root is not None:
            current = self.root
            
            if current.item == value:
                self.root = current.next
                self.size -= 1
            else:
                while current.next is not None:
                    if current.next.item == value:
                        current.next = current.next.next
                        self.size -= 1
                        break
                    current = current.next

    
    def remove_at(self, index: int) -> Any:
        if index >= 0 and index < self.size:
            if index == 0:
                self.root = self.root.next
            else:
                i = 0
                current = self.root
                while i < index:
                    if i == index - 1:
                        current.next = current.next.next
                        break
                    i += 1
                    current = current.next
            self.size -= 1
        else:
            raise IndexError("Index out of range")
    
    
    def __str__(self) -> str:
        temp = [None] * self.size
        
        i = 0
        current = self.root
        while i < self.size:
            temp[i] = str(current.item)
            i += 1
            current = current.next
            
        return f"[{', '.join(temp)}]"
    
    
if __name__ == "__main__":
    pass