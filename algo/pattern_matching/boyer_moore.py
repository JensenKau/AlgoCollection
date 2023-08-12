from __future__ import annotations

class BoyerMoore:
    def __init__(self, pattern: str) -> None:
        self.pattern = pattern
        self.bc_map = None
        self.bc_table = None
        self.zarr = None
        
        self.construct_bc_table(pattern)
        self.reverse_zalgo()
        

    def construct_bc_table(self, pattern: str) -> None:
        counter = 0
        self.bc_map = dict()
        
        for char in pattern:
            if char not in self.bc_map:
                self.bc_map[char] = counter
                counter += 1
                
        self.bc_table = [None] * len(self.bc_map)

        for i in range(len(self.bc_table)):
            self.bc_table[i] = [-1] * len(pattern)
            
        for i in range(len(pattern) - 1, - 1, -1):
            self.bc_table[self.bc_map[pattern[i]]][i] = i
        
        for i in range(len(self.bc_table)):
            for j in range(1, len(self.bc_table[i])):
                self.bc_table[i][j] = max(self.bc_table[i][j], self.bc_table[i][j-1])

    
    def reverse_zalgo(self) -> None:
        self.zarr = [0] * len(self.pattern)
        self.zarr[len(self.zarr) - 1] = len(self.zarr)
        
        left = len(self.zarr) - 1
        right = len(self.zarr) - 1
        
        index = len(self.zarr) - 2
        
        while index >= 0:
            if index >= left and index <= right:
                if self.zarr[len(self.zarr) - 1 - (right - index)] < index - left + 1:
                    self.zarr[index] = self.zarr[len(self.zarr) - 1 - (right - index)]
                    
                elif self.zarr[len(self.zarr) - 1 - (right - index)] > index - left + 1:
                    self.zarr[index] = index - left + 1
                    
                else:
                    start = len(self.zarr) - 1 - self.zarr[len(self.zarr) - 1 - (right - index)]
                    current = left - 1
                    same_counter = self.zarr[len(self.zarr) - 1 - (right - index)]
                    
                    while current >= 0 and self.pattern[current] == self.pattern[start]:
                        start -= 1
                        current -= 1
                        same_counter += 1
                        
                    self.zarr[index] = same_counter
                    
                    if same_counter > 0:
                        right = index
                        left = index - same_counter + 1
            
            else:
                start = len(self.zarr) - 1
                current = index
                same_counter = 0
                
                while current >= 0 and self.pattern[current] == self.pattern[start]:
                    start -= 1
                    current -= 1
                    same_counter += 1
                    
                self.zarr[index] = same_counter
                
                if same_counter > 0:
                    right = index
                    left = index - same_counter + 1
                                
            index -= 1

    def match_pattern(self, setence: str):
        pass


if __name__ == "__main__":
    pass