from __future__ import annotations
from typing import List

class StandardQs:
    
    @classmethod
    def sort(cls, array: List[int | float]) -> None:
        StandardQs.quicksort(array, 0, len(array) - 1)
    
    
    @classmethod
    def quicksort(cls, array: List[int | float], start: int, end: int) -> None:
        if start < end:
            point = StandardQs.partition(array, start, end)
            
            StandardQs.quicksort(array, start, point - 1)
            StandardQs.quicksort(array, point + 1, end)    
    
    
    @classmethod
    def partition(cls, array: List[int | float], start: int, end: int) -> int:
        pivot = array[end]
        pointer = start - 1
        
        for i in range(start, end):
            if array[i] <= pivot:
                pointer += 1
                array[i], array[pointer] = array[pointer], array[i]
                
        pointer += 1
        array[end], array[pointer] = array[pointer], array[end]
        
        return pointer
    
    
if __name__ == "__main__":
    pass