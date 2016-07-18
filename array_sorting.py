## Array Sorting

# Choose one of the array sorting algorithms and implement it. You will use Python's lists and pretend they are arrays but you are not allow to use:
#
# 1. append()
# 2. insert()
# 3. del
# 4. slicing
# 5. any other weird stuff other than arr[i], arr[i] = value, and len(arr).
#
# Your function will take in an array argument, and it will sort that array in-place - as in, it will modify the array that is being sorted. For example:
#
# >>> arr = [45, 3, 8, 2, 9, 10, 11]
# >>> bubble_sort(arr)
# >>> arr
# [2, 3, 8, 9, 10, 11, 45]
#
# We will have a competition for who can implement the fastest sort!


def bubble_sort(my_list):
    did_swap = True
    while did_swap:
        did_swap = False
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                did_swap = True
    return my_list

print bubble_sort([45, 3, 8, 2, 9, 10, 11])
