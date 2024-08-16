# LINKED LISTS 
- Storing objects in a linear manner
- Each object has data and a pointer to the next object
- Similar to arrays, except pointers determine the order of elements, not indices
- Commonly implemented in other data structures: stacks, queues, hash tables, etc
- Used in dynamic memory allocation

![Linked lists](../../../../assets/linked-list.png)

On a linked list, each object has both data and a next pointer. 2 versions of a linked list exists: singly linked list (where traversal is only possible in one direction, head to tail) and doubly linked list (where objects have a pointed to the next and previous node, traversal is possible in both directions). Lastly, circular lists also exist, where the previous pointer of the head object points to the tail and the next pointer of the tail object points to the head. 

## OPERATIONS
### INSERT
1. Move prev pointer before specified position
2. Create new object list, set new object to the value to be inserted
3. Assing new object list's next field to the pointer of the next object
4. Reassign prev pointer to the newly inserted object
5. Increase list size by 1

NOTE: Now the new object should be placed correctly in its specified position. 

Time complexity:
- Average Case: O(1)
- Worst Case: O(1)

### DELETE
1.
2.
3.

Time complexity:
- Average Case: O(1)
- Worst Case: O(1)

### SEARCH
1. 
2.
3.

Time complexity:
- Average Case: O(1)
- Worst Case: O(n)