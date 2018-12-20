import hashlib
"""
    Demonstrate Bloom filter using native python.
    
    Uses raw ints as the basis for bloom.
"""

class bloomFilter:
    def __init__(self, size = 1000, hashFunctions=None):
        """
        Construct a bloom filter with size bits (default: 1000) and the associated hash functions.
        If no hash functions are provided, then a single function based on hash(e) % size is used.
        """
        self.bits = 0  
        self.size = size
        if hashFunctions is None:
            self.k = 1
            self.hashFunctions = [lambda e, size : hash(e) % size]
        else:
            self.k = len(hashFunctions)
            self.hashFunctions = hashFunctions
            
    def add(self, value):
        """Insert value into the bloom filter."""
        """
        Implement your function here.
        What you should do is for each hashFunctions in self.hashFunctions, 
        set the bit in self.bit that matches to hashFunctions(value, self.size) to 1.
        You can get some idea how self.bit should look like in countbits().
        IMPORTANT: You are expected to use bit operations
        """
        for hashf in self.hashFunctions: 
            idx = hashf(value, self.size) 
            self.bits |= 1 << idx
        
        
            
    def countbits(self):
        n = self.bits
        num = 0
        while n > 0:
            num += (n % 2)
            n = n >> 1
        return num
          
    """
    Creates a bit mask with the given integer array in those positions 
    """
    def mask(self, ints): 
        mask = 0
        for i in ints: 
            mask |= 1 << i
        return mask
          
    def fingerprint(self, value):
        """Return hash indices for the given value. Useful for debugging."""
        return [hf(value, self.size) for hf in self.hashFunctions]
         
    def __contains__(self, value):
        """
        Determine whether value is present. A false positive might be returned even if the 
        element is not present. However, a false negative will never be returned (i.e., if 
        the element is present, then it will return True).
        """
        """
        Implement your function here.
        What you should do is for each hashFunctions in self.hashFunctions, 
        check if all corresponding bits in self.bits are 1. 
        If all bits are 1 return True, if any bit is 0 return False.
        IMPORTANT: You are expected to use bit operations

        """
        mask = 0
        for hashf in self.hashFunctions:
            idx = hashf(value,self.size) 
            mask |= 1 << idx
        
        if mask & self.bits == mask: 
            # might be present
            return True

        return False
    
    
def hash1(value): 
    hashobj = hashlib.md5(bytes(value, encoding='utf-8'))
    return int("0x" + (hashobj.hexdigest()[0:4]),0)
    
def hash2(value): 
    hashobj = hashlib.sha256(bytes(value, encoding='utf-8'))
    return int("0x" + (hashobj.hexdigest()[0:4]),0)
    
def hash3(value): 
    hashobj = hashlib.sha384(bytes(value, encoding='utf-8'))
    return int("0x" + (hashobj.hexdigest()[0:4]),0)

def hash4(value): 
    hashobj = hashlib.sha224(bytes(value, encoding='utf-8'))
    return int("0x" + (hashobj.hexdigest()[0:4]),0)
    
def hash5(value): 
    hashobj = hashlib.sha1(bytes(value, encoding='utf-8'))
    return int("0x" + (hashobj.hexdigest()[0:4]),0)
    



hashFunctions = []

"""
Appending the five hash functions into a λ-function array for the constructor
"""
hashFunctions.append(lambda e,size : hash1(e) % size)
hashFunctions.append(lambda e,size : hash2(e) % size)
hashFunctions.append(lambda e,size : hash3(e) % size)
hashFunctions.append(lambda e,size : hash4(e) % size)
hashFunctions.append(lambda e,size : hash5(e) % size)

b = bloomFilter(1000, hashFunctions)    
b.add('hello')
print(b.__contains__('hello'))
print(b.__contains__('hell'))
print(b.__contains__('yup'))

