from __future__ import annotations
from typing import Any
import random

class LinearProbe:
    MIN_CAPACITY = 11
    MILLER_TEST = 30
    
    def __init__(self, initial_capacity: int = MIN_CAPACITY) -> None:
        nearest_prime = self.__nearest_prime(max(initial_capacity, LinearProbe.MIN_CAPACITY))
        
        self.keys = [None] * nearest_prime
        self.values = [None] * nearest_prime
        self.size = 0
    
    
    def __hash(self, key: str) -> int:
        value = 11
        
        for char in key:
            value = (value * 31 + ord(char)) % len(self.keys)
            
        return value
    
    
    def __primality_test(self, num: int) -> bool:
        if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
            d = num - 1
            while d % 2 == 0:
                d //= 2
            
            for _ in range(LinearProbe.MILLER_TEST):
                if not self.__miller_test(d, num):
                    return False
                
            return True
        
        return False
    
    
    def __miller_test(self, d: int, n: int) -> bool:
        a = random.randint(7, n - 2)
        
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            return True
        
        while d != n - 1:
            x = pow(x, 2, n)
            d *= 2
            
            if x == 1:
                return False
            if x == n - 1:
                return True
            
        return False
    
    
    def __nearest_prime(self, num: int) -> int:
        while not self.__primality_test(num):
            num += 1
            
        return num
    
    
    def __resize(self) -> None:
        nearest_prime = self.__nearest_prime(len(self.keys) * 2)
        old_keys = self.keys
        old_values = self.values
        
        self.keys = [None] * nearest_prime
        self.values = [None] * nearest_prime
        
        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                pos = self.__hash(old_keys[i])
                
                while self.keys[pos] is not None:
                    pos = (pos + 1) % len(self.keys)
                    
                self.keys[pos] = old_keys[i]
                self.values[pos] = old_values[i]
    
    
    def __len__(self) -> int:
        return self.size
    
    
    def __contains__(self, key: str) -> bool:
        pos = self.__hash(key)
        
        count = 0
        while count < len(self.keys) and self.keys[pos] is not None:
            if self.keys[pos] == key:
                return True
            
            pos = (pos + 1) % len(self.keys)
            count += 1
        
        return False
    
    
    def __getitem__(self, key: str) -> Any:
        pos = self.__hash(key)
        
        while self.keys[pos] is not None:
            if self.keys[pos] == key:
                return self.values[pos]
            
            pos = (pos + 1) % len(self.keys)
        
        raise ValueError("Key does not exist")
    
    
    def __setitem__(self, key: str, value: Any) -> None:
        pos = self.__hash(key)
        
        while True:
            if self.keys[pos] is not None:
                if self.keys[pos] == key:
                    self.values[pos] = value
                    break
            else:
                self.keys[pos] = key
                self.values[pos] = value
                self.size += 1
                break
            
            pos = (pos + 1) % len(self.keys)
        
        if self.size / len(self.keys) >= 0.5:
            self.__resize()
     
    
    def insert(self, key: str, value: Any) -> None:
        pos = self.__hash(key)
        
        while True:
            if self.keys[pos] is not None:
                if self.keys[pos] == key:
                    raise ValueError("Key already exist")
            else:
                self.keys[pos] = key
                self.values[pos] = value
                self.size += 1
                break
            
            pos = (pos + 1) % len(self.keys)
            
        if self.size / len(self.keys) >= 0.5:
            self.__resize()
            
    
    def remove(self, key: str) -> None:
        pos = self.__hash(key)
        temp = []
        is_found = False
        
        while self.keys[pos] is not None:
            if not is_found:
                if self.keys[pos] == key:
                    self.keys[pos] = None
                    self.values[pos] = None
                    self.size -= 1
                    is_found = True
            else:
                temp.append((self.keys[pos], self.values[pos]))
                self.keys[pos] = None
                self.values[pos] = None
            
            pos = (pos + 1) % len(self.keys)
            
            
        for key, value in temp:
            pos = self.__hash(key)
            
            while self.keys[pos] is not None:
                pos = (pos + 1) % len(self.keys)
                
            self.keys[pos] = key
            self.values[pos] = value
    
    
    def __str__(self) -> str:
        temp = [None] * self.size
        
        pointer = 0
        for i in range(len(self.keys)):
            if self.keys[i] is not None:
                temp[pointer] = f"{self.keys[i]}: {self.values[i]}"
                pointer += 1
                
        return f"{{{', '.join(temp)}}}"
    
    
if __name__ == "__main__":
    pass