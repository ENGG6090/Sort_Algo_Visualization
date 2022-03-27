from ArrayToHistogram.array_to_histogram import plot_histogram
import random


def bubble_sort(nums):
    result = []
    n = len(nums)
    for i in range(n):
        for j in range(n - 1 - i):  # the last i items has been sorted already:
            if nums[j] > nums[j + 1]:
                result.append([j, i] + nums)  # record the status before swap
                nums[j], nums[j + 1] = nums[j + 1], nums[j]  # swap
                result.append([j + 1, i] + nums)  # record the status after swap
            else:
                result.append([j, i] + nums)  # does not need to swap

    result.append([n, n] + nums)
    return result


if __name__ == "__main__":
    test_data = list(range(27))
    random.shuffle(test_data)
    steps = bubble_sort(test_data)

    for i in range(len(steps)):
        step = steps[i]
        plot_histogram(step[2:], step[0], step[1], i)
