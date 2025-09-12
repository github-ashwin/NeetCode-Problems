def maxAdjacentProduct(arr):
    if len(arr) < 2:
        return None  # not enough elements
    max_prod = float('-inf')
    for i in range(len(arr) - 1):
        max_prod = max(max_prod, arr[i] * arr[i + 1])
    return max_prod

# Example
print(maxAdjacentProduct([3, 6, -2, -5, 7, 3]))  # 21 (7*3)
