# Python Client API for Web Services (WFS and WTSS) 

## Building and installing simple_geo.py from source
**1.** In the shell, type
```bash
  git clone https://github.com/vconrado/simple_geo.py.git
  cd simple_geo.py/src
  pip install .
```

## Using simple_geo.py

### Retrieving Features
```python
from simple_geo import simple_geo as sgeo 

# Connecting to servers
s = sgeo(wfs="http://localhost:8080/geoserver-esensing",
         wtss="http://localhost:7654")

# Retrieving the list of all available features in the service
ft_list = s.list_features()
print(ft_list)

# Retrieving the metadata of a given feature
ft_desc = s.describe_feature('esensing:municipios_bra')
print("description: ", ft_desc)

# Retrieving the collection for a given feature
fc, fc_metadata = s.feature_collection("esensing:municipios_bra")

# Retrieving a feature named 'Santa Catarina'
fc, fc_metadata = s.feature_collection("esensing:estados_bra",
                                       filter={"nome": 'Santa Catarina'}, max_features=1)

# Retrieving a feature using a polygon to filter
fc, fc_metadata = s.feature_collection("esensing:municipios_bra",
                                         spatial_filter={'intersects': fc.loc[0, 'geometry'].wkt},
                                         max_features=2,
                                         attributes=['nome', 'geom', 'estado'],
                                         sort_by={"nome": "ASC"},
                                         filter={"regiao": "S"})
print(fc)

# Retrieving collection length of selected elements for a given feature
fc_len = s.feature_collection_len("esensing:municipios_bra",
                                  spatial_filter={'within': fc.loc[0, 'geometry'].wkt,
                                                  'intersects': fc.loc[0, 'geometry'].wkt},
                                  filter={"regiao": "S"})
print(fc_len)
```

### Retrieving Coverages
```python
from simple_geo import simple_geo as sgeo

# Connecting to servers
s = sgeo(wfs="http://localhost:8080/geoserver-esensing",
         wtss="http://localhost:7654")

# Retrieving the list of all available coverages in the service
cv_list = s.list_coverages()
print(cv_list)

# Retrieving the metadata of a given coverage
cv_scheme = s.describe_coverage("climatologia")
print(cv_scheme)

# Retrieving the time series for a given location
ts, ts_metadata = s.time_series("climatologia", ("precipitation", "temperature", "humidity"), -12, -54)
print(ts)
print(ts_metadata)
```
