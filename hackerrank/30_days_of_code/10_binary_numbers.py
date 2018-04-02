# Task
#
# Given a base-10 integer, n, convert it to binary (base-2).
# Then find and print the base-10 integer denoting the maximum
# number of consecutive 1's in n's binary representation.

n = int(input().strip())

converted_number = bin(n)
print(converted_number)

current = 0
longest = 0

for i in converted_number:
    if i == '1':
        current += 1
    else:
        longest = max(longest, current)
        current = 0

print(max(longest, current))
