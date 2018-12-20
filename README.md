# bloom-filter
### :cherry_blossom: :bouquet: :tulip: :hibiscus: :blossom: :maple_leaf: :evergreen_tree: :sunflower: :cactus: :fallen_leaf: :deciduous_tree:


This repository is just a side project and having fun with new tools. 

### Advantages of bloom filters 
- Uses bit arrays to store the presence of items. This signifigantly reduces the in memory storage. :floppy_disk: 
- Implements binary and bit masking operations. This reduces the runtime of add and contains operations to practically O(1). :zap:
- Raw types can be used. The only imports so far are hashlib functions for MD5, sha265, sha384, sha224 ans sha1. :+1:
- Lambda functions used (for fun!) 

### Operations :nut_and_bolt:	

#### `boomFilter(value)`

#### `add(value)`
Takes in a value and hashes it multiple times to obtain a list of indexes. 

#### `contains(value)` 


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
