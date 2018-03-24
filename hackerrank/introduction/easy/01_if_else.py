# Задано целое число n, выполните следующие условные действия:
#
# Если n нечетно (odd), напечатайте Weird
# Если n четное (even) и входит в диапазон от 2 до 5, напечатайте Not Weird
# Если n четное (even) и входит в диапазон от 6 до 20, напечатайте Weird
# Если n четное (even) и больше 20, напечатайте Not Weird

n = int(input())

# Нечетное
if n % 2 != 0:
    print('Weird')
# Четное
elif n % 2 == 0 and 2 <= n <= 5:
    print('Not Weird')
elif n % 2 == 0 and 6 <= n <= 20:
    print('Weird')
elif n % 2 == 0 and n > 20:
    print('Not Weird')
