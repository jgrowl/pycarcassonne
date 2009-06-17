#!/usr/bin/env python

import side
import line.constants
import terrain

__metaclass__ = type

class Top(side.Side):
    def __init__(self, line1=line.constants.TOP_LEFT,
                 line2=line.constants.TOP_RIGHT, _terrain=terrain.Terrain()):
        super(Top, self).__init__(line1, line2, _terrain)
