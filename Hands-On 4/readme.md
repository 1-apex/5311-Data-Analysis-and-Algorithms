### Name : Prathamesh Patil
### Student ID: `1002233913`

## Breakdown of how each recursive step works for `fib(5)`:

- First, `fib(5)` calls both ``fib(4)`` and `fib(3)`.

- Then, `fib(4)` calls both `fib(3)` and `fib(2)`.

- Then, `fib(3)` calls both `fib(2)` and `fib(1)`.

- `fib(2)` further calls `fib(1)` and `fib(0)`, which return `1` and `0` respectively.

- Therefore, `fib(2)` returns `1`, and `fib(3)` returns `2` after summing up `fib(2)` and `fib(1)`.

- Moving back to `fib(4)`, the value `2` from `fib(3)` is added to the value returned by `fib(2)` (which is `1`), resulting in `fib(4)` returning `3`.

- Finally, back in `fib(5)`, the results from `fib(4)` and `fib(3)` are summed (i.e., `3 + 2`), yielding the final output of `5`.

### (a more proper explanation of function call stack working is done down in the `fibonacci.py` file)

## Time complexity of Fibonacci code 

The time complexity of the recursive Fibonacci code is `O(2^n)`, which is exponential.

#### Reasons:
##### Recursive Calls:
    - For each call to fib(n), the function makes two recursive calls: fib(n-1) and fib(n-2). This branching happens at every level, resulting in a large number of repeated calculations.

##### Overlapping Subproblems:
    - Many Fibonacci numbers are recalculated multiple times. For example, fib(2) and fib(1) are computed multiple times across the recursion tree. This duplication of work grows rapidly as n increases.

For each Fibonacci number `n`, the function makes about `2^n` recursive calls due to the repeated recalculations, leading to the exponential time complexity `O(2^n)`.


## Ways we can improve the implementation of Fibonacci 

### 1. Memoization:
        - We can create a memory to store the calculated results of the values so that we avoid recalculating them, and that could reduce the time complexity by `O(n)` considering `O(1)` time to fetch the values of precomputed ones from the map.

### 2. Dynamic Programming
        - We can simply use arrays and store the results and iterate upto n. Even this approach could achieve `O(n)` time complexity. 






