"""
Simple sorting algorithm: Insertion Sort
Builds the sorted list one element at a time by inserting each element into its correct position.
"""


def insertion_sort(arr: list) -> list:
    """Sort a list in ascending order using insertion sort."""
    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


if __name__ == "__main__":
    example = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {example}")
    sorted_result = insertion_sort(example)
    print(f"Original: {example}")
    print(f"Sorted:   {sorted_result}")
