# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 20:10:17 2019

@author: raghav.aggiwal
"""

from PIL import Image
import os

input_dir = r'D:\My Folder\Dailymotion\thumbnails\new_thumbs'
output_dir = r'D:\My Folder\Dailymotion\thumbnails\new_thumbs\resized'

for file in os.listdir(input_dir):
    if os.path.splitext(file)[0] != "resized":
        
        outfile = os.path.splitext(file)[0]
        extension = os.path.splitext(file)[1]

        img = Image.open(input_dir + '\\' + file)
        current_size = img.size

        if(current_size[0] < 640 or current_size[1] <360):
            try:
                new_width = 640
                new_height = (int)(new_width*current_size[1]/current_size[0])
                
                new_size = (new_width, new_height)
                #img.thumbnail(new_size, Image.ANTIALIAS)
                img = img.resize(new_size, Image.LANCZOS)

                new_file = output_dir + '\\' + outfile + extension
                img.save(new_file)

                print("Image resized, previous size was: ", current_size, " New size: ", new_size)
            except:
                print("unable to resize image")
        else:
            print("Not required to resize image as current size is : ", current_size)
    else:
        print("Not parsed, Folder or file name is: ", os.path.splitext(file)[0])