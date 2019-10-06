def mergesort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2

        left = lst[:mid]
        right = lst[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]

                i += 1
            else:
                lst[k] = right[j]

                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
        # if i == len(left):
        #     lst[k:] = lst[j:]
        # else:
        #     lst[k:] = lst[i:]

    return lst

# l = [3, 1, 5, 10, 23, 56, 4, 2]
# print(f'Initial list: {l}')
# l = mergesort(l)
# print(f'Sorted list: {l}')