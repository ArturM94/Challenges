# Task
#
# Write a 'factorial' function that takes a positive integer,
# N as a parameter and prints the result of N! (N factorial).
#
# Note: If you fail to use recursion or fail to name your recursive
# function 'factorial' or 'Factorial', you will get a score of 0.


def factorial(n):
    # Base Case
    if n <= 1:
        return 1
    # Recursive Case
    else:
        # If n = 3:
        # 3 * factorial(2)
        # 3 * 2 * factorial(1)
        # 3 * 2 * 1 = 6
        return n * factorial(n - 1)


if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
