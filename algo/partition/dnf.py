from __future__ import annotations
from typing import List, Tuple

class DutchNationalFlagPartition:
    
    @classmethod
    def partition(cls, array: List[int | float]) -> Tuple[int, int]:
        pivot = array[-1]
        start = -1
        end = len(array)
        pointer = 0
        
        while pointer < end:
            if array[pointer] < pivot:
                start += 1
                array[pointer], array[start] = array[start], array[pointer]
                pointer += 1
                
            elif array[pointer] > pivot:
                end -= 1
                array[pointer], array[end] = array[end], array[pointer]
                
            else:
                pointer += 1
                            
        return start, end
            
    

if __name__ == "__main__":
    pass