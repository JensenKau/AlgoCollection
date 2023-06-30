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


class MSDRadix:
    @classmethod
    def sort(cls, array: List[str]) -> None:
        def sort_aux(array: List[str], start: int, end: int, index: int):
            if start < end:
                buckets = [None] * 27
                
                for i in range(len(buckets)):
                    buckets[i] = Queue()
                
                for i in range(start, end + 1):
                    if index < len(array[i]):
                        alphabet = array[i][index]
                        buckets[ord(alphabet) - ord("a") + 1].insert(array[i])
                    else:
                        buckets[0].insert(array[i])

                pointer = start
                for i in range(len(buckets)):
                    last_pointer = pointer
                    has_items = False
                    
                    while len(buckets[i]) > 0:
                        array[pointer] = buckets[i].pop()
                        pointer += 1
                        has_items = True
                        
                    if i > 0 and has_items:
                        sort_aux(array, last_pointer, pointer - 1, index + 1)
                        
        sort_aux(array, 0, len(array) - 1, 0)
        

if __name__ == "__main__":
    pass