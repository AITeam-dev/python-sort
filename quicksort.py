"""
Simple sorting algorithm: Quick Sort
Divides the list around a pivot, recursively sorts sublists, then combines.
"""


def quicksort(arr: list) -> list:
    """Sort a list in ascending order using quick sort."""
    result = arr.copy()
    _quicksort_inplace(result, 0, len(result) - 1)
    return result


def _quicksort_inplace(arr: list, low: int, high: int) -> None:
    """Sort arr[low:high+1] in place using the last element as pivot."""
    if low < high:
        pivot_idx = _partition(arr, low, high)
        _quicksort_inplace(arr, low, pivot_idx - 1)
        _quicksort_inplace(arr, pivot_idx + 1, high)


def _partition(arr: list, low: int, high: int) -> int:
    """Partition around arr[high]; return final pivot index."""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    example = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {example}")
    sorted_result = quicksort(example)
    print(f"Original: {example}")
    print(f"Sorted:   {sorted_result}")
