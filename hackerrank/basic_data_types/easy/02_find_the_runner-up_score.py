#  You are given n scores. Store them in a list and find the score of the runner-up.

n = int(input())
arr = map(int, input().split())

list_arr = list(arr)
list_max = max(list_arr)

while max(list_arr) == list_max:
    list_arr.remove(max(list_arr))

print(max(list_arr))
