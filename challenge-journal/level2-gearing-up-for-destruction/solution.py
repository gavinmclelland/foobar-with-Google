# File: solution.py
# Author: Gavin MCLELLAND
# GitHub: https://github.com/gavinmclelland
# Date: 2023-09-28
#
# This file contains the solution to the "Gearing up for destruction" challenge.
# Given a list of peg positions, the objective is to calculate the optimal
# first gear radius. The solution uses Python's Fraction class for precise
# arithmetic. The algorithm has a complexity of O(n), where n is the number of
# pegs. It is useful for problems involving series, sequences, and ratios.
#
# Solution for optimal first gear radius calculation
from fractions import Fraction

def calculate_radius_output(distance_center, divisor):
    radius_output = 0
    sign = 1  # Start with a positive sign

    for d in distance_center:
        radius_output += sign * d  # Add or subtract the distance based on the current sign
        sign *= -1  # Flip the sign for the next term

    # Divide by the divisor
    radius_output /= divisor

    return radius_output

def solution(pegs):
    gear_pegs = len(pegs)
    if gear_pegs < 2:
        return [-1, -1]
    # Initial proposed radius for the first gear based on peg positions.
    radius_drive_estimate = 2 * (sum(pegs[1::2]) - sum(pegs[::2])) + pegs[0]

    # Calculate the distance between consecutive pegs
    distance_center = [pegs[i+1] - pegs[i] for i in range(gear_pegs - 1)]

    # Check for small and large gaps
    if any(dist < 2 for dist in distance_center) or any(dist > 10000 for dist in distance_center):
        return [-1, -1]

    # Calculate the divisor for the output gear radius
    divisor = 3 if gear_pegs % 2 == 0 else 1

    # Calculate the initial radius for the output gear
    radius_output = calculate_radius_output(distance_center, divisor)
    if radius_output < 1:
        return [-1, -1]

    # Calculate the initial radius for the drive gear (Constraint: x = 2y)
    radius_input = 2 * radius_output
    gear_drive = radius_input

    # If x is less than 2 or y is less than 1, the configuration is impossible
    if radius_input < 2 or radius_output < 1:
        return [-1, -1]

    gear_drive = Fraction(radius_input).limit_denominator()

    # Check that all gears fit
    for i in range(gear_pegs - 1):
        distance_center = pegs[i + 1] - pegs[i]
        gear_size = distance_center - radius_input
        if gear_size < 1:
            return [-1, -1]
        radius_input = gear_size

    # Case when the number of pegs is even
    if len(pegs) % 2 == 0:
        # Adjust the proposed solution for the last peg
        radius_drive_estimate = 2 * (radius_drive_estimate - pegs[-1])
        # If the resulting radius is less than 1, the task is impossible
        if radius_drive_estimate / 3 < 1:
            return [-1, -1]
        first_gear_size = [radius_drive_estimate // 3, 1] if radius_drive_estimate % 3 == 0 else [radius_drive_estimate, 3]

    # Case when the number of pegs is odd
    else:
        # Adjust the proposed solution for the last peg
        radius_drive_estimate = 2 * (radius_drive_estimate + pegs[-1])
        # If the resulting radius is less than 1, the task is impossible
        if radius_drive_estimate < 1:
            return [-1, -1]
        # The proposed radius is a whole number
        first_gear_size = [radius_drive_estimate, 1]

    # Start with the first gear's radius
    remaining_radius = first_gear_size[0] / first_gear_size[1]

    # Check if all gears fit
    for i in range(len(pegs) - 1):
        next_radius = pegs[i + 1] - pegs[i] - remaining_radius  # Calculate the remaining radius for the next gear
        if next_radius < 1:  # If it's less than 1, the task is impossible
            return [-1, -1]
        remaining_radius = next_radius  # Update remaining_radius for the next iteration

    ### Validate remaining radii for all gears
    remaining_radius = float(gear_drive)
    for i in range(gear_pegs - 1):
      next_radius = pegs[i + 1] - pegs[i] - remaining_radius
      if next_radius < 1:
          return [-1, -1]
      remaining_radius = next_radius

    # Return the radius of the first gear and the smallest common denominator
    return first_gear_size



# You can add your test cases here to verify the function


def assert_equal(actual, expected, message):
    if actual != expected:
        raise AssertionError("Failed: {} - Expected: {}, Got: {}".format(message, expected, actual))

def assert_that(actual, operator, expected, message):
    if operator == '==':
        assert actual == expected, 'Fail: ' + message + ' - Expected: ' + str(expected) + ', Got: ' + str(actual)
    elif operator == '!=':
        assert actual != expected, 'Fail: ' + message + ' - Expected not equal to: ' + str(expected) + ', Got: ' + str(actual)
    elif operator == '>':
        assert actual > expected, 'Fail: ' + message + ' - Expected greater than: ' + str(expected) + ', Got: ' + str(actual)
    elif operator == '<':
        assert actual < expected, 'Fail: ' + message + ' - Expected less than: ' + str(expected) + ', Got: ' + str(actual)
    elif operator == '>=':
        assert actual >= expected, 'Fail: ' + message + ' - Expected greater than or equal to: ' + str(expected) + ', Got: ' + str(actual)
    elif operator == '<=':
        assert actual <= expected, 'Fail: ' + message + ' - Expected less than or equal to: ' + str(expected) + ', Got: ' + str(actual)
    else:
        raise ValueError("Unsupported operator: " + str(operator))

def foobar_fiesta(test_cases):
    total_tests = len(test_cases)
    passed_tests = 0

    # ANSI escape codes for colored output
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

    for i, (func, args, expected, scenario) in enumerate(test_cases):
        result = None
        try:
            result = func(*args)
            assert result == expected, "Expected: {}, Got: {}".format(expected, result)
            print("\033[92mPASS\033[0m: Test Case {} - {}".format(i + 1, scenario))
            passed_tests += 1
        except Exception as e:
            print("\033[91mFAIL\033[0m: Test Case {} - {}".format(i + 1, e))

    print("\n\033[94mSummary:\033[0m")
    print("Total tests: {}".format(total_tests))
    print("Passed: {}".format(passed_tests))
    print("Failed: {}".format(total_tests - passed_tests))


# Test cases [(function_to_test, arguments, expected_result, scenario_name)]

test_cases = [
    # Tests small gap between pegs, unsolvable.
    (solution, [[1, 2]], [-1, -1], "Unsolvable-Small Gap"),

    # Standard test with a known solvable solution.
    (solution, [[4, 30, 50]], [12, 1], "Baseline-Solvable"),

    # Tests large gap between pegs, unsolvable.
    (solution, [[1, 100000]], [-1, -1], "Unsolvable-Large Gap"),

    # Tests non-ascending order of pegs.
    (solution, [[10, 5]], [-1, -1], "Non-Ascending Pegs"),

    # Tests fractional gear radius.
    (solution, [[1, 4, 9]], [4, 3], "Fractional Gear"),

    # Tests small distances between pegs.
    (solution, [[1, 3, 6]], [2, 1], "Small Distances"),

    # Tests specific pattern of pegs, unsolvable.
    (solution, [[1, 3, 7, 15, 31]], [-1, -1], "Patterned-Unsolvable"),

    # Tests max possible gap between pegs.
    (solution, [[10000, 20000]], [-1, -1], "Max Gap-Unsolvable"),

    # Tests only three pegs, unsolvable.
    (solution, [[4, 17, 50]], [-1, -1], "Three Pegs-Unsolvable"),

    # Tests max number of pegs, solvable.
    (solution, [[i for i in range(500, 10001, 500)]], [1000, 3], "Max Pegs"),

    # Tests large initial gap.
    (solution, [[1, 51]], [100, 3], "Large Initial Gap"),

    # Tests small initial gap.
    (solution, [[1, 31]], [20, 1], "Small Initial Gap"),

    # Tests incrementing gaps.
    (solution, [[1, 31, 51, 71]], [20, 1], "Incrementing Gaps"),

    # Tests consistently incrementing gaps.
    (solution, [[1, 31, 51, 71, 91]], [20, 1], "Consistent Gaps"),

    # Tests randomly placed pegs.
    (solution, [[4, 9, 17, 31, 40]], [4, 1], "Random Pegs")
]

if __name__ == '__main__':
    foobar_fiesta(test_cases)