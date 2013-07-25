import os
from django.contrib.gis.gdal import DataSource


world_shp = "neigh_tuc.shp"
ds = DataSource(world_shp)

lyr = ds[0]
print lyr.geom_type

for f in lyr:
    print(f.get('NAME'), f.geom.num_points, f.geom.wkt)
