import hashlib

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
        self.size = size
        if hashFunctions is None:
            self.k = 10
            self.hashFunctions = []
            """Adding the 10 default hash functions"""
            self.hashFunctions.append(self.hash1)
            self.hashFunctions.append(self.hash2)
            self.hashFunctions.append(self.hash3)
            self.hashFunctions.append(self.hash4)
            self.hashFunctions.append(self.hash5)
            self.hashFunctions.append(self.hash6)
            self.hashFunctions.append(self.hash7)
            self.hashFunctions.append(self.hash8)
            self.hashFunctions.append(self.hash9)
            self.hashFunctions.append(self.hash10)

        else:
            self.k = len(hashFunctions)
            self.hashFunctions = hashFunctions
    
    """
    Adding a value to the set in the bloom filter
    @param:  value to add 
    @return: none
    """        
    def add(self, value):
        """Insert value into the bloom filter."""
        for hashf in self.hashFunctions: 
            idx = hashf(value, self.size) 
            self.bits |= 1 << idx
    
    """
    Adding a parameterized function to the list of hash functions
    @param:  function to add to list of hash funcitons 
    @return: none
    """
    def addHashFunction(self, function): 
        if(callable(function)): 
            self.hashFunctions.append(funciton)

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
        return [hf(value, self.size) for hf in self.hashFunctions]
       
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
            idx = hashf(value,self.size) 
            mask |= 1 << idx
        
        if mask & self.bits == mask: 
            # might be present
            return True

        return False
    
    def hash1(self, value, size):
        """ generates the first 4 bytes of an md5 hash """ 
        hashobj = hashlib.md5(bytes(value, encoding='utf-8'))
        return int("0x" + (hashobj.hexdigest()[0:8]),0) % size
        
    def hash2(self, value, size): 
        """ generates the first 4 bytes of an sha256 hash """
        hashobj = hashlib.sha256(bytes(value, encoding='utf-8'))
        return int("0x" + (hashobj.hexdigest()[0:8]),0) % size
        
    def hash3(self, value, size): 
        """ generates the first 4 bytes of an sha384 hash """
        hashobj = hashlib.sha384(bytes(value, encoding='utf-8'))
        return int("0x" + (hashobj.hexdigest()[0:8]),0) % size

    def hash4(self, value, size):
        """ generates the first 4 bytes of an sha224 hash """
        hashobj = hashlib.sha224(bytes(value, encoding='utf-8'))
        return int("0x" + (hashobj.hexdigest()[0:8]),0) % size
        
    def hash5(self, value, size):
        """ generates the first 4 bytes of an sha1 hash """ 
        hashobj = hashlib.sha1(bytes(value, encoding='utf-8'))
        return int("0x" + (hashobj.hexdigest()[0:8]),0) % size
    
    def hash6(self, value, size):
        """ generates the first 4 bytes of an md5 hash """ 
        hashobj = hashlib.md5(bytes(value, encoding='utf-8'))
        return int("0x" + (hashobj.hexdigest()[8:16]),0) % size
        
    def hash7(self, value, size): 
        """ generates the first 4 bytes of an sha256 hash """
        hashobj = hashlib.sha256(bytes(value, encoding='utf-8'))
        return int("0x" + (hashobj.hexdigest()[8:16]),0) % size
        
    def hash8(self, value, size): 
        """ generates the first 4 bytes of an sha384 hash """
        hashobj = hashlib.sha384(bytes(value, encoding='utf-8'))
        return int("0x" + (hashobj.hexdigest()[8:16]),0) % size

    def hash9(self, value, size):
        """ generates the first 4 bytes of an sha224 hash """
        hashobj = hashlib.sha224(bytes(value, encoding='utf-8'))
        return int("0x" + (hashobj.hexdigest()[8:16]),0) % size
        
    def hash10(self, value, size):
        """ generates the first 4 bytes of an sha1 hash """ 
        hashobj = hashlib.sha1(bytes(value, encoding='utf-8'))
        return int("0x" + (hashobj.hexdigest()[8:16]),0) % size
    


