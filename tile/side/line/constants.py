#!/usr/bin/env python

import point.constants

import line

TOP_LEFT = line.Line(point.constants.TOP_LEFT, point.constants.TOP_MIDDLE)
TOP_RIGHT = line.Line(point.constants.TOP_MIDDLE, point.constants.TOP_RIGHT)

MIDDLE_LEFT = line.Line(point.constants.MIDDLE_LEFT,
                        point.constants.MIDDLE_MIDDLE)
MIDDLE_RIGHT = line.Line(point.constants.MIDDLE_MIDDLE,
                         point.constants.MIDDLE_RIGHT)

BOTTOM_LEFT = line.Line(point.constants.BOTTOM_LEFT,
                        point.constants.BOTTOM_MIDDLE)
BOTTOM_RIGHT = line.Line(point.constants.BOTTOM_LEFT,
                         point.constants.BOTTOM_RIGHT)
