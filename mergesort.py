"""
Simple sorting algorithm: Merge Sort
Divides the list in half, recursively sorts each half, then merges the sorted halves.
"""


def mergesort(arr: list) -> list:
    """Sort a list in ascending order using merge sort."""
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    """Merge two sorted lists into one sorted list."""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    example = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {example}")
    sorted_result = mergesort(example)
    print(f"Original: {example}")
    print(f"Sorted:   {sorted_result}")
