# iface.mapCanvas().clearCache()
# iface.mapCanvas().refresh()

# iface.layerTreeView().refreshLayerSymbology(myVector.id())

# myVector = QgsVectorLayer("J:/1. PROJECT/qgis_sample_data/shapefiles/alaska.shp",
# "MyFirstVector", "ogr")
# QgsProject.instance().addMapLayer(myVector)
# myDataProvider = myVector.dataProvider()
# print(myDataProvider)

# changing features
features = myVector.getFeatures(QgsFeatureRequest(599))
myFeature = next(features)

oldGeom = myFeature.geometry()
bbox = oldGeom.boundingBox()
newGeom = QgsGeometry.fromRect(bbox)
newGeomMap = {myFeature.id(): newGeom}
myDataProvider.changeGeometryValues(newGeomMap)