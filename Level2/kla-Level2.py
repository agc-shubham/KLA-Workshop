# -*- coding: utf-8 -*-
"""KLA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a_aIwr7i8VDTuqMAFt5WWiacQSnR-9Pc
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json 

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [1,1,1])

 
f = open('input.json',) 
  
# returns JSON object as  
# a dictionary 
input = json.load(f) 
  
# Closing file 
f.close() 

datapath = 'wafer_image_'
images = []
count = 1
noImg = input['die']['columns']*input['die']['rows']
for i in range(noImg):
  images.append(plt.imread(datapath+str(count)+'.png'))
  count += 1

imageGray = []
for i in range(noImg):
  imageGray.append(rgb2gray(images[i]))
  


data = []
# # print(img1.shape)
# print(len(input['care_areas']))
for k in range(noImg):
  for l in range(len(input['care_areas'])):
    for i in range(input['die']['height']-1-input['care_areas'][l]['top_left']['y'],input['die']['height']-input['care_areas'][l]['bottom_right']['y']):
      for j in range(input['care_areas'][l]['top_left']['x'],input['care_areas'][l]['bottom_right']['x']+1):
        row = []
        if(imageGray[k][i][j] - imageGray[(k+1) % noImg][i][j] != 0 and imageGray[k][i][j] - imageGray[(k+2) % noImg][i][j] != 0 ):
          row.append(k+1)
          row.append(j)
          row.append(input['die']['height']-i-1)
          data.append(row)

for k in range(noImg):
  for l in range(len(input['exclusion_zones'])):
    for i in range(input['die']['height']-1-input['exclusion_zones'][l]['top_left']['y'],input['die']['height']-input['exclusion_zones'][l]['bottom_right']['y']):
      for j in range(input['exclusion_zones'][l]['top_left']['x'],input['exclusion_zones'][l]['bottom_right']['x']+1):
        row = [k+1,j,input['die']['height']-i-1]
        if row in data:
          data.remove(row)

print(data)

# for i in range(input['die']['height']):
#   for j in range(input['die']['width']):
#     row = []
#     if(imggray1[i][j] - imggray2[i][j] != 0 and imggray1[i][j] - imggray3[i][j] != 0 ):
#       row.append(1)
#       row.append(j)
#       row.append(input['die']['height']-i-1)
#       data.append(row)
# for i in range(input['die']['height']):
#   for j in range(input['die']['width']):
#     row = []
#     if(imggray2[i][j] - imggray3[i][j] != 0 and imggray2[i][j] - imggray4[i][j] != 0  ):
#       row.append(2)
#       row.append(j)
#       row.append(input['die']['height']-i-1)
#       data.append(row)
# for i in range(input['die']['height']):
#   for j in range(input['die']['width']):
#     row = []
#     if(imggray3[i][j] - imggray4[i][j] != 0 and  imggray3[i][j] - imggray5[i][j] != 0 ):
#       row.append(3)
#       # row.append(input['die']['height']-i-1)
#       row.append(j)
#       row.append(input['die']['height']-i-1)
#       data.append(row)
# for i in range(input['die']['height']):
#   for j in range(input['die']['width']):
#     row = []
#     if(imggray4[i][j] - imggray5[i][j] != 0  and imggray4[i][j] - imggray1[i][j] != 0 ):
#       row.append(4)
#       # row.append(input['die']['height']-i-1)
#       row.append(j)
#       row.append(input['die']['height']-i-1)
#       data.append(row)
# for i in range(input['die']['height']):
#   for j in range(input['die']['width']):
#     row = []
#     if(imggray5[i][j] - imggray1[i][j] != 0 and imggray5[i][j] - imggray2[i][j] != 0 ):
#       row.append(5)
#       # row.append(input['die']['height']-i-1)
#       row.append(j)
#       row.append(input['die']['height']-i-1)
#       data.append(row)
# print(data)    

df = pd.DataFrame(data)      
# df
df.to_csv('output_2.csv',index=False)
# # for i in range(600):
# #   for j in range(800):
# #     print(imggray1[i][j])