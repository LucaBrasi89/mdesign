#!/bin/bash python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:29:11 2019

@author: andrew
"""



class PointSet:

    _pointSet = []

    def __init__(self):

        pass

    def putPoint(self, point):

        self._pointSet.append(point)


    def calcEverage(self):

        pass

    
    def reset(self):

        self._pointSet = []


    def display(self):

        for point in self._pointSet:

            print(point)


    def getAllPoint(self):

        i = 1
        for point in self._pointSet:
            print(i, point)
            i = i + 1

    







        

    
    