#!/usr/bin/env python3.7
# -*- coding:utf-8 -*-


from osgeo import gdal
from osgeo import ogr

# 矢量文件支持中文
gdal.SetConfigOption('GDAL_FILENAME_IS_UTF8', 'YES')
# 矢量文件属性表支持中文
gdal.SetConfigOption('SHAPE_ENCODING', 'GBK')

ogr.RegisterAll()


# 矢量文件的驱动类型
# driver = ogr.GetDriverByName('ESRI ShapeFile')


class ShapeRead():
    def __init__(self, path):
        self.path = path
        # 矢量文件空间信息
        self.spatial = None
        # 矢量文件类型
        self.geoType = None
        # 矢量文件字段数量
        self.fieldCount = 0

        # 私有化对象驱动
        # 矢量文件驱动
        self.__driver = None
        # 矢量文件数据源
        self.__dataSource = None
        # 矢量文件图层对象
        self.__layer = None
        # 矢量文件定义
        self.__definition = None

        self.__getShpInfo()

    # 读取矢量文件定义
    def __getShpInfo(self):
        try:
            self.__getObject()

            self.spatial = self.__layer.GetSpatialRef()

            # 读取矢量文件空间信息
            self.__definition = self.__layer.GetLayerDefn()
            if self.__definition is None:
                raise Exception('打开矢量文件定义失败')

            self.fieldCount = self.__definition.GetFieldCount()
            # 读取图层集合类型，返回值为数字'''
            # 1:点， 2：线， 3：面'''
            type_num = self.__layer.GetGeomType()
            if type_num == 1:
                self.geoType = 'Point'
            elif type_num == 2:
                self.geoType = 'Polyline'
            elif type_num == 3:
                self.geoType = 'Polygon'
            else:
                raise Exception('不支持此类型数据的读取')
        except Exception as e:
            print(e)
        finally:
            self.__close()

    def __getObject(self):
        try:
            # 读取矢量空间信息驱动
            self.__driver = ogr.GetDriverByName("ESRI Shapefile")
            # 打开矢量文件数据源
            self.__dataSource = self.__driver.Open(self.path)
            if self.__dataSource is None:
                raise Exception('打开矢量文件数据源失败')
            # 新建矢量文件
            # self.__dataSource = self.__driver.CreateDataSource(self.path)
            # self.__layer = self.__dataSource.CreateLayer("layerName",None,ogr.wkbPolygon,)

            # 打开矢量文件图层
            self.__layer = self.__dataSource.GetLayerByIndex(0)

            # 读取矢量文件投影信息
            if self.__layer is None:
                raise Exception('读取矢量文件的空间信息失败')

        except Exception as e:
            print(e)

    # 读取矢量文件字段信息
    def read_field(self):
        try:
            self.__getObject();

            # 读取矢量文件空间信息
            self.__definition = self.__layer.GetLayerDefn()
            if self.__definition is None:
                raise Exception('打开矢量文件定义失败')

            # 此处获得的字段不包括空间字段，所以加一

            fieldList = []
            # 遍历读取字段信息
            for index in range(self.fieldCount):
                fieldObject = self.__definition.GetFieldDefn(index)
                field = {
                    'index': index,
                    'name': fieldObject.GetNameRef(),
                    'type': fieldObject.GetFieldTypeName(fieldObject.GetType()),
                    'length': fieldObject.GetWidth(),
                    'precision': fieldObject.GetPrecision()
                }
                fieldList.append(field)
            return fieldList
        except Exception as e:
            print(e)
            return None
        finally:
            self.__close()

    # 读取矢量文件所有坐标信息
    def read_geo(self):
        try:
            self.__getObject()
            feature = self.__layer.GetNextFeature()
            wkbList = []
            while feature is not None:
                wkbList.append(str(feature.GetGeometryRef()))
                feature = self.__layer.GetNextFeature()
            return wkbList
        except Exception as e:
            print(e)
        finally:
            self.__close()

    # 读取矢量文件属性表
    def read_attr(self):
        try:
            self.__getObject()
            attrs = []
            feature = self.__layer.GetNextFeature()
            while feature is not None:
                row_value = []
                for index in range(0, self.fieldCount):
                    row_value.append(feature.GetFieldAsString(index))
                attrs.append(row_value)
                feature = self.__layer.GetNextFeature()
            return attrs
        except Exception as e:
            print(e)
            return None
        finally:
            self.__close()

    def read_values(self):
        try:
            self.__getObject()
            feature = self.__layer.GetNextFeature()
            values = []
            while feature is not None:
                row_value = []
                for index in range(0, self.fieldCount):
                    row_value.append(feature.GetFieldAsString(index))
                row_value.append(str(feature.GetGeometryRef()))
                values.append(row_value)
                feature = self.__layer.GetNextFeature()
            return values
        except Exception as e:
            print(e)

    # 执行完成关闭驱动和数据源
    def __close(self):
        try:
            # 执行完成关闭驱动和数据源
            if self.__dataSource is not None:
                self.__dataSource.Destroy()
            # if self.__driver is not None:
            #     self.__driver.Deregister()
        except Exception as e:
            print(e)
