import unittest

from quicksort import quicksort
from sort import bubble_sort


class SortAlgorithmTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sample = [64, 34, 25, 12, 22, 11, 90]
        self.expected = sorted(self.sample)

    def test_bubble_sort_orders_values(self) -> None:
        self.assertEqual(bubble_sort(self.sample), self.expected)

    def test_quicksort_orders_values(self) -> None:
        self.assertEqual(quicksort(self.sample), self.expected)

    def test_sorts_empty_list(self) -> None:
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(quicksort([]), [])

    def test_preserves_input_list(self) -> None:
        original = [3, 1, 2]
        bubble_sort(original)
        quicksort(original)
        self.assertEqual(original, [3, 1, 2])

    def test_handles_duplicates(self) -> None:
        data = [3, 1, 3, 2, 1]
        expected = [1, 1, 2, 3, 3]
        self.assertEqual(bubble_sort(data), expected)
        self.assertEqual(quicksort(data), expected)


if __name__ == "__main__":
    unittest.main()
