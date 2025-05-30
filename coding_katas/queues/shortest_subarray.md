# [Shortest Subarry with sum at least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/)

## Description 
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

## Solution
1. Prefix Sum Calculation:
- nums.iter().scan(0, |a, &n| {*a += n as i64; Some(*a)}) creates an iterator that computes the prefix sums of nums.
- once(0).chain(sum_iter).collect::<Vec<_>>() prepends a 0 to the prefix sums and collects them into a vector pfx_sums.

2. Initialization:
- indices is a deque to store indices of the prefix sums.
- sub_len is initialized to the maximum possible value of usize to keep track of the shortest subarray length.
- k is cast to i64 for consistency with the prefix sum

3. Main loop 
- The loop iterates over the prefix sums.
- The first while loop removes indices from the front of the deque if the subarray sum is at least k, updating sub_len with the minimum length found.
- The second while loop removes indices from the back of the deque if the current prefix sum is less than or equal to the prefix sum at the back.
- The current index i is pushed to the back of the deque.

4. Result 
- If sub_len is still usize::MAX, it means no valid subarray was found, so return -1.
- Otherwise, return the length of the shortest subarray as an i32.

```
pub fn shortest_subarray(nums: Vec<i32>, k: i32) -> i32 {
  let sum_iter = nums.iter().scan(0, |a, &n| {*a += n as i64; Some(*a)});
        let sum_iter = nums.iter().scan(0, |a, &n| {*a += n as i64; Some(*a)});
        let pfx_sums = once(0).chain(sum_iter).collect::<Vec<_>>();
        let mut indices = VecDeque::new();
        let mut sub_len = usize::MAX;
        let k = k as i64;

        for (i, &sum) in pfx_sums.iter().enumerate() {

            while indices.front().map_or(false, |&j| sum - pfx_sums[j] >= k) {
                sub_len = sub_len.min(i - indices.pop_front().unwrap());
            }
            while indices.back().map_or(false, |&j| pfx_sums[j] >= sum) {
                indices.pop_back();
            }
            indices.push_back(i);
        }

        if sub_len == usize::MAX { 
            -1 
        } else { 
            sub_len as i32
        }
}
```