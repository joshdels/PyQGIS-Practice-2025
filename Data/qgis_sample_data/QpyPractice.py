# myRaster = QgsRasterLayer("J:/1. PROJECT/qgis_sample_data/raster/landcover.img")
# QgsProject.instance().addMapLayer(myRaster)

myVector = QgsVectorLayer("J:/1. PROJECT/qgis_sample_data/shapefiles/alaska.shp","MyFirstVector", "ogr")
QgsProject.instance().addMapLayer(myVector)

print(myVector.extent().toString())
myVector.featureCount()
myVector.capabilitiesString()

header = myVector.fields()
header = myVector.fields()
field_0 = header[0]
for column in header: 
