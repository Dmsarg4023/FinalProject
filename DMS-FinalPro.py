## Taking LAS Files & Conveting Them Into TIFF Files.
import datetime
import os
import glob
import arcpy
from arcpy import env
env.workspace = ()
outgdb = ()

las = glob.glob('*.las')
print(las)
for las in las:
    name = las.split('.')[0]
    
    time_string = datetime.datetime.now().isoformat()
    output_name = time_string.split('.')[0].replace(":", "_")

    las_path = r'exports\{}_{}'.format(name, output_name)
    las = arcpy.mapping.MapDocument(las)
    print(os.path.join(os.getcwd(), lasd_path))

    arcpy.CreateLasDataset_management(las, os.path.join(os.getcwd(), lasd_path))

    arcpy.mapping.LasDatasetToRaster_conversion(las, os.path.join(os.getcwd(), lasd_path))
    
    lasdesc = arcpy.Describe(lasd)
    arcpy.CopyFeatures_management(lasd, os.path.join(outgdb, lasdesc.basename))
    

    arcpy.mapping.RasterToOtherFormat_conversion(lasd, os.path.join(os.getcwd(), tif_path))
