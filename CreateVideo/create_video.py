import os
from os.path import isfile, join

import cv2


def sort_by_sufix_number(fileitem):
    filename, prefix = fileitem
    if filename.startswith(prefix):
        num = filename[len(prefix):-4] # remove ".png" and prefix
        return int(num)


def convert_pictures_to_video(pathIn, pathOut, fps, time, prefix="bubble"):
    ''' this function converts images to video'''
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    prefix_list = [prefix for _ in range(len(files))]
    files_zip_with_prefix = list(zip(files, prefix_list))
    files_zip_with_prefix.sort(key=sort_by_sufix_number)

    print("I am going to make a video!!!")

    for i in range(len(files_zip_with_prefix)):
        filename = pathIn + files_zip_with_prefix[i][0]
        '''reading images'''
        img = cv2.imread(filename)
        # img=cv2.resize(img,(1400,1000))
        height, width, layers = img.shape
        size = (width, height)

        for k in range(time):
            frame_array.append(img)
    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()


# Example:

def make_video(picture_folder = "../Picture/", video_folder = "../Video/",folder_name_under_Picture_dir="BubbleSort"):
    directory = f'{picture_folder}{folder_name_under_Picture_dir}'
    pathIn = directory + '/'
    pathOut = f'{video_folder}{folder_name_under_Picture_dir}.avi'
    fps = 15
    time = 1  # the duration of each picture in the video
    convert_pictures_to_video(pathIn, pathOut, fps, time, folder_name_under_Picture_dir)
