# SELECTION SORT - Sorting by selecting

- Selection sort first finds the largest key in an unsorted list and then the next largest an so on. 
- Few record swaps
- Swaps required is n−1
- Selection sort is essentially a bubble sort except the next largest value is remembered to delay the swap to the end of each pass
- Selection sort is a good choice to use on an array when the swap cost is large (long strings)


Overall complexity of Θ(n^2) for worst, best and average case.
Number of swaps amounts to Θ(n) time. 

## Steps

1. Start with the first element of the array.
2. Search the unsorted portion of the array to find the smallest element.
3. Swap the smallest element found with the first unsorted element.
4. Move the boundary between the sorted and unsorted portions one element to the right and repeat steps 2 & 3 until entire array is sorted.

**EXAMPLE:**
![selection sort](../../../../assets/selection-sort.gif)

## Pseudocode

    for (j = 0; j < n-1; j++)
        int iMin = j;

        for (i = j+1; i<n; i++)
            if (a[i] < a[iMin])
                iMin = i; 
        if (iMin != j)
            swap(a[j], a[iMin]);

## Asymptotic complexity: 
- Time complexity:

*Best case:*
Comparisons: Θ(n^2)
Swaps: Θ(n)

*Worst case:*
Comparisons: Θ(n^2)
Swaps: Θ(n)

- Space complexity: 
