import arcpy

fc="D:/����/806451852609_csv ���¼�.shp"
shp=arcpy.SearchCursor(fc)

desc = arcpy.Describe(fc)



for row in shp:


    pnt = row.getValue(arcpy.Describe(fc).ShapeFieldName).getPart()
    if pnt.X>118.8:
        if pnt.X<118.82:
            print "Piont " + str(row.getValue(desc.OIDFieldName)) + ":"
            print pnt.X,pnt.Y

