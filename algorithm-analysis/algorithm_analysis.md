# Algorithm analysis

## Problems, Algorithms and Programs


### Problems
* A problem maps inputs to outputs.
* A problem is a mapping from inputs to outputs, and there might be many algorithms that can accomplish this mapping.


### Programs
* A program is an instantiation of an algorithm implemented in a specific programming language.


### Algorithms
* An algorithm is a series of steps that act as a recipe to solve a particular problem.

#### Comparing algorithms

To estimate an algorithm's performance:
* count the number of basic operations


## Complexity

![Best, Worst, and Average Cases](/assets/complexity-comparison.png)

### Worst-Case

### Average-case

### Best-case

## Order of Growth - Growth Rate

### Big-O Notation

## Asymptotic Complexity

### Algorithmic behaviours and time complexity

#### 1. Constant Time: O(1)
* **Behavior**: The execution time does not depend on the size of the input data. The operations are fixed and do not change as the input size changes.
* **Examples**: Accessing an array element by index, checking if a stack is empty, or assigning a value to a variable.

#### 2. Logarithmic Time: O(log n)
* **Behavior**: The execution time increases logarithmically as the input size increases. This usually occurs in algorithms that divide the problem in half each step or work on reducing the problem size exponentially.
* **Examples**: Binary search in a sorted array, finding an element in a balanced binary search tree.

#### 3. Linear Time: O(n)
* **Behavior**: The execution time increases linearly with the increase in input size. These algorithms typically perform a single operation on each element of the input.
* **Examples**: Summing all elements in an array, checking for the existence of an element in an unsorted list.

#### 4. Linearithmic Time: O(n log n)
* **Behavior**: The execution combines linear and logarithmic behaviors. These are often efficient sorting algorithms that recursively divide and conquer the input.
* **Examples**: Merge sort, quicksort (on average).

#### 5. Quadratic Time: O(n²)
* **Behavior**: The execution time grows as the square of the input size. These algorithms usually involve nested iterations over the data set.
* **Examples**: Bubble sort, insertion sort, checking all pairs in an array (like finding duplicates).

#### 6. Cubic Time: O(n³)
* **Behavior**: The execution time is proportional to the cube of the input size. This is typical in algorithms involving three nested loops.
* **Examples**: Naive algorithms for matrix multiplication, solving three-body problems in physics.

#### 7. Exponential Time: O(2^n)
* **Behavior**: The execution time doubles with each addition to the input size. These algorithms often deal with all possible combinations of inputs.
* **Examples**: Brute-force solutions for the traveling salesman problem, generating all subsets of a set.

#### 8. Factorial Time: O(n!)
* **Behavior**: The execution time grows factorial with the input size. These are algorithms that generate all possible permutations of the input.
* **Examples**: Solving the traveling salesman problem by trying every permutation of visits.

