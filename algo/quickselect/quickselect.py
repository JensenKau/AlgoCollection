from __future__ import annotations
from typing import List

class QuickSelect:
    
    @classmethod
    def select(cls, array: List[int | float], k: int) -> int | float:
        return QuickSelect.select_aux(array, k, 0, len(array) - 1)
    
    
    @classmethod
    def select_aux(cls, array: List[int | float], k: int, start: int, end: int) -> int | float:
        point = QuickSelect.partition(array, start, end)
        
        if point == k:
            return array[point]
        elif k < point:
            return QuickSelect.select_aux(array, k, start, point - 1)
        else:
            return QuickSelect.select_aux(array, k, point + 1, end)
            
    
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