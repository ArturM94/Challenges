# Task
#
# Given n names and phone numbers, assemble a phone book
# that maps friends' names to their respective phone numbers.
# You will then be given an unknown number of names to query
# your phone book for. For each name queried, print the associated
# entry from your phone book on a new line in the form name=phoneNumber;
# if an entry for name is not found, print Not found instead.
#
# Note: Your phone book should be a Dictionary/Map/HashMap data structure.

n = int(input())
# Разбиение входной строки на список, состоящий из 2-х элементов: имя и номер.
data = [input().split() for i in range(n)]
# Создание словаря из разделенных строк.
# Пара 'key: value' прогоняется по списку data, тем самым для key и value
# присваивается первый и второй элементы списка соответсвенно.
phone_book = {key: value for key, value in data}

while True:
    name = input(str())
    if name not in phone_book:
        print('Not found')
    else:
        # f-strings
        print(f'{name}={phone_book[name]}')
        # % operator
        # print('%s=%s' % (name, phone_book[name]))
