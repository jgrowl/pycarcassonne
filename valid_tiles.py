#!/usr/bin/env python

import tile

CITY_CITY_CITY_CITY_P = Tile( \
    side.CITY, side.CITY, side.CITY, side.CITY, \
    ((tile.TOP, tile.RIGHT, tile.BOTTOM, tile.LEFT)),
    {'pennants': 1})

CITY_CITY_FIELD_CITY = Tile( \
    side.CITY, side.CITY, side.FIELD, side.CITY, \
    ((tile.TOP, tile.RIGHT, tile.LEFT)))

CITY_CITY_FIELD_CITY_P = Tile( \
    side.CITY, side.CITY, side.CITY, side.CITY, \
    ((tile.TOP, tile.RIGHT, tile.LEFT)),
    {'pennants': 1})

CITY_CITY_ROAD_CITY = Tile( \
    side.CITY, side.CITY, side.ROAD, side.CITY, \
    ((tile.TOP, tile.RIGHT, tile.LEFT)))

CITY_CITY_ROAD_CITY_P = Tile( \
    side.CITY, side.CITY, side.ROAD, side.CITY, \
    ((tile.TOP, tile.RIGHT, tile.LEFT)),
    {'pennants': 1})

FIELD_CITY_FIELD_CITY = Tile( \
    side.FIELD, side.CITY, side.FIELD, side.CITY, \
    ((tile.RIGHT, tile.LEFT)))

FIELD_CITY_FIELD_CITY_P = Tile( \
    side.FIELD, side.CITY, side.FIELD, side.CITY, \
    ((tile.RIGHT, tile.LEFT)), \
    {'pennants': 1})

CITY_FIELD_FIELD_CITY = Tile( \
    side.CITY, side.FIELD, side.FIELD, side.CITY,
    ((tile.TOP, tile.LEFT), (tile.RIGHT, tile.BOTTOM)))

CITY_FIELD_FIELD_CITY_P = TILE( \
    side.CITY, side.FIELD, side.FIELD, side.CITY, \
    ((tile.TOP, tile.LEFT), (tile.RIGHT, tile.BOTTOM)), \
    {'pennants': 1})

CITY_ROAD_ROAD_CITY = TILE( \
    side.CITY, side.ROAD, side.ROAD, side.CITY, \
    ((tile.TOP, tile.LEFT), (tile.RIGHT, tile.BOTTOM)))
    
CITY_ROAD_ROAD_CITY_P = TILE( \
    side.CITY, side.ROAD, side.ROAD, side.CITY, \
    ((tile.TOP, tile.LEFT), (tile.RIGHT, tile.BOTTOM)), \
    {'pennants': 1})

CITY_CITY_FIELD_FIELD = TILE( \
    side.CITY, side.CITY, side.FIELD, side.FIELD, \
    ((tile.BOTTOM, tile.LEFT)))

FIELD_CITY_FIELD_CITY = TILE( \
    side.FIELD, side.CITY, side.FIELD, side.CITY, \
    ((tile.TOP, tile.BOTTOM)))

CITY_FIELD_FIELD_FIELD = TILE( \
    side.CITY, side.FIELD, side.FIELD, side.FIELD, \
    ((tile.RIGHT, tile.BOTTOM, tile.LEFT)))

CITY_ROAD_ROAD_FIELD = TILE( \
    side.CITY, side.ROAD, side.ROAD, side.FIELD, \
    ((tile.RIGHT, tile.BOTTOM)))

CITY_FIELD_ROAD_ROAD = TILE( \
    side.CITY, side.FIELD, side.ROAD, side.ROAD, \
    ((tile.BOTTOM, tile.LEFT)))

CITY_ROAD_ROAD_ROAD = TILE( \
    side.CITY, side.ROAD, side.ROAD, side.ROAD, \
    ((tile.RIGHT, tile.MIDDLE), (tile.BOTTOM, tile.MIDDLE), \
    (tile.LEFT, tile.MIDDLE)))

CITY_ROAD_FIELD_ROAD = TILE( \
    side.CITY, side.ROAD, side.FIELD, side.ROAD, \
    ((tile.RIGHT, tile.LEFT)))

FIELD_FIELD_ROAD_FIELD = Tile( \
    side.FIELD, side.FIELD, side.ROAD, side.FIELD, \
    ((tile.BOTTOM, tile.MIDDLE)), \
    {'cloister': True})

FIELD_FIELD_FIELD_FIELD = Tile( \
    side.FIELD, side.FIELD, side.FIELD, side.FIELD, \
    ((tile.TOP, tile.RIGHT, tile.BOTTOM, tile.LEFT)), \
    {'cloister': True})

FIELD_FIELD_ROAD_ROAD = Tile( \
    side.FIELD, side.FIELD, side.ROAD, side.ROAD, \
    ((tile.TOP, tile.RIGHT), (tile.BOTTOM, tile.LEFT)))

ROAD_FIELD_ROAD_FIELD = Tile( \
    side.ROAD, side.FIELD, side.ROAD, side.FIELD, \
    ((tile.TOP, tile.BOTTOM)))

FIELD_ROAD_ROAD_ROAD = Tile( \
    side.FIELD, side.ROAD, side.ROAD, side.ROAD, \
    ((tile.RIGHT, tile.MIDDLE), (tile.BOTTOM, tile.MIDDLE), \
    (tile.RIGHT, tile.MIDDLE)))

ROAD_ROAD_ROAD_ROAD = Tile( \
    side.ROAD, side.ROAD, side.ROAD, side.ROAD, \
    ((tile.TOP, tile.MIDDLE), (tile.RIGHT, tile.MIDDLE), (tile.BOTTOM, tile.MIDDLE), \
    (tile.RIGHT, tile.MIDDLE)))

