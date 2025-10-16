**Approaching The Problem**

The key insight for this problem is realizing that the 2D matrix is effectively a flattened 1D sorted array in disguise. Each row continues from where the previous one left off, meaning the entire structure maintains global sorted order.

Because of that, we can treat the matrix as if it were a single linear array and apply a binary search over the full range of elements. The main challenge is mapping between the 1D index and the 2D coordinates — this can be done using division and modulus operations:

row = mid // n

col = mid % n

*Note: Only the number of columns n is needed to map a 1D index to a 2D coordinate, since the matrix elements increase left-to-right across rows and then wrap to the next row.* 

At each step, we compare the middle element with the target and halve the search space accordingly — shifting low or high to narrow the window. This reduction by half on each iteration is what gives binary search its logarithmic O(log(m·n)) complexity.

In summary, the key reasoning steps were:
- Recognize the matrix’s sorted property allows linear indexing.
- Apply binary search logic over the conceptual 1D array.
- Convert between 1D and 2D indices dynamically.
- Use the standard exit condition while low <= high and return True if the target is found.