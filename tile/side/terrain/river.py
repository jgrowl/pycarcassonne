#!/usr/bin/env python

import terrain

__metaclass__ = type

class River(terrain.Terrain):
    def __init__(self, pennants=0):
        self.pennants = pennants