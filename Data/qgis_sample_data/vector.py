#Geom
features = myVector.getFeatures(QgsFeatureRequest(3))
feature = next(features)
geom = feature.geometry()
print(geom)


print("It's length is", geom.length())
print("It's area measure", geom.area())
print("Is it multipart?", geom.isMultipart())

myVector.crs().mapUnits()