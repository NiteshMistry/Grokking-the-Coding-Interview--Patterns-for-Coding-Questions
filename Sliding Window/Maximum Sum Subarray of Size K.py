# Maximum Sum Subarray of Size K (easy)

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9

import time

# Brute Force Approach
# Time Complexity: O(N * K)
def find_max_sum_subarray_bf(arr: list, k: int) -> list:
    _max_sum = 0
    for i in range(len(arr) - k + 1):
        _sum = 0   
        for j in range(i, i + k):
            _sum += arr[j]
        if _sum > _max_sum:
            _max_sum = _sum
    return _max_sum

# Sliding Window Approach
# Time Complexity: O(N)
def find_max_sum_subarray_sw(arr: list, k: int) -> list:
    _max_sum = 0
    _sum = 0
    for i in range(len(arr) - k + 1):
        if i == 0:
            _sum = sum(arr[i:i+k])
        else:
            _sum = _sum - arr[i-1] + arr[i+k-1]
        if _sum > _max_sum:
            _max_sum = _sum
    return _max_sum            
            
if __name__ == '__main__':
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    
    # Brute Force Approach
    start = time.time()
    print(find_max_sum_subarray_bf(arr, k))
    print(f'Brute Force Approach took {time.time() - start} seconds')
    
    # Sliding Window Approach
    start = time.time()
    print(find_max_sum_subarray_sw(arr, k))
    print(f'Sliding Window Approach took {time.time() - start} seconds')
    


