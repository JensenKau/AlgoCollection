from __future__ import annotations
from typing import List

class HoarePartition:
    
    @classmethod
    def partition(cls, array: List[int | float]) -> int:
        pivot = array[0]
        low = -1
        high = len(array)
        
        while True:
            
            low += 1
            while array[low] < pivot:
                low += 1
                
            high -= 1
            while array[high] > pivot:
                high -= 1
                
            if low >= high:
                return high
            
            array[low], array[high] = array[high], array[low]
    

if __name__ == "__main__":
    pass