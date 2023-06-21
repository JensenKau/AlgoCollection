from __future__ import annotations
from typing import List
from math import inf

class CountingSort:
    
    @classmethod
    def sort(cls, array: List[int]) -> None:
        min_value = inf
        max_value = -inf
        temp = None
        array_pointer = 0
        
        for i in range(len(array)):
            if array[i] < min_value:
                min_value = array[i]
            if array[i] > max_value:
                max_value = array[i]
                
        temp = [0] * (max_value - min_value + 1)
        
        for i in range(len(array)):
            temp[array[i] - min_value] += 1
            
        for i in range(len(temp)):
            while temp[i] > 0:
                array[array_pointer] = i + min_value
                array_pointer += 1
                temp[i] -= 1
                
if __name__ == "__main__":
    pass