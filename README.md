# Algorithme

## Big-O

- Drop the constant: O(2n) -> O(n), O(3n + 2) -> O(n)
- Drop the non-determinant term: O(n^2 + n) -> O(n^2), O(n + logn) -> O(n), O(5 * 2^n + 1000 * n^10) -> O(2^n)
- 3 scenarios: worst case, best case, average case
- Example:
```python
for i in range(10):
    print(i)

for j in range(100):
    print(j)
```
```python
for i in range(10):
    for j in range(20):
        print(i * j)
```