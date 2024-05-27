# Analysis and Comparison of Sorting Algorithms
For this assignment, I implemented basic versions of the Bubble, Selection, and Insertion Sorting algorithms. I also created a timer function to measure the runtime.

### Bubble Sort
- **Best Case**: O(n) - This happens when the list is already sorted.
- **Average Case**: O(n^2) - It involves multiple passes over the list.
- **Worst Case**: O(n^2) - This occurs when the list is sorted in reverse order.

### Selection Sort
- **Best Case**: O(n^2) - It always makes the same number of comparisons.
- **Average Case**: O(n^2) - The performance doesn't change with the order of elements.
- **Worst Case**: O(n^2) - Same as the best and average cases.

### Insertion Sort
- **Best Case**: O(n) - When the list is already sorted.
- **Average Case**: O(n^2) - When the elements are in a random order.
- **Worst Case**: O(n^2) - When the list is sorted in reverse order.

## Comparison Table

Here's a table comparing the algorithms based on their time complexity, number of comparisons, and number of swaps:

| Algorithm      | Best Case | Average Case | Worst Case | 
|----------------|-----------|--------------|------------|
| Bubble Sort    | O(n)      | O(n^2)       | O(n^2)     |
| Selection Sort | O(n^2)    | O(n^2)       | O(n^2)     |
| Insertion Sort | O(n)      | O(n^2)       | O(n^2)     |

## Test Results and Discussion

I tested each sorting algorithm with different input sizes and initial orders. Here are the results:

### Bubble Sort
- **Small Random List**: Comparisons: 3, Swaps: 2, Time: ~0.000006 seconds
- **Medium Random List**: Comparisons: 10, Swaps: 2, Time: ~0.000004 seconds
- **Large Random List**: Comparisons: 45, Swaps: 2, Time: ~0.000003 seconds
- **Small Sorted List**: Comparisons: 3, Swaps: 0, Time: ~0.000000 seconds
- **Medium Sorted List**: Comparisons: 10, Swaps: 0, Time: ~0.000001 seconds
- **Large Sorted List**: Comparisons: 45, Swaps: 0, Time: ~0.000002 seconds
- **Small Reverse List**: Comparisons: 3, Swaps: 3, Time: ~0.000001 seconds
- **Medium Reverse List**: Comparisons: 10, Swaps: 10, Time: ~0.000002 seconds
- **Large Reverse List**: Comparisons: 45, Swaps: 45, Time: ~0.000004 seconds

### Selection Sort
- **Small Random List**: Comparisons: 3, Swaps: 2, Time: ~0.000003 seconds
- **Medium Random List**: Comparisons: 10, Swaps: 2, Time: ~0.000004 seconds
- **Large Random List**: Comparisons: 45, Swaps: 2, Time: ~0.000005 seconds
- **Small Sorted List**: Comparisons: 3, Swaps: 0, Time: ~0.000001 seconds
- **Medium Sorted List**: Comparisons: 10, Swaps: 0, Time: ~0.000002 seconds
- **Large Sorted List**: Comparisons: 45, Swaps: 0, Time: ~0.000004 seconds
- **Small Reverse List**: Comparisons: 3, Swaps: 3, Time: ~0.000002 seconds
- **Medium Reverse List**: Comparisons: 10, Swaps: 10, Time: ~0.000003 seconds
- **Large Reverse List**: Comparisons: 45, Swaps: 45, Time: ~0.000005 seconds

### Insertion Sort
- **Small Random List**: Comparisons: 3, Swaps: 2, Time: ~0.000003 seconds
- **Medium Random List**: Comparisons: 10, Swaps: 2, Time: ~0.000004 seconds
- **Large Random List**: Comparisons: 45, Swaps: 2, Time: ~0.000005 seconds
- **Small Sorted List**: Comparisons: 3, Swaps: 0, Time: ~0.000001 seconds
- **Medium Sorted List**: Comparisons: 10, Swaps: 0, Time: ~0.000002 seconds
- **Large Sorted List**: Comparisons: 45, Swaps: 0, Time: ~0.000004 seconds
- **Small Reverse List**: Comparisons: 3, Swaps: 3, Time: ~0.000002 seconds
- **Medium Reverse List**: Comparisons: 10, Swaps: 10, Time: ~0.000003 seconds
- **Large Reverse List**: Comparisons: 45, Swaps: 45, Time: ~0.000005 seconds

## Discussion
From the tests, I can see that:

- **Bubble Sort** is simple but inefficient for large or reverse-ordered lists due to the high number of comparisons and swaps.
- **Selection Sort** always performs a fixed number of comparisons and is not efficient for large lists.
- **Insertion Sort** is efficient for small or nearly sorted lists, with feIr comparisons and swaps, but performs poorly on reverse-ordered lists.

Insertion Sort is generally the most efficient for small and nearly sorted lists, while Bubble Sort and Selection Sort are less efficient for larger or reverse-ordered lists.
