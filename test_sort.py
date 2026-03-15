"""Tests for sort.bubble_sort."""

import unittest
from sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    def test_sorts_unsorted_list(self):
        """Sorts a list of integers in ascending order."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        self.assertEqual(bubble_sort(arr), [11, 12, 22, 25, 34, 64, 90])

    def test_empty_list(self):
        """Returns empty list unchanged."""
        self.assertEqual(bubble_sort([]), [])

    def test_single_element(self):
        """Single-element list is unchanged."""
        self.assertEqual(bubble_sort([42]), [42])

    def test_already_sorted(self):
        """Already sorted list is unchanged."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        """Reverse-sorted list becomes ascending."""
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(bubble_sort(arr), [1, 2, 3, 4, 5])

    def test_does_not_mutate_original(self):
        """Original list is not modified."""
        arr = [3, 1, 2]
        bubble_sort(arr)
        self.assertEqual(arr, [3, 1, 2])


if __name__ == "__main__":
    unittest.main()
