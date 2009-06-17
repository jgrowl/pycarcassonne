#!/usr/bin/env python

__metaclass__ = type

class Point():
    ''' Single 2-dimensional point with additional game relevant data '''
    def __init__(self, x=None, y=None):
        self.__x = x
        self.__y = y
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
        
        
