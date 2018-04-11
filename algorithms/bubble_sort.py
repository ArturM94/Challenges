unsort_list = [5, 3, 8, 1, 4]


def bubble_sort(unsort_list):
    last_index = len(unsort_list) - 1
    for i in range(0, last_index):
        for j in range(0, last_index - i):
            if unsort_list[j] > unsort_list[j + 1]:
                unsort_list[j], unsort_list[j + 1] = unsort_list[j + 1], unsort_list[j]
    return unsort_list


print('Unsort list: ', unsort_list)
sort_list = bubble_sort(unsort_list)
print('Sort list: ', sort_list)