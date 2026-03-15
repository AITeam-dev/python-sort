"""
Simple sorting algorithm: Selection Sort
Repeatedly selects the smallest unsorted element and swaps it to the front.
"""


def selection_sort(arr: list) -> list:
    """Sort a list in ascending order using selection sort."""
    result = arr.copy()
    n = len(result)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    return result


if __name__ == "__main__":
    example = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {example}")
    sorted_result = selection_sort(example)
    print(f"Original: {example}")
    print(f"Sorted:   {sorted_result}")
