#!/usr/bin/env python

import line
import terrain

__metaclass__ = type

class Side():
    def __init__(self, _line1=line.Line(), _line2=line.Line(),
                 _terrain=terrain.Terrain()):
        self.__terrain = _terrain
        self.__line1 = _line1
        self.__line2 = _line2
        
    def getTerrain(self):
        return self.__terrain
        
    def getLine1(self):
        return self.__line1
        
    def getLine2(self):
        return self.__line2
        
    line1 = property(getLine1)
    line2 = property(getLine2)
        
    # The middle point of a side
    #middle = property(getLine1.getPoint2)
