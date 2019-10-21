#!/bin/bash python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:29:11 2019

@author: andrew
"""

class Line:

    _p1 = []
    _p2 = []


    def __init__(self, p1, p2):

        self._p1 = p1
        self._p2 = p2


    def getLinearSystem(self):
        A = (self._p1[1] - self._p2[1])
        B = (self._p2[0] - self._p1[0])
        C = (self._p1[0]*self._p2[1] - self._p2[0]*self._p1[1])

        return A, B, -C







        

    
    