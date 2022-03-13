from ArrayToHistogram.array_to_histogram import plot_histogram_range_green
import copy
import random


def merge_sort(a):
    result = []

    def sort(a, aux, lo, hi):
        if hi <= lo:
            return
        mid = lo + (hi - lo) // 2
        sort(a, aux, lo, mid)
        sort(a, aux, mid + 1, hi)
        merge(a, aux, lo, mid, hi)
        # print(a, lo, hi, mid)
        return result.append([mid, lo, hi] + a)

    def merge(a, aux, lo, mid, hi):
        aux = copy.deepcopy(a)  # copy

        i = lo
        j = mid + 1

        for k in range(lo, hi + 1):  # merge
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif aux[i] < aux[j]:
                a[k] = aux[i]
                i += 1
            else:
                a[k] = aux[j]
                j += 1

    sort(a, None, 0, len(a) - 1)

    return result


if __name__ == "__main__":
    test_data = list(range(100))
    random.shuffle(test_data)
    steps = merge_sort(test_data)
    print(steps)

    for i in range(len(steps)):
        step = steps[i]
        plot_histogram_range_green(step[3:], step[0], step[1], step[2], i, sort_method="mergesort")
