# Max K Elements

This function calculates the maximum possible score by performing the following operations:

1. Insert all elements of the input vector `nums` into a max-heap.
2. For `k` iterations, do the following:
   - Extract the maximum element from the heap and add it to the score.
   - Calculate a new value by dividing the extracted element by 3, rounding up to the nearest integer.
   - Insert the new value back into the heap.

## Arguments

- `nums`: A vector of integers from which the maximum score is to be calculated.
- `k`: The number of iterations to perform the extraction and insertion operations.

## Returns

- An `i64` representing the maximum possible score after `k` iterations.

## Explanation

The function uses a max-heap to always extract the largest element in each iteration. After extracting the largest element, it adds this element to the score and then calculates a new value by dividing the element by 3 and rounding up. This new value is then pushed back into the heap to be considered in subsequent iterations. This process is repeated `k` times to maximize the score.

## Code

```rust

use std::collections::BinaryHeap;

pub fn max_kelements(nums: Vec<i32>, k: i32) -> i64 {
    let mut heap = BinaryHeap::new();

    for &num in &nums {
        heap.push(num);
    }

    let mut score: i64 = 0;
    for _ in 0..k {
        if let Some(max_element) = heap.pop() {
            score += max_element as i64;

            let new_value = (max_element as f64 / 3.0).ceil() as i32;

            heap.push(new_value);
        }
    }

    score
}

fn main() {
        assert_eq!(max_kelements(vec![10, 10, 10, 10, 10], 5), 50);
        assert_eq!(max_kelements(vec![1,10,3,3,3], 3), 17);
        assert_eq!(max_kelements(vec![9, 8, 7, 6, 5], 3), 24);   
        println!("All Passed!")
}
```
