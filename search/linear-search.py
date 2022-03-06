# Worst-case: O(n), Best-case: O(1)

def linear_search(arr: list, target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
print(linear_search(arr, target))