import matplotlib.pyplot as plt
import numpy as np
import random
import os

# Generate a frame of one step of sort,
# nums is a list of y values, red index is which column to show red, green index is from which column, all the columns greater than this are marked as green
# picture name index is used for sorting the frames to create a video in the next step, start from 0

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


def plot_histogram_range_green(nums, red_index=0, green_start=0, green_end=None, picture_name_index=0,
                               sort_method="insert", picture_folder="../Picture/", ):
    plt.figure(figsize=(3, 2.6), dpi=300)
    plt.axis('off')

    x_axis = np.arange(len(nums))
    y_values = nums
    colors = ["red" if _ == red_index else "blue" for _ in x_axis]

    if green_end==None:
        green_end = len(nums)

    for i in range(len(colors)):
        if i == red_index:
            continue
        if green_end >= i >= green_start:
            colors[i] = "green"
    plt.bar(x_axis, y_values, color=colors)
    # e.g picture_path = ../Picture/bubble/bubble01.png

    if not os.path.exists(picture_folder + sort_method + "/"):
        os.makedirs(picture_folder + sort_method + "/")
    picture_path = picture_folder + sort_method + "/" + sort_method + str(picture_name_index) + ".png"

    plt.savefig(picture_path, bbox_inches='tight')
    plt.close()




if __name__ == "__main__":
    test_data = list(range(10))
    random.shuffle(test_data)
    plot_histogram_range_green(test_data, 3)
