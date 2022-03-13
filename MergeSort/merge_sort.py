import random


def merge_sort(nums_list):
    if len(nums_list) == 1:
        return
    else:
        mid = len(nums_list) // 2
        left = nums_list[:mid]
        right = nums_list[mid:]

        # do call back till the left_list or the right_list length drop to 1
        merge_sort(left)
        merge_sort(right)

        # i is the iterator for the left_list
        # j is the iterator for the right_list

        i = j = 0

        # K is the iterator for the final sorted_list
        K = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums_list[K] = left[i]
                i += 1
            else:
                nums_list[K] = right[j]
                j += 1

            K += 1

        # if i has reached to the final index of the left_list
        # OR j has reached to the final index of the right_part
        # But its counterpart has not reached to its final one,
        # we need to solve the remaining
        while i < len(left):
            nums_list[K] = left[i]
            i += 1
            K += 1

        while j < len(right):
            nums_list[K] = right[j]
            j += 1
            K += 1


test_data = list(range(25))
random.shuffle(test_data)
print(test_data)

merge_sort(test_data)
print(test_data)
