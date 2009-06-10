#!/usr/bin/env python

import side

__metaclass__ = type

# Define constants to be used for connections in Tile class
TOP = 1
RIGHT = 2
BOTTOM = 3
LEFT = 4
MIDDLE = 0

class Tile(self):
    ''' Holds information about a tiles state.  This includes the values of its
    sides, connections, and special attributes '''
    def __init__(self, top=None, right=none, bottom=None, left=None, \
                 connections=None, attributes=None):
        ''' Sides should be initialized to a valid side type.  Will be
        initialized to None type if not specified '''
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        
        # All connections in a tile are represented as a tuple of tuples
        self.connections = connections
        
        # Tile attributes such as cloisters and penants are represented
        # as a dictionary
        self.attributes = attributes
    
