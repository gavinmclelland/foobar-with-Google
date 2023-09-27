# Gearing Up for Destruction with Google Foobar

## Table of Contents

- [Overview](#overview)
- [Challenge Details](#challenge-details)
  - [The Problem](#the-problem)
  - [The Task](#the-task)
  - [The Rules](#the-rules)
- [Technical Details](#technical-details)
  - [Language](#language)
  - [Problem Specification](#problem-specification)
  - [Constraints for Python](#constraints-for-python)
  - [Python Cases](#python-cases)
  - [Expanded Coverage for Python Cases](#expanded-coverage-for-python-cases)
- [Getting Started](#getting-started)
  - [How to Verify Your Solution](#how-to-verify-your-solution)
  - [Submission](#submission)
- [Additional Information](#additional-information)
  - [Status](#status)
  - [More Information](#more-information)

---

## Overview
As Commander Lambda's personal assistant, you are tasked with configuring the LAMBCHOP doomsday device's axial orientation gears. This README covers the details needed for this challenge.


[Back to Top](#table-of-contents)

---

## Challenge Details

### The Problem

Due to the layout of the LAMBCHOP and its support system, the pegs that will support the gears are fixed in place. The goal is to build a system where the last gear rotates at twice the rate of the first gear, regardless of the direction.

### The Task

Write a function called `solution(pegs)` which takes a list of distinct positive integers named `pegs` representing the location of each peg along the support beam. The function should return the numerator and denominator of the first gear's radius in its simplest form if a solution exists. Otherwise, it should return `[-1, -1]`.

### The Rules

- The list `pegs` will be given sorted in ascending order.
- `pegs` will contain at least 2 and no more than 20 distinct positive integers.
- All integers will be between 1 and 10000 inclusive.

[Back to Top](#table-of-contents)

---

## Technical Details
### Problem Specification

| Topic        | Details       |
|--------------|---------------|
| **Objective**  | Create a gear system with the correct rotation ratio. |
| **Function Signature** | `solution(pegs: List[int]) -> List[int]` |
| **Input**       | A list of distinct positive integers named `pegs`. |
| **Output**      | A list of two integers representing the numerator and denominator of the first gear's radius in its simplest form, or `[-1, -1]` if a solution is not possible. |

### Language

- I'll provide a Python solution, see `solution.py`.


### Constraints for Python

- Your code will run inside a Python 2.7.13 sandbox.
- All tests will be run by calling the `solution()` function.
- Standard libraries are supported except for a few [listed in the original `constriaints.txt` file](constraints.txt).
- Input/output operations are not allowed.
- Your solution must be under 32,000 characters in length.

### Python Cases

`solution.py` code should pass the following test cases:

| Test Case No. | Solution()                 | Expected Output  | Scenario                                     |
|---------------|----------------------------|------------------|----------------------------------------------|
| 1             | `[1, 2]`                   | `[-1, -1]`       | Non-solvable case                            |
| 2             | `[4, 30, 50]`              | `[12, 1]`        | Typical case                                 |


### Expanded Coverage for Python Cases

These cases have been carefully selected to test the function across a range of potential hidden unit test case scenarios:

| Test Case No. | Solution()                 | Expected Output  | Scenario                                     |
|---------------|----------------------------|------------------|----------------------------------------------|
| 3             | `[1, 1000]`                | TBD              | Minimum number of pegs (2 pegs)              |
| 4             | `[1, 100, 200, ..., 2000]` | TBD              | Maximum number of pegs (20 pegs)             |
| 5             | `[3, 7, 15, 30, 45]`       | TBD              | Random peg arrangements                      |
| 6             | `[1, 11, 21, 31, 41]`      | TBD              | All equal distances between pegs             |
| 7             | `[1, 10000]`               | TBD              | Boundary values (1 and 10000)                |



[Back to Top](#table-of-contents)

---

## Getting Started

### How to Verify Your Solution

When you are finished editing your code, test your solution and see how it does:

``` bash
verify solution.py
```


### Submission

Once you're confident your solution works, use the `submit` command to submit your answer.

```bash
submit solution.py
```

[Back to Top](#table-of-contents)

---


## Additional Information

For more information, refer to the original challenge description provided in [readme.txt](https://github.com/gavinmclelland/foobar-with-Google/blob/main/challenge-journal/level1-skipping-work/readme.txt)


### Status
- Work in progress

---
## License
This project is licensed under MPL 2.0.

[Back to Top](#table-of-contents)
