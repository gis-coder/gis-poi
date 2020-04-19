#!/usr/bin/env python3.7
# -*- coding:utf-8 -*-


from osgeo import gdal
from osgeo import ogr
import osr

# 栅格数据投影转换
from osgeo import gdal, osr
from osgeo.gdalconst import *

# 源图像投影
source = osr.SpatialReference()
source.ImportFromEPSG(32650)
# 目标图像投影
target = osr.SpatialReference()
target.ImportFromEPSG(3857)
coordTrans = osr.CoordinateTransformation(source, target)
# 打开源图像文件
ds = gdal.Open("fdem.tif")
# 仿射矩阵六参数
mat = ds.GetGeoTransform()
# 源图像的左上角与右下角像素，在目标图像中的坐标
(ulx, uly, ulz) = coordTrans.TransformPoint(mat[0], mat[3])
(lrx, lry, lrz) = coordTrans.TransformPoint(mat[0] + mat[1] * ds.RasterXSize, mat[3] + mat[5] * ds.RasterYSize)
# 创建目标图像文件（空白图像），行列数、波段数以及数值类型仍等同原图像
driver = gdal.GetDriverByName("GTiff")
ts = driver.Create("fdem_lonlat.tif", ds.RasterXSize, ds.RasterYSize, 1, GDT_UInt16)
# 转换后图像的分辨率
resolution = (int)((lrx - ulx) / ds.RasterXSize)
# 转换后图像的六个放射变换参数
mat2 = [ulx, resolution, 0, uly, 0, -resolution]
ts.SetGeoTransform(mat2)
ts.SetProjection(target.ExportToWkt())
# 投影转换后需要做重采样
gdal.ReprojectImage(ds, ts, source.ExportToWkt(), target.ExportToWkt(), gdal.GRA_Bilinear)
# 关闭
ds = None
ts = None
