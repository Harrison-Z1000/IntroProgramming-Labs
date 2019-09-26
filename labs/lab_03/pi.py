# Introduction to Programming
# Author: Harrison Zheng
# Date: 09/25/19
# This program approximates the value of pi based on user input.


import math


def main():
    print("This program approximates the value of pi.")
    n = int(input("Enter the number of terms to be summed: "))
    piApproximation = approximate(n)  # Calls the approximate method, passing n as the argument
    print("The sum of the first", n, "terms of this series is", piApproximation)
    difference = math.pi - piApproximation  # Finds the difference between the approximated value and actual value of pi
    print("The difference between the approximation and the actual value of pi is", difference)


def approximate(n):
    total = 0.0
    for i in range(n):
        total = total + (-1.0) ** i / (2.0 * i + 1.0)  # The sign of each term in the sequence is always the opposite
        # of the last. The denominator of every term is odd and is two more than that of the previous term.
    return 4 * total  # The numerator of every term is 4 so multiply total by 4 to get the approximation of pi


main()
