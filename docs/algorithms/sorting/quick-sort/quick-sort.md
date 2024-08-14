# QUICKSORT - sorting in ascending or descending order

*quick sort is recursive*

- fastest known general-purpose in-memory sorting algorithm in the average case
- Much more space efficient compared to merge sort
- Widely used algorithm 
- lomuto partition scheme is being used for this specific implementation

## Steps
1) Select pivot (either in left, right or midpoint)
2) Move pivot to start of array
3) Select left and right pointers
4) Partition subarray
    - Swap when: 
        a. `left` points to element greater than or equal to pivot (<=)
        b. `right` points to element less than or equal to pivot (>=)
    - Repeat until pointers cross

Conditions:
1. Correct position in final sorted array
2. items to the left are smaller
3. items to the right are larger

Stop sorting when: 
index of `left` > index of `right`

- itemFromLeft = is greater than pivot
- itemFromRight = is smaller than pivot

### Find the pivot
Find the pivot by calculating rightmost and leftmost positions and dividing by 2:
- (left + right) / 2 = pivot index

### Partition
1. Move the Pivot:
    -  Move the pivot to the rightmost position if not already there.

2. Set Left and Right Bounds:
    - `left` = start of array
    `right` = end - 1 (assuming end is the index of the pivot)

3. Move Pointers:
    - Move `left` pointer to `right` until element is greater or equal to pivot
    - Move `right` pointer to `left` until element is less than or equal to pivot

4. Swap Elements:
    - Swap pointers = left pointer is less or equal to right pointer

5. Repeat Steps:
    - Terminate process when left/right pointer crosses right/left pointer, then, move pivot to *crossing position*

crossing position: where the left and right pointers have crossed

NOTE: Once the process is done, repeat parition on its subarrays (from left to right). Make sure to select a new pivot and use the old pivot as separator between left and right sublist

## Pseudocode

    Quicksort(A as array, low as int, high as int)
        If (low < high)
            pivot_location = Partition(A, low, high)
            Quicksort(A, low, pivot_location - 1)
            Quicksort(A, pivot_location + 1, high)
    
    Partition(A as array, low as int, high as int)
        pivot = A[low]
        leftwall = low
    
        for i = low + 1 to high
            if (A[i] < pivot) then
                leftwall = leftwall + 1
                swap(A[i], A[leftwall])
        
        swap(A[low], A[leftwall])
        return leftwall

## Time Complexity
The total cost of the partition operation is constrained by how far right and left can move inwards.

paritioning: O(n)

Best Case: (O(n \log n))
    - Occurs when the pivot chosen always divides the array into 2 nearly equal halves, depth of recursion tree is O(log n) at each level, partitioning takes O(n)

worst-case: O(n^2)
average-case: O(n log n)

## Space Complexity