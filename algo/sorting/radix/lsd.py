from __future__ import annotations
from typing import List, Any

class Queue:
    class Node:
        def __init__(self, item: Any) -> None:
            self.item = item
            self.next = None
        
            
    def __init__(self) -> None:
        self.tail = None
        self.head = None
        self.size = 0
        
        
    def __len__(self) -> int:
        return self.size
    
    
    def insert(self, item: Any) -> None:
        node = Queue.Node(item)
        
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.head.next = node
            self.head = self.head.next
            
        self.size += 1
        
    
    def pop(self) -> Any:
        if self.size == 0:
            raise ValueError("Queue is emtpy")
        
        output = self.tail.item
        
        self.tail = self.tail.next
        self.size -= 1
        
        return output


class LSDRadix:
    @classmethod
    def sort(cls, array: List[str]) -> None:
        max_length = 0
        buckets = [None] * 27
        
        for i in range(len(array)):
            max_length = max(len(array[i]), max_length)
            
        max_length -= 1
            
        for i in range(len(buckets)):
            buckets[i] = Queue()
            
        while max_length >= 0:
            for i in range(len(array)):
                if max_length < len(array[i]):
                    alphabet = array[i][max_length]
                    buckets[ord(alphabet) - ord("a") + 1].insert(array[i]) 
                else:
                    buckets[0].insert(array[i])
                    
            pointer = 0
            for i in range(len(buckets)):
                while len(buckets[i]) > 0:
                    array[pointer] = buckets[i].pop()
                    pointer += 1
            
            max_length -= 1
        
            
if __name__ == "__main__":
    pass