#########################################################################################################################################################
#-------------------------------------------------------------------------------------------------------------------------------------------------------#
'''
 NAME:          SnapExtractMask
 PURPOSE:       Extracts by mask using mask feature and snaps to raster layer to align

 DATE:          December 12, 2018

 AUTHOR:        Cole Fields
                Spatial Analyst
                Marine Spatial Ecosystem Analysis (MSEA)
                Fisheries and Oceans Canada
'''
#-------------------------------------------------------------------------------------------------------------------------------------------------------#

#########################################################################################################################################################
# IMPORT MODULES
#########################################################################################################################################################

#-------------------------------------------------------------------------------------------------------------------------------------------------------#

# Import system modules
import os
import sys
import arcpy
from arcpy import env

# Check out the ArcGIS Spatial Analyst extension license
arcpy.CheckOutExtension("Spatial")

#-------------------------------------------------------------------------------------------------------------------------------------------------------#

#########################################################################################################################################################
# USAGE STRING FOR COMMAND PROMPT
#########################################################################################################################################################

#-------------------------------------------------------------------------------------------------------------------------------------------------------#

# Usage string
usage = "<mask feature> <raster to snap to> <working directory> <output directory>"
usageExample = "python SnapExtractMask.py D:/Projects/SOG.shp D:/Projects/SOG_bathy.tif D:/Projects/Rasters D:/Projects/Output"

if len(sys.argv) < 4:
	raise Exception, "Invalid number of parameters provided. \n\n" + "Usage: " + usage + "\n\nExample: " + usageExample

#-------------------------------------------------------------------------------------------------------------------------------------------------------#

#########################################################################################################################################################
# FUNCTION(S)
#########################################################################################################################################################

#-------------------------------------------------------------------------------------------------------------------------------------------------------#

####################################################################################
## EXTRACT BY MASK USING SNAP ENVIRONMENT SO RASTERS ARE ALIGNED
####################################################################################
def snapExtract(maskFeature, snapRaster, workingDir, outDir):
    # set extent
    extentObj = arcpy.Describe(maskFeature)
    ext = extentObj.extent
    # Set Snap Raster environment
    arcpy.env.snapRaster = snapRaster
    # set workspace to working directory
    env.workspace = workingDir
    # make list rasters in workspace
    rasters = arcpy.ListRasters()
    # set counter
    counter = 1
    # loop through rasters and extract by mask (will be aligned because of the snap environment)
    for i in rasters:
        print('Working on file {} of {}\n'.format(counter, len(rasters)))
        # output file
        outPath = os.path.join(outDir, i)
        # Process: Extract by Mask
        print('Masking {} with {}\nSnapping to: {}\nExporting to: {}\n\n'.format(i, maskFeature, snapRaster, outDir))
        arcpy.gp.ExtractByMask_sa(i, maskFeature, outPath)
        # increment counter
        counter += 1



#-------------------------------------------------------------------------------------------------------------------------------------------------------#

#########################################################################################################################################################
# PARAMETERS
#########################################################################################################################################################

#-------------------------------------------------------------------------------------------------------------------------------------------------------#

mask = arcpy.GetParameterAsText(0)
snap = arcpy.GetParameterAsText(1)
workDirectory = arcpy.GetParameterAsText(2)
outDirectory = arcpy.GetParameterAsText(3)


#-------------------------------------------------------------------------------------------------------------------------------------------------------#

#########################################################################################################################################################
# CALL FUNCTION W/PARAMETERS
#########################################################################################################################################################

#-------------------------------------------------------------------------------------------------------------------------------------------------------#

snapExtract(mask, snap, workDirectory, outDirectory)

