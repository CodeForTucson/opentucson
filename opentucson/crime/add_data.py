import os
from django.contrib.gis.utils.layermapping import LayerMapping
from models import Neighborhood


neighborhood_mapping = {
    'name' : 'NAME',
    'ward' : 'WARD',
    'geom' : 'MULTIPOLYGON',
}

world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/neigh_tuc.shp'))

def run(verbose=True):
    lm = LayerMapping(
        Neighborhood,
        world_shp,
        neighborhood_mapping,
        transform=False
    )

    lm.save(strict=True, verbose=verbose)


if __name__ == '__main__':
    run()
