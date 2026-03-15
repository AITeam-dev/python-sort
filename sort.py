"""
Simple sorting algorithm: Bubble Sort
Compares adjacent elements and swaps them if they're in the wrong order.
"""


def bubble_sort(arr: list) -> list:
    """Sort a list in ascending order using bubble sort."""
    n = len(arr)
    # Make a copy so we don't mutate the original
    result = arr.copy()

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break  # Already sorted

    return result


if __name__ == "__main__":
    example = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {example}")
    sorted_result = bubble_sort(example)
    print(f"Sorted:   {sorted_result}")
