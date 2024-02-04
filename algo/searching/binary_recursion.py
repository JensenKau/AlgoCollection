from __future__ import annotations
from typing import List

class RecursiveBinarySearch:
    @classmethod
    def binary_search_aux(cls, arr: List[int], elem: int, start: int, end: int) -> int:
        if start > end:
            return -1
        
        mid = (start + end) // 2
        
        if arr[mid] == elem:
            return mid
        elif elem < arr[mid]:
            return RecursiveBinarySearch.binary_search_aux(arr, elem, start, mid - 1)
        else:
            return RecursiveBinarySearch.binary_search_aux(arr, elem, mid + 1, end)
    
    @classmethod
    def binary_search(cls, arr: List[int], elem: int) -> int:
        return RecursiveBinarySearch.binary_search_aux(arr, elem, 0, len(arr) - 1)

if __name__ == "__main__":
    pass