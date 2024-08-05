# INSERTION SORT

- Will form both sorted and unsorted partitions


## Steps
1. Work left to right, starting in index 0

2. Begin with the first element in the unsorted partition (index 1)

3. Compare current element with sorted partition from left to right.

4. *Swap* element if:
    - current element is smaller than compared element in sorted partition (swap compared element right)
    - continue process until the correct position for the current element is reached

5. Continue to the next element in the unsorted partition. 


## Pseudocode

    for i : 1 to length(A) -1
        j = i
        while j > 0 and A[j-1] > A[j]
            swap A[j] and A[j-1]
            j = j - 1

## Asymptotic complexity: 

- Time complexity:

Comparisons: O(n^2)
Swaps: O(n^2)

- Space complexity: 
