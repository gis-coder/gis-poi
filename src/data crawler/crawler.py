#!/usr/bin/env python3.7
# -*- coding:utf-8 -*-

import urllib
import requests
from bs4 import BeautifulSoup


# 获取需要爬取的数据分类
def get_catogrys(url_path):
    try:
        url_request = requests.get(url_path)
        url_soup = BeautifulSoup(url_request.text)
        # 获取分类标签  <div class="catgory"></div>
        catgory_eles = url_soup.find_all('div', class_='catgory')
        if catgory_eles is None or len(catgory_eles) == 0:
            raise Exception('未能读取到目录信息')
        for catgory_ele in catgory_eles:
            # 获取分类标签中的a标签的属性href值
            catgory_url = url_path + catgory_ele.find_all('a')[0].get('href')
            get_citys(url_path, catgory_url)
        # 使用完成后清理对象内存
        url_soup.clear()
        url_request.close()
    except Exception as e:
        print(e)


# 获取每种分类对应的城市列表
# url_path:原始网页的标签
# catogry:分类列表
def get_citys(url_path, catogry):
    try:
        catgory_request = requests.get(catogry)
        catgory_soup = BeautifulSoup(catgory_request.text)
        # 读取城市标签元素
        city_eles = catgory_soup.find_all('div', class_='col-xs-10')
        for city_ele in city_eles:
            city_eles = city_ele.find_all('a')
            for city_ele in city_eles:
                # 城市标签中的href值只是完整标签的后半段，需要进行拼接
                city_url = url_path + city_ele.get('href')
                if city_url.find('北京') == -1:
                    continue
                print(city_url)
                get_pages(url_path, city_url)
        # 完成后清理对象
        catgory_soup.clear()
        catgory_request.close()
    except Exception as e:
        print(e)


# 获取对应城市的分页链接
# url_path:原始网页链接
# city_url:城市数据对应的链接
def get_pages(url_path, city_url):
    try:
        city_request = requests.get(city_url)
        city_soup = BeautifulSoup(city_request.text)
        # 获取分页列表标签
        page_ele = city_soup.find_all('ul', class_='pagination pagination-sm mar-t5')
        page_hrefs = page_ele[0].find_all('a')
        for page_href in page_hrefs:
            if str.strip(page_href.get('href')) == '':
                continue
            page_url = url_path + page_href.get('href')
            get_pois(page_url)
        city_soup.clear()
        city_request.close()
    except Exception as e:
        print(e)


# 根据分页链接获取页面中的poi表数据
# 将表格的数据拼接为sql语句生成txt文件
def get_pois(page_url):
    try:
        poi_request = requests.get(page_url)
        poi_soup = BeautifulSoup(poi_request.text)
        tb_div = poi_soup.find_all('table', class_='table table-bordered table-striped table-hover data-table')
        # 表头
        thead_ele = tb_div[0].find_all('th')
        # 表格
        rows = tb_div[0].find_all('tr')

        data_path = r'D:\Code\gis-poi\data\poi.txt'
        data = open(data_path, 'a', encoding='utf-8')

        for row in rows:
            cells = row.find_all('td')
            # 插入式需要将特殊符号转义，此处不完整，只进行了单引号的转义
            sql = "insert into " \
                  "tb_poi(f_name,f_pname,f_cname,f_dname,f_dcode,f_tel,f_area,f_address,f_b,f_s,f_x,f_y) " \
                  "values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}',{10},{11});".format(
                cells[1].text.replace("'", "\\'"), cells[2].text.replace("'", "\\'"),
                cells[3].text.replace("'", "\\'"), cells[4].text.replace("'", "\\'"),
                cells[5].text.replace("'", "\\'"), cells[6].text.replace("'", "\\'"),
                cells[7].text.replace("'", "\\'"), cells[8].text.replace("'", "\\'"),
                cells[9].text.replace("'", "\\'"), cells[10].text.replace("'", "\\'"),
                cells[11].text.replace("'", "\\'"), cells[12].text.replace("'", "\\'"))
            data.write(sql + "\n")
        data.close()

        poi_soup.clear()
        poi_request.close()
    except Exception as e:
        print(e)


# 函数入口
if __name__ == '__main__':
    try:
        # 需要爬取的网页地址
        url_path = 'http://www.poilist.cn/'

        get_catogrys(url_path)

        print('complate')
    except Exception as e:
        print(e)
