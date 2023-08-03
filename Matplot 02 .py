#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 23:15:01 2023

@author: nahidferdous
"""
# Line plot and its two different drawstyle 
from numpy.random import randn as rn
import matplotlib.pyplot as plt


data= rn(30).cumsum()
plt.plot(data, 'k--', label='Default')
plt.plot(data, 'k--',drawstyle='steps-post', label='steps-post')
plt.legend(loc='best')
