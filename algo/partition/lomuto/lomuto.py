from __future__ import annotations
from typing import List

class LomutoPartition:
    
    @classmethod
    def partition(cls, array: List[int | float]) -> int:
        pivot = array[-1]
        pointer = -1
        
        for i in range(len(array) - 1):
            if array[i] <= pivot:
                pointer += 1
                array[i], array[pointer] = array[pointer], array[i]
        
        pointer += 1
        array[pointer], array[-1] = array[-1], array[pointer]
    
        return pointer
    

if __name__ == "__main__":
    pass