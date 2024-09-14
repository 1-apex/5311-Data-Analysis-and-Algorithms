### Detailed breakdown of how each recursive step works for `fib(5)`:

First, `fib(5)` calls both ``fib(4)`` and `fib(3)`.

Then, `fib(4)` calls both `fib(3)` and `fib(2)`:

When `fib(3)` is called, it recursively calls `fib(2)` and `fib(1)`.

`fib(2)` further calls `fib(1)` and `fib(0)`, which return `1` and `0` respectively.

Therefore, `fib(2)` returns `1`, and `fib(3)` returns `2` after summing up `fib(2)` and `fib(1)`.

Moving back to `fib(4)`, the value `2` from `fib(3)` is added to the value returned by `fib(2)` (which is `1`), resulting in `fib(4)` returning `3`.

Finally, back in `fib(5)`, the results from `fib(4)` and `fib(3)` are summed (i.e., `3 + 2`), yielding the final output of `5`.