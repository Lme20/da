# GLOSSARY

## Address
A location in memory.

## Adjacency List
An implementation for a graph that uses an (array-based) list to represent the vertices of the graph, and each vertex is in turn represented by a (linked) list of the vertices that are neighbors.

## Adjacency Matrix
An implementation for a graph that uses a 2-dimensional array where each row and each column corresponds to a vertex in the graph. A given row and column in the matrix corresponds to an edge from the vertex corresponding to the row to the vertex corresponding to the column.

## Adjacent
Two nodes of a tree or two vertices of a graph are said to be adjacent if they have an edge connecting them. If the edge is directed from a to b, then we say that a is adjacent to b, and b is adjacent from a.

## ADT
Abbreviation for abstract data type.

## Adversary
A fictional construct introduced for use in an adversary argument.

## Aggregate Type
A data type whose members have subparts. For example, a typical database record. Another term for this is composite type.

## Amortized Complexity
A modification to the notion of complexity for operations on a data structure where, for each fixed input size, one does not just look at the cost of a single run of the operation, but its amortized cost over sufficiently long series of operations of the same kind. This can be made precise without considering averages by introducing potentials.

## Amortized Cost
The average cost of an operation in a sufficiently long series of operations of the same kind. This is as opposed to considering every individual operation to independently have its own cost, which might lead to an overestimate for the total cost of the series. This can be made precise without considering averages by introducing potentials. In amortized analysis, gives rise to the notion of amortized complexity.

## Asymptotic Complexity
The growth rate or order of growth of the complexity of an algorithm or problem. There are several independent categories of qualifiers for (asymptotic) complexity:

- time complexity (default)
- space complexity
- complexity in some other cost
- worst case (default)
- average case
- best case

### Term
Whether to use amortized complexity.

## Average Case
In algorithm analysis, specifically complexity of an algorithm, the average of the costs for all problem instances of a given input size n. If not all problem instances have equal probability of occurring, then the average case must be calculated using a weighted average that is specified with the problem (for example, every input may be equally likely). Every input size n has its own average case. We never consider the average case as removed from input size.

## Basic operation
A basic operation must have the property that its time to complete does not depend on the particular values of its operands. Adding or comparing two integer variables are examples of basic operations in most programming languages.

## Call Stack
Known also as execution stack. A stack that stores the function call sequence and the return address for each function.

## Size
Size is often the number of inputs processed. For example, when comparing sorting algorithms the size of the problem is typically measured by the number of records to be sorted.

## Height
The number of nodes on the longest path from the root to the leaf.