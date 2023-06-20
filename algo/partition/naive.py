from __future__ import annotations
from typing import List, Tuple

class NaivePartition:
    
    @classmethod
    def partition(cls, array: List[int | float]) -> Tuple[int, int]:
        less = []
        equal = []
        more = []
        pointer = 0
        out_left = 0
        out_right = 0
        
        for i in range(len(array)):
            if array[i] < array[-1]:
                less.append(array[i])
            elif array[i] == array[-1]:
                equal.append(array[i])
            else:
                more.append(array[i])
                
        for i in range(len(less)):
            array[pointer] = less[i]
            pointer += 1
            
        for i in range(len(equal)):
            if i == 0:
                out_left = pointer
            if i == len(equal) - 1:
                out_right = pointer
            
            array[pointer] = equal[i]
            pointer += 1
            
        for i in range(len(more)):
            array[pointer] = more[i]
            pointer += 1
            
        return out_left, out_right
    

if __name__ == "__main__":
    pass