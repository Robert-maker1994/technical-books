# [_Majority Element_](https://leetcode.com/problems/majority-element/description/?envType=problem-list-v2&envId=hash-table)

## Description

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

## How I solved this problem

I wanted to take a different approach to fix this problem as quickly as possible.

I thought of a basic algorithm which followed:
**Initialize** 
    - Majority Number = length / 2; 
    - create a Map<number, number>() - result

**Iterate** 
    - Iterate over the nums array 
    - Add each number to the array 
    - if its repeated increment the value

**Iterate over the Map** 
    - See if the value is higher than the majority number
    - if the value is the highest value add it to the result

```typescript
function majorityElement(nums: number[]) {
  const m = nums.length / 2;

  const map = new Map<number, number>();

  for (const n of nums) {
    if (!map.has(n)) {
      map.set(n, 0);
    }
    map.set(n, map.get(n)! + 1);
  }

  for (const [key, val] of map.entries()) {
    if (val > m) {
      if (val > result) {
        return key;
      }
    }
  }
}
```

I cracked the code, however, not in an optimized way this took a mer 14 miliseconds to render. However, lets see what I've learned when I wanted to optimism the function. I started looking around I thought I could probably fit everything into one for loop an not have two, because lets be honest two loops is a little overkill. 

This is where I found the most optimized algorithm is (Moore majority vote algorithm)[https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm]  which I have never heard of. 

Initialize:

Set a candidate element (candidate) to None.
Set a counter (count) to 0.
Iterate through the array:

For each element in the array:
    - If count is 0, set the candidate to the current element and set count to 1.
    - If the current element is the same as candidate, increment count.
    - If the current element is different from candidate, decrement count.
    - At the end of this phase, the candidate will be the majority element if there is one.

Phase 2: Verifying the Candidate
Initialize:

- Set a counter (count) to 0.
Iterate through the array:

For each element in the array:
- If the element is the same as candidate, increment count.
- Check if the candidate is the majority element:

If count is greater than n/2, the candidate is the majority element.
- Otherwise, there is no majority element.

```typescript
function majorityElement(nums: number[]): number {
    let candidate;
    let count = 0;
    
    for (const num of nums) {
        if (count === 0) {
            candidate = num;
        }
        
        count += (num === candidate) ? 1 : -1
    }
    
    return candidate;
};
```

This is the code to solve this problem which blows my mind a little and took me a while to get my head around how to was functioning. 