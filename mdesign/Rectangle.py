#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:29:11 2019

@author: andrew
"""

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

class Rectangle:

    _startPoint = (0, 0)
    _length = 0
    _height = 0
    _rectangle = None

    def __init__(self, startPoint, length, height):

        self._startPoint = startPoint
        self._length = length
        self._height = height
        self._doRectangle()




    def containsPoints(self, points):

        pointsInside = []
        for point in points:
            if (self._rectangle.contains(point)):
                pointsInside.append(point.coords[:])

        return pointsInside



    def _doRectangle(self):

    #calc points

    #   p2         p3
    #    *---------*
    #    |         |
    #    |         |
    #    |         |
    #    |         |
    #    *---------*
    #   p1         p4
    
        x1 = self._startPoint[0]
        y1 = self._startPoint[1]
        p1 = Point(x1, y1)
        
        x2 = self._startPoint[0]
        y2 = self._startPoint[1] + self._height
        p2 = Point(x2, y2)


        x3 = self._startPoint[0] + self._length
        y3 = y2
        p3 = Point(x3, y3)

        x4 = x3
        y4 = y1
        p4 = Point(x4, y4)

        self._rectangle = Polygon([(x1,y1), (x2,y2), (x3,y3), (x4,y4)])
            

    def __str__(self):

        return '''Start point: {} Length: {} Height: {}\n'''.format(
            self._startPoint, self._length, self._height
        )







        

    
    