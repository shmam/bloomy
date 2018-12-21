
### Bloom Filter
\\bloom **fil**-ter\\
_**Noun**_
1. Space-efficient probabilistic data structure that is used to test whether an element is a member of a set. 
2. A fun side project!

### :cherry_blossom: :bouquet: :tulip: :hibiscus: :blossom: :maple_leaf: :evergreen_tree: :sunflower: :cactus: :fallen_leaf: :deciduous_tree:

### Advantages of bloom filters 
- Uses bit arrays to store the presence of items. This signifigantly reduces the in memory storage. :floppy_disk: 
- Implements binary and bit masking operations. This reduces the runtime of add and contains operations to practically O(1). :zap:
- Raw types can be used. The only imports so far are hashlib functions for md5, sha265, sha384, sha224 ans sha1. :+1:
- Lambda functions used (for fun!) 

### Operations :nut_and_bolt:	

#### `___init__(m,[array of additional hash functions])`
Create a bit array `bits` with m bits cleared to 0, and saves k number of hash functions. M has a default of 1000 and the filter comes with five unique default hash functions. 

#### `add(value)`
Takes in a value and hashes it k times to obtain a list of indexes. For each index obtained by a given hash function, set the value in the bit array `bits` to 1. 

Pseudocode: 
```
add (value)
    foreach hashFunction hf
        setbit = 1 << hf (value)
        bits |= setbit
end
```


#### `contains(value)` 
Takes in a value and hashes it k times to obtain a list of unique indexes. Create a bit mask with the initial value 0. For each index obtained by a hash funciton in, set that index in the mask 1. Preform the followinng binary operation `bits AND mask`, and if the value preformed by that operation equals the mask, we can conclude that the value _**probably**_ exists in the bloom filter. 

Pseudocode: 
```
search (value)
    foreach hashfunction hf
        checkbit = 1 << hf(value)
        if checkbit & bits = 0 then
            return false
            
    return true
```


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
