#!/usr/bin/env python

import side
import line.constants
import terrain

__metaclass__ = type

class Right(side.Side):
    def __init__(self, line1=line.constants.TOP_RIGHT,
                 line2=line.constants.MIDDLE_RIGHT, _terrain=terrain.Terrain()):
        super(Right, self).__init__(line1, line2, _terrain)
