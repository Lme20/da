# SEPARATE CHAING (open hashing) - HASH TABLES

Used to deal with collisions in hash tables. 
Usually includes linked lists as an "auxiliary" data structure. Other data structures can be used instead.

Structure: 
- Each slot in the hash table can be the head of a linked list
- Records within a slot can be ordered in several ways: insertion order, key value order, frequency-of-access order

Load factor: λ = n / m
- where 'n'is the number of keys stored
- 'm' is total number of slots
- a higher factor means the table is more full

Hash colision: 2 keys hash to the same value

## Operations

### DELETION

time complexity:
- Average Case: O(1 + λ)
- Worst Case: O(n)

### INSERTION

1) pass element's key to hash function
2) modulus operation: n / index and then taking the reminder
*EXAMPLE*
    a. 334 / 10 = 33,4 
    b. 334 - 10 x 33 = 4 (always remove decimal values)

3) if a value is already placed on the index, add new element to the linked list at that index

time complexity:
- Average Case: O(1)
- Worst Case: O(1)

### LOOKUPS

time complexity:
- Average Case: O(1 + λ)
- Worst Case: O(n)






## Costs




## 

