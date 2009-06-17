#!/usr/bin/env python

import side
from side import terrain

__metaclass__ = type

class Tile():
    ''' Holds information about a tiles state.  This includes the values of its
    sides, connections '''
    def __init__(self, top=terrain.Terrain(), right=terrain.Terrain(),
                 bottom=terrain.Terrain(), left=terrain.Terrain(),
                 connections=None):
        
        ''' Each side has a terrain '''
        self.top = side.Top(top)
        self.right = side.Right(right)
        self.bottom = side.Bottom(bottom)
        self.left = side.Left(left)
        
        self.connections = connections
        
