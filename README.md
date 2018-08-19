# algorithms
Various algorithms implemented for practice

## Sorting Algorithms
### Bubblesort
bubblesort.py

Swaps inverted pairs until none are found
O(n^2)

### Insertion sort
insertionsort.py

Constructs a new array by picking values from the original array and inserting them into the correct place in the new array.
O(n^2) (due to shifting in the new array)

### Heapsort
heapsort.py

Adds all elements in the array into a minimum heap, then pops all items out of the heap.

O(n log n)

### Mergesort
mergesort.py

Splits array in half, calls itself for each half separately, merges the results.

O(n log n)

### Quicksort
quicksort.py

Selects a random pivot element, divides the remaining elements into partitions where all elements are either larger or 
smaller than the pivot. Each partition is recursively sorted in isolation.

O(n log n) average

### Selectionsort
selectionsort

Find the smallest item in the array, then add that to the new array.

O(n^2)

## Graph Algorithms
### Kruskal's minimum spanning tree algorithm
graph.py

Computes the minimum spanning tree by iteratively finding the edge with the smallest weight that connects to disconnected components.

## Complexity Estimator

classifier.py contains utilities for determining the big O class of an algorithm, based on experimental data

benchmark.py contains a suite of benchmarking tools to test various sorting algorithms
