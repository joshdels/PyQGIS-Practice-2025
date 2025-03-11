# Data loaded
myVector = QgsVectorLayer("J:/1. PROJECT/qgis_sample_data/shapefiles/alaska.shp","MyFirstVector", "ogr")
# QgsProject.instance().addMapLayer(myVector)

header = myVector.fields()
print("How many columns?", header.count())
print("does the column 4 exits?", header.exists(4))
print("Column 0 has name", header[0].name())
for column in header:
    print("name", column.name())
    print("type", column.typeName())
    print("precision", column.precision())

