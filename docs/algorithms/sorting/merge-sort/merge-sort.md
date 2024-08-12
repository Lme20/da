# MERGE SORT - Sort by divide and conquer
- Merge sort is done recursively
- Uses a divide and conquer aproach
- Stable sort, meaning that elements retain their relative order

## Steps

**SPLITTING**

1. If the array mas more than 1 elememnt, split into 2 halves
2. Continue splitting into 2 halves until reaching subarrays of single elements

Example: 
- Start with an array: [38, 27, 43, 3, 9, 82, 10]
- Split into two halves: [38, 27, 43] and [3, 9, 82, 10]
- Continue splitting: [38, 27], [43], [3, 9], [82, 10]
- Keep splitting until each subarray has one element: [38], [27], [43], [3], [9], [82], [10]

**MERGING**
1. Merge individual elements first, combine them into sorted arrays
2. Compare smallest elements of each subarray (from one branch to another) and build a new sorted array by taking the smallest element of each (from left to right). 
3. Continue merging until reaching a single sorted array

Example:
- Start merging: [38] and [27] into [27, 38], [3] and [9] into [3, 9], [82] and [10] into [10, 82]
- Merge further: [27, 38] with [43] into [27, 38, 43], [3, 9] with [10, 82] into [3, 9, 10, 82]
- Final merge: [27, 38, 43] with [3, 9, 10, 82] into [3, 9, 10, 27, 38, 43, 82]

NOTE: 

![Merge Sort](../../../../assets/insertion-sort.png)



## Pseudocode

Recursive function - where the array is halved:

    mergesort(array a)
        if (n == 1)
            return a

        arrayOne = a[0]...a[n/2]
        arrayTwo = a[n/2+1]...a[n]

        arrayOne = mergesort(arrayOne)
        arrayTwo = mergesort(arrayTwo)

        return merge (arrayOne, arrayTwo)

Merge function - where the array is combined:

    merge (array a, array b)
        array c

        while (a and b have elements)
            if(a[0] > b[0])
                add b[0] to the end of c
                remove b[0] from b
            else
                add a[0] to the end of c
                remove a[0] from a
        
        //At this point either b or a is empty
        while (a has elements)
            add a[0] to the end of c
            remove a[0] from a
        
        while (b has elements)
            add b[0] to the end of c
            remove b[0] from b

        return c


## Asymptotic complexity: 

- time complexity:
*Best case:*
O (n log n)

*Worst case:*
O (n log n)

- Space complexity: 
O(n)