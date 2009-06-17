#!/usr/bin/env python

import side
import line.constants
import terrain

__metaclass__ = type

class Bottom(side.Side):
    def __init__(self, line1=line.constants.BOTTOM_LEFT,
                 line2=line.constants.BOTTOM_RIGHT, _terrain=terrain.Terrain()):
        super(Bottom, self).__init__(line1, line2, _terrain)
