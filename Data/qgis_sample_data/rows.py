# Data loaded
myVector = QgsVectorLayer("J:/1. PROJECT/qgis_sample_data/shapefiles/alaska.shp","MyFirstVector", "ogr")
# QgsProject.instance().addMapLayer(myVector)

features = myVector.getFeatures(QgsFeatureRequest(3))
feature = next(features)

print(feature.attributes())
geom = feature.geometry()
print(geom)
