#adding a feature

# get data Provider
myDataProvider = myVector.dataProvider()

#get feature id 599
features = myVector.getFeatures(QgsFeatureRequest(599))
myFeature = next(features)

# create geometry bounding box
bbox = myFeature.geometry().boundingBox()
newGeom = QgsGeometry.fromRect(bbox)

# Create new feature
newFeature = QgsFeature()
newFeature.setFields(myVector.fields())

# Set ANew Attributes 
newAttributes = [1000, "Alaska", 2]
newFeature.setAttributes(newAttributes)

# set the geometry of the new feature
newFeature.setGeometry(newGeom)

# add new feature in myVector using the provider
myDataProvider.addFeatures([newFeature])
