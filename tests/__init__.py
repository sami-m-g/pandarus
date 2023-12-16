"""Test suite for the __pandarus__ package."""
import os

PATH_DATA: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))
PATH_CFS = os.path.join(PATH_DATA, "raster_cfs_32bit.tif")
PATH_DEM: str = os.path.join(PATH_DATA, "DEM.tif")
PATH_DUPLICATES: str = os.path.join(PATH_DATA, "duplicates.geojson")
PATH_COUNTRIES: str = os.path.join(PATH_DATA, "test_countries.gpkg")
PATH_GC = os.path.join(PATH_DATA, "gc.geojson")
PATH_GRID: str = os.path.join(PATH_DATA, "grid.geojson")
PATH_GRID_INTS: str = os.path.join(PATH_DATA, "grid-ints.geojson")
PATH_GRID_PROJ: str = os.path.join(PATH_DATA, "grid-3410.geojson")
PATH_INTER_RES = os.path.join(PATH_DATA, "intersection_result.geojson")
PATH_INTER_RES_DECOMP = os.path.join(PATH_DATA, "i_result.json")
PATH_INTER_RES_MD = os.path.join(PATH_DATA, "intersection_result.json.bz2")
PATH_INVALID = os.path.join(PATH_DATA, "invalid.txt")
PATH_LINES: str = os.path.join(PATH_DATA, "lines.geojson")
PATH_LINES_PROJ: str = os.path.join(PATH_DATA, "lines-25000.geojson")
PATH_OUTSIDE: str = os.path.join(PATH_DATA, "outside.geojson")
PATH_POINT = os.path.join(PATH_DATA, "point.geojson")
PATH_POINTS: str = os.path.join(PATH_DATA, "points.geojson")
PATH_POINTS_PROJ: str = os.path.join(PATH_DATA, "points-32631.geojson")
PATH_RANGE_RASTER: str = os.path.join(PATH_DATA, "range.tif")
PATH_RASTER: str = os.path.join(PATH_DATA, "test_raster_cfs.tif")
PATH_REMAIN_RESULT: str = os.path.join(PATH_DATA, "remaining.geojson")
PATH_SIXTY_FOUR = os.path.join(PATH_DATA, "test_raster_cfs.tif")
PATH_SQUARE: str = os.path.join(PATH_DATA, "square.geojson")
PATH_SQUARE_PROJ: str = os.path.join(PATH_DATA, "square-3857.geojson")
