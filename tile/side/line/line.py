#!/usr/bin/env python

import point

class Line():
    ''' A line in 2-dimensional space '''
    def __init__(self, point1=point.Point(), point2=point.Point()):
        self.__point1 = point1
        self.__point2 = point2

    def getPoint1(self):
        return self.__point1
    
    def getPoint2(self):
        return self.__point2