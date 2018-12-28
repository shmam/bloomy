import hashlib
import math


class bloomFilter:
    
    """
    Constructs a new bloom filter with the specified (or default) parameters. 
    
    Default values are set for a 1,000,000 bit array 122.07KiB with k = 10 hash functions, set to 
    hold up 50,000 items with a reasonable odds against false positives(1 in 11243)
    
    Calculated with https://hur.st/bloomfilter/
    where 
    n = ceil(m / (-k / log(1 - exp(log(p) / k))))
    p = pow(1 - exp(-k / (m / n)), k)
    m = ceil((n * log(p)) / log(1 / pow(2, log(2))));
    k = round((m / n) * log(2));
    
    @param:  size and list of hash functions
    @return: constructed bloom filter object
    """
    def __init__(self, size = 1000000, hashFunctions=None):
        self.bits = 0  
        self.m = size
        self.n = 0
        if hashFunctions is None:
            
            self.hashFunctions = []
            """Adding the 10 default hash functions"""
            for i in range(0,10): 
                self.hashFunctions.append(self.kHash(i))
            self.k = len(self.hashFunctions)

        else:
            self.hashFunctions = hashFunctions
            self.k = len(self.hashFunctions)

    
    """
    Adding a value to the set in the bloom filter
    @param:  value to add 
    @return: none
    """        
    def add(self, value):
        """Insert value into the bloom filter."""
        for hashf in self.hashFunctions: 
            idx = hashf(value) 
            self.bits |= 1 << idx
        self.n += 1
    
    """
    Adding a parameterized function to the list of hash functions
    @param:  function to add to list of hash funcitons 
    @return: none
    """
    def addHashFunction(self, function): 
        if(callable(function)): 
            self.hashFunctions.append(function)
            self.k = len(self.hashFunctions)

    """
    Creates a bit mask with the given integer array in those positions  
    @param:  array of ints representing indexes in the bit array to 1
    @return: bit mask 
    """
    def mask(self, ints):
        mask = 0
        for i in ints: 
            mask |= 1 << i
        return mask
          
    """
    Return hash indices for the given value
    @param:  value to hash and generate unique fingerprint
    @return: list of hash values generated for the given value
    """
    def fingerprint(self, value):
        return [hf(value) for hf in self.hashFunctions]
       
    """
    Determine whether value is present. A false positive might be returned even if the 
    element is not present. However, a false negative will never be returned (i.e., if 
    the element is present, then it will return True).
    @param:  value to check presence in Set
    @return: True/False responce to presence in set
    """  
    def __contains__(self, value):

        mask = 0
        for hashf in self.hashFunctions:
            idx = hashf(value) 
            mask |= 1 << idx
        
        if mask & self.bits == mask: 
            # might be present
            return True

        return False
        
    """
    Implementation of the golden ratio compression method 
    Hash value depends on all characters and their positions, therfore permutations not likely to collide
    If key space is strings of a certain length, the method distributes keys uniformly across hash table
    """
    def gr_compression(self, hash): 
        phi = (1.0 + math.sqrt(5)) / 2
        inv_phi = 1.0 / phi
        return math.floor(self.m * (hash*inv_phi - math.floor(hash*inv_phi)))            
    
    """
    Determine the optimal number of hash functions necessary given m and n 
    """
    def calculate_k(self, m = None, n = None):
        if m == None: m = self.m
        if n == None: n = self.n
        
        try: 
            return round(m / n  * math.log(2))
        except ZeroDivisionError: 
            return 0
    
    
    """
    Calculating the probability of false positives given m, n and k
    """
    def calculate_p(self, k = None, m = None, n = None):
        if k == None: k = self.k 
        if m == None: m = self.m
        if n == None: n = self.n 
        
        try: 
            return pow(1 - math.exp( -k / (m / n)), k)
        except ZeroDivisionError: 
            return 0
        
    def kHash(self,n): 
        return lambda value: (self.gr_compression(int(hashlib.md5(bytes(value, 'ascii') + bytes(n)).hexdigest()[0:8],16)))
        
