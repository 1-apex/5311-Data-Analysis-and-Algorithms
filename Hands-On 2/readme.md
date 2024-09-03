# Selection Sort Algorithm: Correctness Proof
 
## Overview

Selection sort is a simple, comparison-based sorting algorithm. It works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the array and swapping it with the first element of the unsorted portion. This process continues until the entire array is sorted.

This document provides a detailed argument for the correctness of the selection sort algorithm using the concept of loop invariants and induction.

## Correctness Argument

### Loop Invariant

A **loop invariant** is a property that holds true before and after each iteration of a loop. For the selection sort algorithm, the key loop invariant is:

> **At the start of each iteration of the outer loop (for a given `i`), the subarray `arr[0:i]` contains the smallest `i` elements of the array, sorted in ascending order.**

### Base Case

- Before the first iteration of the outer loop (when `i = 0`), the subarray `arr[0:i]` is empty. An empty subarray is trivially sorted, so the loop invariant holds.

### Inductive Step

- **Inductive Hypothesis**: Assume that the loop invariant holds true for the first `i` iterations. This means that `arr[0:i]` contains the smallest `i` elements of the array, sorted in ascending order.

- **Iteration `i`**: During the `i`-th iteration, the algorithm scans the remaining unsorted portion of the array (`arr[i:n]`) to find the smallest element and swaps it with `arr[i]`. After this swap:
  1. `arr[i]` now contains the smallest element in `arr[i:n]`.
  2. The subarray `arr[0:i+1]` now contains the smallest `i+1` elements of the array, sorted in ascending order.

- Therefore, the loop invariant is maintained after the `i`-th iteration.

### Termination

- The outer loop runs until `i = n-1`. At this point, the subarray `arr[0:n-1]` is sorted, and the last remaining element is already in its correct position. Thus, the entire array `arr[0:n]` is sorted.

### Conclusion

By the principle of induction, since the loop invariant is true before the first iteration and is maintained across all iterations, the selection sort algorithm correctly sorts the array.
The selection sort algorithm is correct and will always produce a sorted array for any valid input array. This correctness is established through the preservation of the loop invariant, the proper termination of the algorithm, and the accurate implementation of the minimum element identification and swap operations.

