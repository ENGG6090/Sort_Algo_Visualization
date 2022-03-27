import random

from ArrayToHistogram.array_to_histogram import plot_histogram_range_green


# return a 2d array,
# each element is [red_index, green_start, green_end, the frame of this array]

def insertion_sort(nums):
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append([0, 0, 0] + nums)
            continue
        else:
            red_index = i
            key = nums[i]
            j = i - 1

            result.append([red_index, 0, red_index - 1] + nums)  # assume all the elements before index i are sorted

            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                nums[j] = key
                result.append([j, j + 1, red_index] +
                              nums)  # if need to exchange, set the current position of key to be red, then, the elements after this postion are green;
                j -= 1

            nums[j + 1] = key
            result.append([j, 0, red_index] + nums)

    result.append([0, 0, len(nums) - 1] + nums)  # insert an all green frame at the end

    return result


if __name__ == "__main__":
    test_data = list(range(15))
    random.shuffle(test_data)

    for i in range(len(test_data)):
        if test_data[i]==0:
            test_data[i]=0.5

    steps = insertion_sort(test_data)

    for i in range(len(steps)):
        step = steps[i]
        plot_histogram_range_green(step[3:], step[0], step[1], step[2], picture_name_index=str(i))
