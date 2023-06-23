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
    array = [7, 6, 1, 7, 9, 8, 9, 8, 8, 8, 8, 3, 3, 10, 7, 10, 6, 10, 10, 4]
    
    print(array)
    
    res = LomutoPartition.partition(array)
    
    print(array)
    print(res)