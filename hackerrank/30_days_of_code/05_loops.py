n = int(input().strip())

for i in range(1, 11):
    result = n * i
    # f-strings
    print(f'{n} x {i} = {result}')
    # % operator
    # print('%s x %s = %s' % (n, i, result))
