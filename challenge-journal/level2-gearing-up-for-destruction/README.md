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
  - [Baseline Test for Python Cases](#baseline-test-for-python-cases)
  - [Expanded Coverage for Python Cases](#expanded-coverage-for-python-cases)
- [Getting Started](#getting-started)
  - [How to Verify Your Solution](#how-to-verify-your-solution)
  - [Submission](#submission)
- [Additional Information](#additional-information)
  - [Status](#status)
  - [License](#license)

---

## Overview
As Commander Lambda's personal assistant, you are tasked with configuring the LAMBCHOP doomsday device's axial orientation gears. This README covers the details needed for this challenge.

### Personal Note

At first glance, the challenge appears straight forward: identify gear sizes that fulfill specific criteria. However, the task conceals an added layer of complexity. The solution must not only find a radius that meets the given constraints but must also express it as a simplified fraction \( \frac{a}{b} \), where both \( a \) and \( b \) are integers. This requirement introduces an additional layer of mathematical rigor to the problem. In otherwords, many other solution() examples have passed foo/bar validate, but I don't think they are actually correct solutions—I did not notice this until my first solution version passed 10/10 foobar validations, but was still failing my test cases. In this version, I hope to solve the challenge using the most efficent method; Remember—We are Commander Lambda's personal assistant:

> Commander Lambda loves efficency!

[Back to Top](#table-of-contents)

---

## Challenge Details

### The Problem

Due to the layout of the LAMBCHOP and its support system, the pegs that will support the gears are fixed in place. The goal is to build a system where the last gear rotates at twice the rate of the first gear, regardless of the direction.

### The Task
To configure the axial orientation gears for the LAMBCHOP doomsday device.The goal is to build a system where the last gear rotates at twice the rate (in revolutions per minute, or rpm) of the first gear, no matter the direction, using a function called `solution(pegs)` which takes a list of distinct positive integers named `pegs` representing the location of each peg along the support beam. The function should return the numerator and denominator of the first gear's radius in its simplest form if a solution exists. Otherwise, it should return `[-1, -1]`.

#### Inputs
- A sorted list `pegs` of distinct positive integers representing the center distances (peg positions) along a given support beam. The list will contain between 2 and 20 integers, each between 1 and 10,000 inclusive.

#### Outputs
- If a solution exists, the function should return a list `[a, b]` where:
  - **a**: The numerator of the first gear's radius in its simplest form.
  - **b**: The denominator of the first gear's radius in its simplest form.
  - Thus, the radius of the first gear will be \( \\frac{a}{b} \).
- If it is impossible to achieve the proper rotation ratio or gear sizes, return `[-1, -1]`.

#### Examples
- Input: `[4, 30, 50]`, Output: `[12, 1]`
### The Rules
- The list `pegs` will contain at least 2 and no more than 20 distinct positive integers.
- Each integer in `pegs` will be between 1 and 10,000 inclusive.
- The list `pegs` will be sorted in ascending order.
- A gear must be placed on each peg (otherwise the gears will collide with unoccupied pegs).
- The radius of each gear must be at least 1.

#### Special Cases
- The last gear should rotate at twice the rate of the first gear.
- The radius of the first gear should be returned in its simplest fractional form \( \\frac{a}{b} \).


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

- I'll provide a Python solution, see [`solution.py`](https://github.com/gavinmclelland/foobar-with-Google/blob/main/challenge-journal/level2-gearing-up-for-destruction/solution.py).


### Constraints for Python

- Your code will run inside a Python 2.7.13 sandbox.
- All tests will be run by calling the `solution()` function.
- Standard libraries are supported except for a few [listed in the original `constriaints.txt` file](https://github.com/gavinmclelland/foobar-with-Google/blob/main/challenge-journal/level2-gearing-up-for-destruction/constraints.txt).
- Input/output operations are not allowed.
- Your solution must be under 32,000 characters in length.

### Baseline Test for Python Cases

`solution.py` code should pass the following test cases:

| Test Case No. | Solution()                 | Expected Output  | Scenario                                     |
|---------------|----------------------------|------------------|----------------------------------------------|
| 1             | `[1, 2]`                   | `[-1, -1]`       | Non-solvable case                            |
| 2             | `[4, 30, 50]`              | `[12, 1]`        | Typical case                                 |


### Expanded Coverage for Python Cases

These cases have been carefully selected to test the function across a range of potential hidden unit test case scenarios:

| Test Case No.  | Function to Test | Arguments                          | Expected Output    | Scenario                   |
|----------------|------------------|------------------------------------|--------------------|-----------------------------|
| 1              | `solution`       | `[[1, 2]]`                         | `[-1, -1]`         | Unsolvable-Small Gap        |
| 2              | `solution`       | `[[4, 30, 50]]`                    | `[12, 1]`          | Baseline-Solvable           |
| 3              | `solution`       | `[[1, 100000]]`                    | `[-1, -1]`         | Unsolvable-Large Gap        |
| 4              | `solution`       | `[[10, 5]]`                        | `[-1, -1]`         | Non-Ascending Pegs          |
| 5              | `solution`       | `[[1, 4, 9]]`                      | `[4, 3]`           | Fractional Gear             |
| 6              | `solution`       | `[[1, 3, 6]]`                      | `[2, 1]`           | Small Distances             |
| 7              | `solution`       | `[[1, 3, 7, 15, 31]]`              | `[-1, -1]`         | Patterned-Unsolvable        |
| 8              | `solution`       | `[[10000, 20000]]`                 | `[-1, -1]`         | Max Gap-Unsolvable          |
| 9              | `solution`       | `[[4, 17, 50]]`                    | `[-1, -1]`         | Three Pegs-Unsolvable       |
| 10             | `solution`       | `[[i for i in range(500, 10001, 500)]]` | `[1000, 3]`    | Max Pegs                    |
| 11             | `solution`       | `[[1, 51]]`                        | `[100, 3]`         | Large Initial Gap           |
| 12             | `solution`       | `[[1, 31]]`                        | `[20, 1]`          | Small Initial Gap           |
| 13             | `solution`       | `[[1, 31, 51, 71]]`                | `[20, 1]`          | Incrementing Gaps           |
| 14             | `solution`       | `[[1, 31, 51, 71, 91]]`            | `[20, 1]`          | Consistent Gaps             |
| 15             | `solution`       | `[[4, 9, 17, 31, 40]]`             | `[4, 1]`           | Random Pegs                 |




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

For more information, refer to the original challenge description provided in [readme.txt](https://github.com/gavinmclelland/foobar-with-Google/blob/main/challenge-journal/level2-gearing-up-for-destruction/readme.txt)


### Status
- Work in progress

---
## License
This project is licensed under MPL 2.0.

[Back to Top](#table-of-contents)
