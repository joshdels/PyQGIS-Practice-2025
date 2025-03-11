myPoint = QgsGeometry.fromWkt('POINT(-195935.165 766139000.585')
newPoint = QgsPointXY(-195935.165,  766139000.585)
myPoint = QgsGeometry.fromPointXY(newPoint)

QgsProject.instance().addMapLayer(myPoint)