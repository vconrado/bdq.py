# -*- coding: utf-8 -*-
import sys

# to use local version of simple_geo
sys.path.insert(0, '../src/simple_geo')

from simple_geo import simple_geo as sgeo
from osgeo import ogr

######################################################################################################################
# simple_geo Features

s = sgeo(wfs="http://localhost:8080/geoserver-esensing", wtss="http://localhost:7644", debug=True, cache=True)

print("Features")

# Retrieving the list of all available features in the service
# ft_list = s.list_features()
# print(ft_list)

ft_desc = s.describe_feature('esensing:municipios_bra')
print("description: ", ft_desc)

ft_desc = s.describe_feature('esensing:focos_bra_2016')
print("description: ", ft_desc)

fc, fc_metadata = s.feature_collection("esensing:estados_bra",
                                       filter={"nome": 'Santa Catarina'}, max_features=1)

print("metadata: ", fc_metadata)
print(fc)

fc2, fc2_metadata = s.feature_collection("esensing:municipios_bra",
                                         spatial_filter={'within': fc.loc[0, 'geometry'].wkt,
                                                         'intersects': fc.loc[0, 'geometry'].wkt},
                                         max_features=2,
                                         attributes=['nome', 'geom', 'estado'],
                                         sort_by={"nome": "DESC"},  # 'nome', ['nome', 'estado']
                                         filter={
                                             "regiao": "S"})  # [SGEO.EQ("regiao","S"), SGEO.LT("idade",10), SGEO.OR(SGEO.EQ("regiao","S"), SGEO.EQ("regiao", "NE"))]?

print("metadata: ", fc2_metadata)
print(fc2)

# fc_len = s.feature_collection_len("esensing:municipios_bra",
#                                   spatial_filter={'within': fc.loc[0, 'geometry'].wkt,
#                                                   'intersects': fc.loc[0, 'geometry'].wkt},
#                                   filter={"regiao": "S"})
#
# print('fc_len', fc_len)
