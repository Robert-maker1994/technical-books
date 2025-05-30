[*Longest Common Prefix*](https://leetcode.com/problems/longest-common-prefix/solutions/3493266/alphabetise-and-compare-98-speed/)


# Solution 
My solution here was pretty simple: iterate over the `strs` array and reduce the `prefix` until it matches the start of `str[i]`. To compare the substring, I used the `substring` method. While iterating over the `prefix`, we will find the correct prefix.

```typescript
function longestCommonPrefix(strs: string[]): string {
        if (strs.length === 0) return ""; 
    let prefix =  strs[0]; 
    
    for (let i = 1; i < strs.length; i++) {
        while (strs[i].indexOf(prefix) !== 0) {
            prefix = prefix.substring(0, prefix.length - 1);
            if (prefix === "") return ""; 
        }
    }
    return prefix
};

longestCommonPrefix(["flower", "flow", "flight"])
```