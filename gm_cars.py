# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 22:23:47 2025

@author: user
"""

import numpy as np
arr1 = np.load('gm_2020.npz')
arr2 = np.load('gm_2021.npz')
data1 =  arr1['models']
data2 = arr1['qnts']
data3 = arr2['models']
data4 = arr2['qnts']
mask= (data3== 'Damas') | (data3 == 'Nexia')| (data3 == 'Cobalt')| (data3 == 'Gentra') 
