# Вам дается год, и вам нужно написать функцию, чтобы проверить, является ли год высокосным или нет.
#
# Вывод берется по шаблону. Ваша функция должна возвращать логическое значение (True / False)


def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True

    return leap


# Suggestion of solution in a discussion on HackerRank
# def is_leap(year):
#     return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


year = int(input())
print(is_leap(year))



