
import random

from ArrayToHistogram.array_to_histogram import plot_histogram_range_green
from CreateVideo.create_video import make_video
from InsertionSort.insertion_sort import insertion_sort

# make frames first
test_data = list(range(27))
random.shuffle(test_data)
sort_method = "insert"

for i in range(len(test_data)):
    if test_data[i] == 0:
        test_data[i] = 0.5

steps = insertion_sort(test_data)

for i in range(len(steps)):
    step = steps[i]
    plot_histogram_range_green(step[3:], step[0], step[1], step[2], picture_name_index=str(i), sort_method=sort_method, picture_folder="./Picture/")

# make video after
make_video(picture_folder="./Picture/",video_folder="./Video/",folder_name_under_Picture_dir = sort_method)