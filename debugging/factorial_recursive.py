#!/usr/bin/python3
import sys

# Function Description:
# This function calculates the factorial of a given number n using recursion.
# A factorial of a number n is the product of all positive integers less than or equal to n.
# Example: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120

# Parameters:
# n (int): The number for which the factorial is to be calculated. It must be a non-negative integer.

# Returns:
# int: The factorial of the given number n. If n is 0, the factorial is defined as 1.
def factorial(n):
    if n == 0:
        return 1  # The base case: 0! is 1
    else:
        return n * factorial(n-1)  # Recursively calculate the factorial

# The program takes a number from the command line argument and calculates its factorial
f = factorial(int(sys.argv[1]))  # Convert the input argument to an integer and call the factorial function
print(f)  # Print the calculated factorial
