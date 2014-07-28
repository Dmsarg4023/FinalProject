## This program will take multiple .las files and 
#   convert them to one .dem then to one Geo .tif file

import arcpy
import os
from arcpy import env
arcpy.CheckOutExtension('3D')
env.workspace = 'C:/data'
arcpy.LasDatasetToRaster_3d
