# Average of all contiguous subarrays of size K (easy)

# Input: Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]

import time

# Brute Force Approach
# Time Complexity: O(N * K)
def find_avg_subarray_bf(arr: list, k: int) -> list:
    result = []
    for i in range(len(arr) - k + 1):
        _sum = 0   
        for j in range(i, i + k):
            _sum += arr[j]
        result.append(_sum/k)
    return result

# Sliding Window Approach
# Time Complexity: O(N)
def find_avg_subarray_sw(arr: list, k: int) -> list:
    result = []
    _sum = 0
    for i in range(len(arr) - k + 1):
        if i == 0:
            _sum = sum(arr[i:i+k])
        else:
            _sum = _sum - arr[i-1] + arr[i+k-1]
        result.append(_sum/k)
    return result            
            
if __name__ == '__main__':
    arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    k=5
    
    # Brute Force Approach
    start = time.time()
    print(find_avg_subarray_bf(arr, k))
    print(f'Brute Force Approach took {time.time() - start} seconds')
    
    # Sliding Window Approach
    start = time.time()
    print(find_avg_subarray_sw(arr, k))
    print(f'Sliding Window Approach took {time.time() - start} seconds')
    


