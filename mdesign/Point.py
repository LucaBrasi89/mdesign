#!/bin/bash python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:29:11 2019

@author: andrew
"""



class Point:

    _x = 0
    _y = 0    

    def __init__(self, x, y):

        self._x = x
        self._y = y


    def __str__(self):
        return 'x: {}, y: {}'.format(self._x, self._y)








        

    
    