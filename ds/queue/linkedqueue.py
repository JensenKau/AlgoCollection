from __future__ import annotations
from typing import Any

class LinkedQueue:
    class LinkedNode:
        def __init__(self, item: Any = None, next: Any = None) -> None:
            self.item = item
            self.next = next
    
    
    def __init__(self) -> None:
        self.root = None
        self.head = None
        self.tail = None
        self.size = 0
    
    
    def __len__(self) -> int:
        return self.size
    
    
    def is_empty(self) -> bool:
        return self.size == 0
    
    
    def enqueue(self, value: Any) -> None:
        current = LinkedQueue.LinkedNode(value)
        
        if self.tail is None:
            self.head = current
            self.tail = current
        else:
            self.head.next = current
            self.head = self.head.next
            
        self.size += 1
            
    
    def dequeue(self) -> Any:
        if self.size == 0:
            raise ValueError("Queue is empty")
        
        output = self.tail.item
        self.tail = self.tail.next
        self.size -= 1
        
        return output
    
    
    def peek(self) -> Any:
        if self.size == 0:
            raise ValueError("Queue is empty")
        
        return self.tail.item
    
    
    def __str__(self) -> str:
        temp = [None] * self.size
        
        current = self.tail
        for i in range(len(temp)):
            temp[i] = current.item
            current = current.next
            
        return f"[{', '.join(temp)}]"
    
    
if __name__ == "__main__":
    pass