# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 20:29:09 2021

@author: zjy
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlrd

x = [2,4,7]
y = [3,7,6]
plt.xlim((0, 10))
plt.ylim((0, 10))
ax=plt.gca()
ax.spines['right'].set_color('none') #只保留一条纵坐标轴，形成象限图
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.plot(x, y, marker = 'o', color='red' )