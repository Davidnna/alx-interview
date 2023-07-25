_ALX INTERVIEW__


*0x02-Minimum_Operations*


## 0. Minimum Operations

In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

- Prototype: def minOperations(n)
- Returns an integer
- If n is impossible to achieve, return 0

### Example:

n = 9<br>

H => Copy All => Paste => HH => Paste => HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH<br>

Number of operations: 6
