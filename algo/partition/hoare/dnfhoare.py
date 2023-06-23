from __future__ import annotations
from typing import List

class DNFHoarePartition:
    
    @classmethod
    def partition(cls, array: List[int | float]) -> int:
        pivot = array[0]
        low = -1
        high = len(array)
        
        point = 0
        
        while True:
            
            low += 1
            while array[low] < pivot:
                low += 1
                
            high -= 1
            while array[high] > pivot:
                high -= 1
                
            if low >= high:
                point = high
                break
            
            array[low], array[high] = array[high], array[low]
    
        left = point + 1
        right = point
        
        while left - 1 >= 0 and array[left - 1] == pivot:
            left -= 1
        
        for i in range(left):
            if array[i] == pivot:
                left -= 1
                array[i], array[left] = array[left], array[i]
            
            if i >= left - 1:
                break
            
        while right + 1 < len(array) and array[right + 1] == pivot:
            right += 1
            
        for i in range(len(array) - 1, right, -1):
            if array[i] == pivot:
                right += 1
                array[i], array[right] = array[right], array[i]
                
            if i <= right + 1:
                break
        
        return left, right
        

if __name__ == "__main__":
    pass