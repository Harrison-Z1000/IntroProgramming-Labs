# Introduction to Programming
# Author: Harrison Zheng
# Date: 09/25/19
# This program computes the nth Fibonacci number given by the user.


def main():
    n = int(input("Which Fibonacci number would you like to compute? "))  # Asks the user to choose the number in the
    # Fibonacci sequence that they want
    fibNumber = fibonacci(n)  # Calls the fibonacci method, passing n as the argument
    print("The", n, "th Fibonacci number is", fibNumber)  # Prints the calculated Fibonacci number


def fibonacci(n):
    if n < 0:  # No negative Fibonacci numbers
        return
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Calculates the Fibonacci number by calling the method it is in


main()
