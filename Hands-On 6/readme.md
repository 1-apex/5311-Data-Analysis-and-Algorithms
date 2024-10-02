### Name : Prathamesh Patil
### Student ID: `1002233913`


# Average Runtime Complexity of Non-Random Pivot Quicksort

The average runtime complexity of the non-random pivot version of quicksort is **O(n log n)**. This means that, on average, the time taken to sort an array of size `n` is proportional to `n log n`.

## Explanation

In Quicksort, we select a pivot element and partition the array into three groups:
- Elements less than the pivot.
- Elements equal to the pivot.
- Elements greater than the pivot.

The recurrence relation for Quicksort can be written as:

\`\`\`
T(n) = n + 2T(n/2)
\`\`\`

Where:
- \( T(n) \) is the time complexity for sorting an array of size `n`.
- `n` is the time taken to partition the array (linear time).
- \( 2T(n/2) \) accounts for the time taken to sort the two partitions, assuming the pivot divides the array into two equal-sized parts.

### Solving the Recurrence Relation

Using the **Master Theorem** for divide and conquer algorithms, we can solve the recurrence:

\`\`\`
T(n) = n + 2T(n/2)
\`\`\`

This falls into the standard case where the complexity is \( O(n \log n) \). Thus, the average runtime complexity of Quicksort is **O(n log n)**, which is efficient and well-balanced for different types of inputs.

## Summary
- Best case: \( O(n \log n) \)
- Worst case: \( O(n^2) \)
- Average case: \( O(n \log n) \)

This makes Quicksort a highly efficient sorting algorithm in practice.
