# Consider a simple algorithm to solve the problem of finding the largest value in an array of n integers. 
# The algorithm looks at each integer in turn, saving the position of the largest value seen so far. 
# This algorithm is called the largest-value sequential search and is illustrated by the following function:

# Return position of largest value in integer array A
def largest(A): 
    currlarge = 0 # Position of largest element seen
    for i in range(1, A.length): # For each element
        if A[currlarge] < A[i]: # if A[i] is larger
            currlarge = i # remember its position
    return currlarge # Return largest position