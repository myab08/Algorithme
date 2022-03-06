# Worst-case: O(log(n)), Best-case: O(1)

def binary_search(array: list, target: int) -> int:
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 3
print(binary_search(arr, 3))