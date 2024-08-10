# MERGE SORT - Sort by divide and conquer
- Merge sort is done recursively
- Uses a divide and conquer aproach
- 


## Steps

**SPLITTING**

**MERGING**


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

*Best case:*


*Worst case:*
O (n log n)

- Space complexity: 
