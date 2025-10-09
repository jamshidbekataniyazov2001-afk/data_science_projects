# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 13:57:33 2025

@author: user
"""

import numpy as np
def boolean_slicing():
  names =  ['Hasan', 'Husan', 'Javohir', 'Elyor', 'Hasan', 'Javohir', 'Elyor']
  arr4 = np.array( [[5, 6, 1, 1],
   [9, 1, 1, 1],
   [7, 7, 4, 2],
   [1, 5, 1, 9],
   [9, 9, 4, 5],
   [7, 5, 9, 6],
   [5, 3, 7, 4]])
  mask = (np.array(names) == 'Javohir') | (np.array(names) == 'Elyor')
  return arr4[mask]
boolean_slicing()