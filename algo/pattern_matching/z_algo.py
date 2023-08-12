from __future__ import annotations
import random
from boyer_moore import BoyerMoore

def z_algo(sentence: str):
    zarr = [0] * len(sentence)
    
    zarr[0] = len(zarr)
    
    left = 0
    right = 0
    
    index = 1
    
    while index < len(zarr):        
        if index >= left and index <= right:
            if zarr[index - left] < right - index + 1:
                zarr[index] = zarr[index - left]
            elif zarr[index - left] > right - index + 1:
                zarr[index] = right - index + 1
            else:
                start = zarr[index - left]
                current = right + 1
                same_counter = zarr[index - left]
                
                while current < len(zarr) and sentence[current] == sentence[start]:
                    same_counter += 1
                    start += 1
                    current += 1
                    
                zarr[index] = same_counter
                
                if same_counter > 0:
                    left = index
                    right = index + same_counter - 1
                                                    
        else:
            start = 0
            current = index
            same_counter = 0
            
            while current < len(zarr) and sentence[current] == sentence[start]:
                same_counter += 1
                start += 1
                current += 1
                
            zarr[index] = same_counter
            
            if same_counter > 0:
                left = index
                right = index + same_counter - 1              
                
        index += 1
        
    return zarr
    
    

if __name__ == "__main__":
    # print(str(z_algo("aabaabxcaabxaabxay", "aabaabxcaabxaabxay")))
    
    for i in range(10000):
        input_value = ''.join(random.choices(["a", "b", "c"], k=10000))
        # input_value = "baaaccacaa"
        # input_value = "cbaabaabaa"[::-1]
        
        verify = [0] * len(input_value)
        verify[0] = len(verify)
        
        obj = BoyerMoore(input_value)
        
        # for i in range(1, len(verify)):
        #     start = 0
        #     current = i
        #     same_counter = 0
            
        #     while current < len(verify) and input_value[start] == input_value[current]:
        #         start += 1
        #         current += 1
        #         same_counter += 1
                
        #     verify[i] = same_counter
              
        if obj.zarr[::-1] != z_algo(input_value[::-1]):
            print(input_value[::-1])
            print(obj.zarr[::-1])
            print(z_algo(input_value[::-1]))
            raise ValueError("dkfjkslj")
        
        # break
        