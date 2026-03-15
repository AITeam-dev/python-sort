import unittest

from insertionsort import insertion_sort
from quicksort import quicksort
from selectionsort import selection_sort
from sort import bubble_sort


class SortingAlgorithmsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.unsorted_values = [64, 34, 25, 12, 22, 11, 90, 22]
        self.sorted_values = sorted(self.unsorted_values)

    def _assert_algorithm(self, sort_fn) -> None:
        original = self.unsorted_values.copy()
        result = sort_fn(original)

        self.assertEqual(result, self.sorted_values)
        self.assertEqual(
            original,
            self.unsorted_values,
            "Sorting function should not mutate the input list.",
        )

    def test_bubble_sort(self) -> None:
        self._assert_algorithm(bubble_sort)

    def test_quicksort(self) -> None:
        self._assert_algorithm(quicksort)

    def test_insertion_sort(self) -> None:
        self._assert_algorithm(insertion_sort)

    def test_selection_sort(self) -> None:
        self._assert_algorithm(selection_sort)


if __name__ == "__main__":
    unittest.main()
