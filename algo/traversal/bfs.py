from __future__ import annotations
from typing import List, Any

class BreadthFirstSearch:
    class Counter:
        def __init__(self) -> None:
            self.counter = 0
            
        def retrieve(self) -> int:
            self.counter += 1
            return self.counter
        
        
    class LinkedNode:
        def __init__(self, item: Any = None, next: BreadthFirstSearch.LinkedNode = None) -> None:
            self.item = item
            self.next = next
    
    
    @classmethod
    def search(cls, array: List[List[int]]) -> List[List[int]]:
        head = BreadthFirstSearch.LinkedNode((0, 0))
        tail = head
        counter = BreadthFirstSearch.Counter()
        
        output = [None] * len(array)
        
        for i in range(len(output)):
            output[i] = [0] * len(array[0])
        
        while tail is not None:
            row = tail.item[0]
            col = tail.item[1]
            
            if (row >= 0 and row < len(output)) and (col >= 0 and col < len(output[0])) and output[row][col] <= 0:
                output[row][col] = counter.retrieve()
                
                head.next = BreadthFirstSearch.LinkedNode((row + 1, col))
                head = head.next
                head.next = BreadthFirstSearch.LinkedNode((row - 1, col))
                head = head.next
                head.next = BreadthFirstSearch.LinkedNode((row, col + 1))
                head = head.next
                head.next = BreadthFirstSearch.LinkedNode((row, col - 1))
                head = head.next
                
            tail = tail.next
                
        return output
                
    
if __name__ == "__main__":
    pass