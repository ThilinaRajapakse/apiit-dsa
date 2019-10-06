def insertion_sort(lst):
    for i in range(len(lst) - 1):
        j = i + 1

        while j > 0 and lst[j] < lst[j - 1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1

    return lst

# l = [3, 1, 5, 10, 23, 56, 4, 2]
# print(f'Initial list: {l}')
# l = insertion_sort(l)
# print(f'Sorted list: {l}')