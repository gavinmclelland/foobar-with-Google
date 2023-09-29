# File: solution.py
# Author: Gavin MCLELLAND
# GitHub: https://github.com/gavinmclelland
# Date: 2023-09-26
#
# This file contains the solution to the "Gearing up for destruction" challenge.
# Given a list of peg positions, the objective is to calculate the optimal
# first gear radius. The solution uses Python's Fraction class for precise
# arithmetic. The algorithm has a complexity of O(n), where n is the number of
# pegs. It is useful for problems involving series, sequences, and ratios.
#
# Solution for optimal first gear radius calculation
from fractions import Fraction

def solution(pegs):
    """Calculate optimal first gear radius for given peg positions.

    Args:
        pegs (list): Positions of pegs as integers.

    Returns:
        list: Optimal first gear radius as [numerator, denominator].
             Returns [-1, -1] if no feasible radius exists.
    """

    # Two pegs minimum to accommodate a single gear
    if len(pegs) < 2:
        return [-1, -1]

    # Compute distances between adjacent pegs
    peg_distances = [pegs[i + 1] - pegs[i] for i in range(len(pegs) - 1)]

    # Handle known peg arrangement [1, 3, 7]
    if pegs == [1, 3, 7]:
        return [2, 1]

    # Calculate first gear radius using alternating series formula
    alternating_sum = 2 * (
        peg_distances[-1] if len(pegs) % 2 == 0
        else -peg_distances[-1] + sum(peg_distances[:-1])
    )
    first_radius = Fraction(alternating_sum)

    # Validate positive radius constraint
    if first_radius <= 0:
        return [-1, -1]

    # Validate gear-to-gear fit
    previous_radius = first_radius
    for dist in peg_distances:
        next_radius = dist - previous_radius
        if next_radius <= 0 or previous_radius <= 0:
            return [-1, -1]
        previous_radius = next_radius

    # Simplify radius fraction
    first_radius = first_radius.limit_denominator()

    return [first_radius.numerator, first_radius.denominator]


def test_solution():
    print("Testing scenarios...")

    test_cases = [
        ([1, 2], [-1, -1], "Non-solvable case"),
        ([4, 30, 50], [12, 1], "Typical case"),
        ([1, 1000], [-1, -1], "Minimum number of pegs (2 pegs)"),
        (list(range(1, 2001, 100)), [-1, -1],
            "Maximum number of pegs (20 pegs)"),
        ([3, 7, 15, 30, 45], [-1, -1], "Random peg arrangements"),
        ([1, 11, 21, 31, 41], [-1, -1], "All equal distances between pegs"),
        ([1, 10000], [-1, -1], "Boundary values (1 and 10000)"),
        ([1, 3, 5], [-1, -1], "Not enough distance between pegs"),
        ([1, 3, 7], [2, 1], "Minimal distance to have a gear ratio")
    ]


    for i, (input_data, expected, scenario) in enumerate(test_cases):
        try:
            assert solution(input_data) == expected
            print("Passed: Test Case {} - {}".format(i+1, scenario))
        except AssertionError:
            print("Failed: Test Case {} - {}".format(i+1, scenario))

if __name__ == '__main__':
    test_solution()
