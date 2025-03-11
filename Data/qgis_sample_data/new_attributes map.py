#changing features

columnIndex = myVector.fields().indexFromName("NAME")
columnIndex2 = myVector.fields().indexFromName("AREA_MI")

newColumnValueMap = {columnIndex: 12352, columnIndex2: 123412341234}
newAttributesValuesMap = {myFeature.id(): newColumnValueMap}
myDataProvider.changeAttributeValues(newAttributesValuesMap)