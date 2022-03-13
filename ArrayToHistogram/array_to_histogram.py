import matplotlib.pyplot as plt
import numpy as np
import random


def plot_histogram(nums, red_index=0, green=0, picture_name_index = 0):
    plt.figure(figsize=(3, 2.6), dpi=300)
    plt.axis('off')

    x_axis = np.arange(len(nums))
    y_values = nums
    colors = ["red" if _ == red_index else "blue" for _ in x_axis]

    if green != 0:
        colors = colors[:-green] + ["green"] * green

    plt.bar(x_axis, y_values, color=colors)
    # plt.show()
    plt.savefig("../Picture/BubbleSort/bubble"+str(picture_name_index)+".png", bbox_inches='tight')
    plt.close()




if __name__ == "__main__":
    test_data = list(range(10))
    random.shuffle(test_data)
    plot_histogram(test_data, 4)
