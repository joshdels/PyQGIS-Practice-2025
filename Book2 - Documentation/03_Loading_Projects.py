# Creating an Instance
from qgis.core import QgsProject
project = QgsProject.instance()

# project data
project.read('testdata/01_project.qgs')
print(project.fileName())

# modifications
project.write()
project.write('testdata/my_new_qgis_project.qgs')