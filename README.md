
## Bloom Filter
\\bloom **fil**-ter\\
_**Noun**_
1. Space-efficient probabilistic data structure that is used to test whether an element is a member of a set. 
2. A fun side project!

[![Build Status](https://travis-ci.com/shmam/bloom-filter.svg?branch=master)](https://travis-ci.com/shmam/bloom-filter)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Coverage Status](https://coveralls.io/repos/github/shmam/bloom-filter/badge.svg?branch=master)](https://coveralls.io/github/shmam/bloom-filter?branch=master)

### :cherry_blossom: :bouquet: :tulip: :hibiscus: :blossom: :maple_leaf: :evergreen_tree: :sunflower: :cactus: :fallen_leaf: :deciduous_tree:

### Advantages of bloom filters 
- Uses bit arrays to store the presence of items. This significantly reduces the in memory storage. :floppy_disk: 
- Implements binary and bit masking operations. This reduces the runtime of add and contains operations to practically O(1). :zap:
- Raw types can be used. The only imports so far are hashlib functions for md5, sha265, sha384, sha224 and sha1. :+1:
- Lambda functions used (for fun!) 

---
### Operations :nut_and_bolt:	

#### `___init__(m,[array of additional hash functions])`
       params: (optional) size of bit array, (optional) additional hash functions 
       return: bloomFilter object 
Create a bit array `bits` with m bits cleared to 0, and saves k number of hash functions. M has a default of 1000 and the filter comes with five unique default hash functions. 

#### `add(value)`
       params: object to add to the bloomFilter set
       return: None
Takes in a value and hashes it k times to obtain a list of indexes. For each index obtained by a given hash function, set the value in the bit array `bits` to 1. 


Pseudocode: 
```
add (value)
    foreach hashFunction hf
        setbit = 1 << hf (value)
        bits |= setbit
end
```


#### `__contains__(value)` 
       params: object to search for in the set 
       return: True/False indicating presence in the set
Takes in a value and hashes it k times to obtain a list of unique indexes. Create a bit mask with the initial value 0. For each index obtained by a hash function, set that index in the mask 1. Perform the following binary operation `bits AND mask`, and if the value performed by that operation equals the mask, we can conclude that the value _**probably**_ exists in the bloom filter. 

Pseudocode: 
```
search (value)
    foreach hashfunction hf
        checkbit = 1 << hf(value)
        if checkbit & bits = 0 then
            return false
            
    return true
```


#### `addHashFunction(fn)`
       params: additional hash function to add
       return: None
Takes in a function as a parameter, and adds this function to the existing list of hash functions used by the bloom filter. The function `fn` has to take the form `fn(value, size, ...)` where `value` is the item to hash, `size` is the upper index bound in the bit array, and the function must return an integer between 0 and the upper index bound. All other following parameters must have default values. 

The function also has to be able to provide consistent values for the given input. There is no randomization involved, rather this is a pure key transformation function. Any compression function may be used, as long as it limits the key space within the upper bound of the bit array. 

#### `fingerprint(value)`
       params: value to inspect fingerprint
       return: array (len = k) of hashed values 
Takes in a value and returns an array of the hashed values created by the list of hash functions. Used to debug and inspect the behavior of the hashing mechanism. 

#### `mask([ints])`
       params: integer values to use to create bit mask
       return: integer bit mask
Creates a bit masked integer with 1 in the indexes specified by the parameter integer array. 

---
### Example (k = 3, m = 12)
```
0. constructor 

bit array: 
  --- --- --- --- --- --- --- --- --- --- --- --- --- 
 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ...
  --- --- --- --- --- --- --- --- --- --- --- --- --- 

1. add("Hello world") => 00, 03, 04

bit array: 
  --- --- --- --- --- --- --- --- --- --- --- --- --- 
 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ...
  --- --- --- --- --- --- --- --- --- --- --- --- --- 

2. contains("Hello World") => 00,03,04 

bit array: 
  --- --- --- --- --- --- --- --- --- --- --- --- --- 
 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ...
  --- --- --- --- --- --- --- --- --- --- --- --- --- 
   ||          ||  ||
   ||==========||==||=================> 1,1,1 = True 

3. contains("java is the best") => 02,03,07 

bit array: 
  --- --- --- --- --- --- --- --- --- --- --- --- --- 
 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ...
  --- --- --- --- --- --- --- --- --- --- --- --- --- 
           ||  ||              ||
           ||==||==============||=====> 0,1,0 = False
```

### Thank you!! 🤩
Thank you for checking this out! Please feel free to reach out via email [sdcroche@ncsu.edu](mailto:sdcroche@ncsu.edu), or twitter [@shmam_](https://twitter.com/shmam_)
