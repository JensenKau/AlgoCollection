from __future__ import annotations
from typing import List
import random

class InsertionSort:
    
    @classmethod
    def sort(cls, array: List[int | float]) -> None:
        for i in range(1, len(array)):
            current = array[i]
            
            for j in range(i - 1, -1, -1):
                if array[j] > current:
                    array[j + 1] = array[j]
                else:
                    array[j + 1] = current
                    break
                
                if j == 0:
                    array[j] = current
        
                    
if __name__ == "__main__":
    pass