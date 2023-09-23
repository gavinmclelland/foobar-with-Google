# File: solution.py
# Author: Gavin MCLELLAND
# Date: 2023-09-19
#
# This file contains the solution to the "Skipping Work" challenge. In this
#	challenge, we are given two lists of Worker IDs. One list has all workers
# who completed their tasks, and the other list has all workers but one who is
# skipping work. The objective is to identify the Worker ID of the worker who
# is skipping work. The solution uses bitwise XOR for an efficient O(n) time
# complexity and O(1) space complexity. This algorithm is particularly useful
# for quickly identifying the unique, unpaired element in large datasets.
#

# Solution for finding the unique integer between two lists
def solution(x, y):
	"""

	Given two lists of Worker IDs, List x and List y, one of which has an extra
	element, this function identifies and returns that extra element. The
	function uses bitwise XOR to achieve this in O(n) time and O(1) space.

	Args:
	x, y: Lists of integers. One of the lists contains an extra unique integer.

	Returns:
	- The unique integer found in one of the lists.

	Raises:
	- ValueError: If the lists are identical, which contradicts the
		challenge premise.
	"""

	# Using 0 as an initializer for XOR operation ensures that the
	# XOR of the first element with 0 will be the element itself.
	unique_worker_id_xor = 0

	# XOR operation with all worker IDs in list x
	for worker_id in x:
			unique_worker_id_xor ^= worker_id

	# XOR operation with all worker IDs in list y
	for worker_id in y:
			unique_worker_id_xor ^= worker_id

	# Debugging line: Uncomment line 30 to print the final XOR result,
	# which can help in debugging the function's behavior during testing:
	# print("Debug: Returning XOR result: {}".format(unique_worker_id_xor))

	# If XOR result is 0, it could mean that either all IDs are paired
	# between the lists, or that the unpaired ID is actually 0. We use
	# list lengths to distinguish between these scenarios.
	if unique_worker_id_xor == 0:
		if len(x) != len(y):
			return 0 # Lists have different lengths; unique ID is 0.
		else:
			# Both lists are identical, which is against the problem's assumptions
			# TODO(gavinmclelland): Python's built-in exceptions keeps the code
			# simple, but consider using a custom exception like IdenticalListError
			# for more descriptive error handling in a more complex project.
			raise ValueError(
				"All workers are present in both lists. No worker is skipping work. "
				"List lengths: x={}, y={}. Commander Lambda loves efficiency!"
				.format(len(x), len(y))
			)

	# Return the unique worker ID found via XOR operation
	return unique_worker_id_xor

# test_solution() Conducts unit tests on the solution() function
def test_solution():
	"""
	Test the solution function using a variety of test cases, including:
	- Typical scenarios with positive and negative numbers
	- Edge cases with zero and boundary values
	- Cases where the lists are not strictly identical

	Raises:
			AssertionError: If any of the test cases fail.

	Returns:
			None
	"""
	# TODO(gavinmclelland): Integrate with unittest or pytest for
	# scalability and better assertion handling if solution() function
	# moves to a complex project.

	# Test for Typical Scenarios
	print("Testing typical scenarios...")
	try:
			# Test if function handles typical cases with positive numbers
			assert solution([13, 5, 6, 2, 5], [5, 2, 5, 13]) == 6
			print("Passed: Typical positive cases - [13, 5, 6, 2, 5], "
						"[5, 2, 5, 13]")
	except AssertionError:
			print("Failed: Typical positive cases - [13, 5, 6, 2, 5], "
						"[5, 2, 5, 13]")

	try:
			# Test if function handles typical cases with negative numbers
			assert solution([14, 27, 1, 4, 2, 50, 3, 1],
											[2, 4, -4, 3, 1, 1, 14, 27, 50]) == -4
			print("Passed: Typical negative cases - [14, 27, 1, 4, 2, 50, 3, 1], "
						"[2, 4, -4, 3, 1, 1, 14, 27, 50]")
	except AssertionError:
			print("Failed: Typical negative cases - [14, 27, 1, 4, 2, 50, 3, 1], "
						"[2, 4, -4, 3, 1, 1, 14, 27, 50]")

	# Test for Boundary Conditions
	print("Testing boundary conditions...")
	try:
			# Test for positive boundary values
			assert solution([-1000], [-1000, 1000]) == 1000
			print("Passed: Positive boundary values - [-1000], [-1000, 1000]")
	except AssertionError:
			print("Failed: Positive boundary values - [-1000], [-1000, 1000]")

	try:
			# Test for negative boundary values
			assert solution([1000], [-1000, 1000]) == -1000
			print("Passed: Negative boundary values - [1000], [-1000, 1000]")
	except AssertionError:
			print("Failed: Negative boundary values - [1000], [-1000, 1000]")

	# Test for Edge Cases
	print("Testing edge cases...")
	try:
			# Test if function can correctly identify that the unique element is 0
			# when other elements are non-zero integers.
			assert solution([1, 2, 3], [3, 2, 1, 0]) == 0
			print("Passed: Unique number is zero - [1, 2, 3], [3, 2, 1, 0]")
	except AssertionError:
			print("Failed: Unique number is zero - [1, 2, 3], [3, 2, 1, 0]")

	try:
			# Test if function can correctly identify that the unique element is 0
			# when all other elements are also 0.
			assert solution([0, 0, 0], [0, 0]) == 0
			print("Passed: All elements are zero - [0, 0, 0], [0, 0]")
	except AssertionError:
			print("Failed: All elements are zero - [0, 0, 0], [0, 0]")

	print("All edge unit tests evaluated.")

	# Test for ValueError integrity
	print("Testing ValueError integrity...")
	try:
		# Test if function raises a ValueError for identical lists, which is against
		# the problem's assumptions.
		result = solution([1, 2, 3], [1, 2, 3])
		print("Failed: Both lists are identical - [1, 2, 3], [1, 2, 3]")
		# This line should not be reached
	except ValueError:
		print("Passed: Both lists are identical - [1, 2, 3], [1, 2, 3]")
		# This line should be reached
	except AssertionError:
		print("Failed: Unexpected AssertionError - [1, 2, 3], [1, 2, 3]")

if __name__ == '__main__':
	test_solution()