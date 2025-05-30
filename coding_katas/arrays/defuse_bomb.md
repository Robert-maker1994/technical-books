# [Defuse the bomb](https://leetcode.com/problems/defuse-the-bomb/description/?envType=daily-question&envId=2024-11-18)

Topics - *Sliding windows* - *Arrays*

You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If `k > 0`, replace the ith number with the sum of the next k numbers.
If `k < 0`, replace the ith number with the sum of the previous k numbers.
If `k == 0`, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

## Solution 
I knew that with this solution had to map over the code array twice. Once to iterate over the code array and another to create a sum for the ith number. I have done this two ways as a map or with a for range function in Rust. Both are the same ways outcomes. 

### Algorithm.
Concepts that I used for this is functional programming, iterators and mapping.  

1. Declare a pointer to the code length. 
2. Handle `k == 0`  with the length and return an zero array. 
3. Create an inclusive range loop. 
 - Check if k is a positive or a negative 
 - Map the corresponding elements in the code with k as the range and then use the iterator sum.
 - If k > 0: Iterate over the range 1..=k and compute the sum of elements in the array, wrapping around with modulo n.
 - If k < 0: Iterate over the range 1..=-k in reverse and compute the sum using the circular indexing formula.
4. Return the resulting array created from the map operation.


```
    pub fn decrypt(code: Vec<i32>, k: i32) -> Vec<i32> {
    let n = code.len();
        if k == 0 {
            return vec![0; n];
        }

        (0..n).map(|i| {
            if k > 0 {
                // When k is positive, sum the next k elements, wrapping around using modulo
                (1..=k).map(|j| code[(i + j as usize) % n]).sum()
            } else {
                // When k is negative, sum the previous |k| elements in reverse order
                (1..=(-k)).map(|j| code[(i + n - j as usize) % n]).sum()
            }
        }).collect()
    }

```


### Aspects learn in this Coding Kata

First time concepts - Modulo,  Circular Indexing learn more [*Circular Queue*](../../data-structures-and-algorithms/queues/circular_queue.md)

