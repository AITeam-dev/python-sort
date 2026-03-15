# Bubble Sort

A simple Python implementation of the bubble sort algorithm.

## About

Bubble sort compares adjacent elements and swaps them if they're in the wrong order. The algorithm iterates through the list until no more swaps are needed, at which point the list is sorted.

## Usage

Run the script directly:

```bash
python sort.py
```

Output:

```
Original: [64, 34, 25, 12, 22, 11, 90]
Sorted:   [11, 12, 22, 25, 34, 64, 90]
```

Or import and use the `bubble_sort` function:

```python
from sort import bubble_sort

sorted_list = bubble_sort([3, 1, 4, 1, 5, 9, 2, 6])
```
