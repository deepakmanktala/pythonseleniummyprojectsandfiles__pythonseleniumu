import os
import easyocr
import cv2
# from matplotlib import pyplot as plt
import numpy as np

import os

png = []

files = os.listdir('C:\personal\Deepaks\pythonseleniummyprojectsandfiles__pythonseleniumu\Fundamentals of Big Data')


# for root, dirs, files in os.walk(r'C:\personal\Deepaks\pythonseleniummyprojectsandfiles__pythonseleniumu\Fundamentals of Big Data'):
#     for file in files:
#         if file.endswith('.png'):
#             png.append(file)

# for i in files:
#     if i is like '*.png':
#         print (i)


for i in files:
    if i.endswith(".png"):
        file_object = open('Fundmentals_Big_Data_Slides.txt', 'a')
        IMAGE_PATH = i
        reader = easyocr.Reader(['en'])
        result = reader.readtext(IMAGE_PATH,paragraph="False")
        file_object.write('------------ /n /n --------$$$$$-------------- ' + str(result))
        file_object.close()

        # print(result)