# HASH TABLES - Map keys to values
- Hash tables are a specific way of mapping keys to values, essentially the implementation of a dictionary with a hash function
- The hash function maps keys to a location in the table that holds data
- Sometimes used interchangebly with dictionary
- Represents a *dynamic* set of data

**GOOD VS BAD HASH FUNCTION:**
- Good hash function:
    - Uniformly ditributes keys across the hash table to minimize collisions
    - simple and fast to compute
    - Example: multiplicative hash function, where the hash code is dervided from a prime number

- Bad hash function
    - Clusters keys into few indices, leading to many collisions
    - Complex and slow to compute
    - Example: modulo operation with non-prime number as divisor

**LOAD FACTOR:**
ratio of the number of elements in a hash table (n) to the number of available slots (m).
- Load Factor = n/m.
- High load factor: increased likelyhood of collision
- Low load factor: low chances of collision
- Used to determine if a table needs to be resized


**RESIZING A TABLE**
- A table should be resized when its load factor exceeds a predefined threshold of 0.7 

## OPERATIONS
- Operations on hash tables requires techniques which handle collisions, separate chaining and linear probing are the most common techniques used for this case.

### SEARCH
- For search to be close to O(1), you need:
    - a hash function with maximized randomness + least amount of collisions
    - Examples: division, multiplication, universal hashing, dynamic perfect hashing, static perfect hashing

#### Hashing by division
- H(k) = k mod m (where 'k' is the key and 'm' is the size of the table)
- The modulo operation returns the remainder of the division of k by m.

Example:
If you have a key k = 123 and the size of the hash table m = 12:

H(123) = 123 mod 12 = 3

Steps to calculate mod:
1. *Divide* key by table size: 123 ÷ 12 = 10.25
2. Take the integer part of the result: 10
3. *Multiply* the integer part by the table size: 10 × 12 = 120
4. *Subtract* the result from the key: 123 - 120 = 3

So, the key 123 would be stored at index 3 in the hash table.

Note: This example only shows how to compute the index.

### HANDLING COLLISIONS
- When 2 different keys hash to the same index in a hash table array. (both keys are assinged to the same slot)

#### SEPARATE CHAINING
![Separate chaining](../../../../assets/separate-chaining.png)

- Each slot in the hash table array holds a linked list (or another structure) of entries that hash to the same index.
- Use the modulo operation to get the computed index.
- Introduce linked lists to handle collision

**INSERT:**
Add the key-value pair to the linked list at the computed index.

**DELETE:**
Traverse the linked list at the computed index to find and remove the key-value pair.

**LOOKUP:**
Traverse the linked list at the computed index to find the key and return its associated value.

**COMPLEXITIES**
- Average case: O(1) for insert, delete, and lookup.
- Worst case: O(n) for insert, delete, and lookup (if all keys hash to the same index).

#### LINEAR PROBING (open addressing)
![Lineat probing](../../../../assets/linear-probing.png)

- Handles collisions by placing the collided key in the next available slot in the array.

**INSERT:**
If the desired index is occupied, probe sequentially to find the next empty slot.

**LAZY DELETION:**
Mark an element as deleted rather than removing it immediately, and skip it during probing.

**LOOKUP:**
If the key isn’t at the computed index, check the next slot until the key is found or an empty slot is reached.

**COMPLEXITIES**
- Insert: O(1) average, O(n) worst case.
- Lookup: O(1) average, O(n) worst case.
- Lazy Deletion: Like insert and lookup.