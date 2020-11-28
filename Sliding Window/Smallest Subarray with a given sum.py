# Smallest Subarray with a given sum (easy)

# Problem Statement: 
# Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

# Example 1:
# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

# Example 2:
# Input: [2, 1, 5, 2, 8], S=7 
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

# Example 3:
# Input: [3, 4, 1, 1, 6], S=8 
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].

import math

# Sliding Window Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def smallest_subarray_given_sum_sw(arr: list, s: int) -> int:
    min_len = math.inf
    window_start = 0
    window_sum = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        # Shrink the window until the window_sum < s
        while window_sum >= s:
            min_len = min(min_len, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    
    if min_len == math.inf:
        return 0
    return min_len

if __name__ == '__main__':
    print(smallest_subarray_given_sum_sw([2, 1, 5, 2, 3, 2], 7))
    print(smallest_subarray_given_sum_sw([2, 1, 5, 2, 8], 7))
    print(smallest_subarray_given_sum_sw([3, 4, 1, 1, 6], 8))


