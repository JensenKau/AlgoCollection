from __future__ import annotations
from typing import List, Tuple

class DNFLomutoPartition:
    
    @classmethod
    def partition(cls, array: List[int | float]) -> Tuple[int, int]:
        pivot = array[-1]
        pointer = -1
        
        for i in range(len(array) - 1):
            if array[i] <= pivot:
                pointer += 1
                array[i], array[pointer] = array[pointer], array[i]
        
        pointer += 1
        array[pointer], array[-1] = array[-1], array[pointer]
        
        left = pointer
        
        for i in range(len(array)):
            if array[i] == pivot:
                left -= 1
                array[i], array[left] = array[left], array[i]
                
            if i >= left - 1:
                break
            
    
        return left, pointer
    

if __name__ == "__main__":
    pass