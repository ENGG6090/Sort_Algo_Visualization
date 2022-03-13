import cv2
import numpy as np
import glob
import os
from os.path import isfile, join

def sort_by_sufix_number(filename, prefix = "bubble"):
    if filename.startswith(prefix):
        num = filename[len(prefix):-4]
        return int(num)

def convert_pictures_to_video(pathIn, pathOut, fps, time):
    ''' this function converts images to video'''
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    files.sort(key=sort_by_sufix_number)
    for i in range(len(files)):
        filename = pathIn + files[i]
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
directory = '../Picture/BubbleSort'
pathIn = directory + '/'
pathOut = '../Video/BubbleSort.avi'
fps = 15
time = 1  # the duration of each picture in the video
convert_pictures_to_video(pathIn, pathOut, fps, time)
