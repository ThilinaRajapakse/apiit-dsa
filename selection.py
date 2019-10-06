def selection_sort(lst):
    for i in range(len(lst)):
        smallest_idx = i

        for j in range(i+1, len(lst)):
            if lst[j] < lst[smallest_idx]:
                smallest_idx = j
        lst[i], lst[smallest_idx] = lst[smallest_idx], lst[i]

    return lst

# l = [3, 1, 5, 10, 23, 56, 4, 2]
# print(f'Initial list: {l}')
# l = selection_sort(l)
# print(f'Sorted list: {l}')