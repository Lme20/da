# INSERTION SORT - Sorting through insertion
- Sorts elements by repeatedly taking the next element and inserting it into its correct position 
- Will form both sorted and unsorted partitions
- Comparisons are done from RIGHT to LEFT!
- Best used for a small number of records
- Insertion sort is a stable algorithm
- If binary search is used, the worst-case complexity likely remains at  O(N^2)


## Steps
1. Work left to right, starting in index 0

2. Begin with the first element in the unsorted partition (index 1)

3. Compare current element with sorted partition from *right* to *left*.

4. Insert the current element into its correct position in the sorted partition.

5. Continue to the next element to the right and repeat process.  

NOTE: Visually, the pointer moves sequentally as comparisons and swaps are performed (from left to right). 

![Insertion Sort](../assets/insertion-sort.png)

## Pseudocode

    for i : 1 to length(A) -1
        j = i
        while j > 0 and A[j-1] > A[j]
            swap A[j] and A[j-1]
            j = j - 1

## Asymptotic complexity: 
- Time complexity:

*Best case:*
Comparisons: O(n)
Swaps: O(n)

*Worst case:*
Comparisons: O(n^2)
Swaps: O(n^2)

- Space complexity: 
