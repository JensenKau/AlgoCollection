from __future__ import annotations
from typing import List

class MergeSort:
    
    @classmethod
    def sort(cls, array: List[int | float]) -> None:
        if len(array) > 1:
            first_half = [0] * (len(array) // 2)
            second_half = [0] * (len(array) - len(first_half))
            
            for i in range(len(array)):
                if i < len(first_half):
                    first_half[i] = array[i]
                else:
                    second_half[i - len(first_half)] = array[i]
                    
            MergeSort.sort(first_half)
            MergeSort.sort(second_half)
            
            pointer1 = 0
            pointer2 = 0
            array_pointer = 0
            
            while pointer1 < len(first_half) and pointer2 < len(second_half):
                if first_half[pointer1] <= second_half[pointer2]:
                    array[array_pointer] = first_half[pointer1]
                    pointer1 += 1
                else:
                    array[array_pointer] = second_half[pointer2]
                    pointer2 += 1
                
                array_pointer += 1
                
            if pointer1 < len(first_half):
                for i in range(pointer1, len(first_half)):
                    array[array_pointer] = first_half[i]
                    array_pointer += 1
            else:
                for i in range(pointer2, len(second_half)):
                    array[array_pointer] = second_half[i]
                    array_pointer += 1
        
    
if __name__ == "__main__":
    pass