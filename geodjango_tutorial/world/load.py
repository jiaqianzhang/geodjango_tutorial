from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import WorldBorder

# using LayerMapping in python script
# each key in world_mapping corresponds to a field in WorldBorder model
# the value is the name of the shapefile field that data will be loaded from
# the path to the shapefile is not absolute so if you move the world application with data subdir to a different location the script will still work
world_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'mpoly' : 'MULTIPOLYGON', # the key mpoly, the geometry type GeoDjango will import the field as, even simple polygons in the shapefile will automatically be converted in collections prior to the insertion into the db
}
 
world_shp = Path(__file__).resolve().parent / 'data' /'TM_WORLD_BORDERS-0.3.shp'

# the transform keyword is set to false because the data in the shapefile doesn't need to be converted (WGS84)
def run(verbose=True):
    lm = LayerMapping(WorldBorder, world_shp, world_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)