unsort_list = [9, 3, 2, 10, 4]


def insertion_sort(unsort_list):
    for i in range(0, len(unsort_list)):
        j = i
        while j > 0 and unsort_list[j] < unsort_list[j - 1]:
            unsort_list[j], unsort_list[j - 1] = unsort_list[j - 1], unsort_list[j]
            j = j - 1
    return unsort_list


print('Unsort list: ', unsort_list)
sort_list = insertion_sort(unsort_list)
print('Sort list: ', sort_list)
