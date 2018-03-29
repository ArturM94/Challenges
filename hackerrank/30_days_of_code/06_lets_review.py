# Task
#
# Given a string, S, of length N, that is indexed from 0 to N - 1,
# print its even-indexed and odd-indexed characters as 2 space-separated strings
# on a single line (see the Sample below for more detail).
#
# Note: 0 is considered to be an even index.

# Number of test cases
for t in range(int(input())):
    # Each test case contain a string
    s = str(input())

    index = 0
    odd = ''
    even = ''

    for index, i in enumerate(s):
        if index % 2 == 0:
            even = even + i
        else:
            odd = odd + i

    print(even, odd, end='' + '\n')
