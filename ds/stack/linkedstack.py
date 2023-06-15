from __future__ import annotations
from typing import Any

class LinkedStack:
    class LinkedNode:
        def __init__(self, previous: LinkedStack.LinkedNode = None, item: Any = None, next: LinkedStack.LinkedNode = None) -> None:
            self.previous = previous
            self.item = item
            self.next = next
    
    
    def __init__(self) -> None:
        self.root = None
        self.end = None
        self.size = 0
    
    
    def __len__(self) -> int:
        return self.size
    
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    
    def push(self, value: Any) -> None:
        if self.root is None:
            self.root = LinkedStack.LinkedNode(None, value)
            self.end = self.root
        else:
            self.end.next = LinkedStack.LinkedNode(self.end, value)
            self.end = self.end.next
        
        self.size += 1
    
    
    def pop(self) -> Any:
        if self.size == 0:
            raise ValueError("Stack is empty")
        
        output = self.end.item
        self.end = self.end.previous
        self.end.next = None
        self.size -= 1
        
        return output
    
    
    def peek(self) -> Any:
        if self.size == 0:
            raise ValueError("Stack is empty")
        
        return self.end.item
    
    
    def __str__(self) -> str:
        temp = [None] * self.size
        
        i = 0
        current = self.root
        while current is not None:
            temp[i] = str(current.item)
            current = current.next
            i += 1
            
        return f"[{', '.join(temp)}]"
    
    
if __name__ == "__main__":
    pass