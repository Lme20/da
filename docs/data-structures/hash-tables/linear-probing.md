# LINEAR PROBING - Probing method for resolving collisions on hash tables

- To solve collisions in a table (when 2 keys have the same index value)
- Mainly for open addressing hash tables

## STEPS

1. **Compute Index:**
    Use the hash function to compute the index for the given key.
2. **Inspect Slot:**
    - If the slot is empty, insert the key-value pair.
    - If the slot is occupied by the same key, update the value.
    - If the slot is occupied by a different key (collision), continue to step 3.
2. **Check Next Slot:**
    Check the next slot in the array.
    - If it's empty or has the same key, insert/update the key.
    - If the end of the array is reached, wrap around to the beginning.
    - If no empty slot is found after checking all slots, the table is full, and insertion fails.


## OPERATIONS

*Handle wrap around*
If the end of the array is reached, continue from the beginning. 


## PSEUDOCODE
