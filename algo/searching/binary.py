from __future__ import annotations
from typing import List

class BinarySearch:
    @classmethod
    def binary_search(cls, arr: List[int], elem: int) -> int:
        start = 0
        end = len(arr) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if arr[mid] == elem:
                return mid
            elif elem < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
                
        return -1

if __name__ == "__main__":
    pass