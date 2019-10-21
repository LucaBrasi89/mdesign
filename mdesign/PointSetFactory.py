#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:29:11 2019

@author: andrew
"""
from mdesign.Point import *
from mdesign.PointSet import *


class PointSetFactory:

    @staticmethod    
    def findPosPointSets(df, treshold):

        pointSets = []

        
        # xValues = [] #getting stack of xValues
        # yValues = [] #getting stack of yValues
        for i in range(len(df)):
            #calc Rectangle dimensions
            pointSet = PointSet()
            if df['y_val'][i] >= treshold:
                #getting first point beyond treshold
                
                point = Point(df['x_val'][i], df['y_val'][i])
                pointSet.putPoint(point)
        
                #last point have been found
                if df['y_val'][i+1] <= treshold:
                    pointSets.append(pointSet)                    
                    pointSet.reset()
                
            

        return pointSets


""" 
    @staticmethod    
    def findNegativeRectangles(df, treshold):

        rectangles = []
        xValues = [] #getting stack of xValues
        yValues = [] #getting stack of yValues
        for i in range(len(df)):

            
            #calc Rectangle dimensions
            if df['y_val'][i] <= treshold:
                #getting start point
                
                xValues.append(df['x_val'][i])
                yValues.append(df['y_val'][i])
                
                if df['y_val'][i+1] >= treshold:

                    x1 = min(xValues)
                    y1 = min(yValues)
                    #for high precision, we take next point after current...
                    x4 = df['x_val'][i+1]
                    y4 = df['y_val'][i+1]
                    startPoint = (x1, y1)
                    length = x4 - x1
                    height = max(yValues) - y1

                    rectangles.append(Rectangle(startPoint, length, height))

                    xValues.clear()
                    yValues.clear()

        return rectangles
 """















        

    
    
