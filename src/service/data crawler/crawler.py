#!/usr/bin/env python3.7
# -*- coding:utf-8 -*-

import urllib
import requests
from bs4 import BeautifulSoup

sqls = []


def get_catogrys(url_path):
    try:
        url_request = requests.get(url_path)
        url_soup = BeautifulSoup(url_request.text)
        catgory_eles = url_soup.find_all('div', class_='catgory')
        if catgory_eles is None or len(catgory_eles) == 0:
            raise Exception('未能读取到目录信息')

        for catgory_ele in catgory_eles:
            catgory_url = url_path + catgory_ele.find_all('a')[0].get('href')
            get_citys(url_path, catgory_url)
        url_soup.clear()
        url_request.close()
    except Exception as e:
        print(e)


def get_citys(url_path, catogry):
    try:
        catgory_request = requests.get(catogry)
        catgory_soup = BeautifulSoup(catgory_request.text)
        city_eles = catgory_soup.find_all('div', class_='col-xs-10')
        for city_ele in city_eles:
            city_eles = city_ele.find_all('a')
            for city_ele in city_eles:
                city_url = url_path + city_ele.get('href')
                get_pages(url_path, city_url)
        catgory_soup.clear()
        catgory_request.close()
    except Exception as e:
        print(e)


def get_pages(url_path, city_url):
    try:
        city_request = requests.get(city_url)
        city_soup = BeautifulSoup(city_request.text)
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


def get_pois(page_url):
    try:
        poi_request = requests.get(page_url)
        poi_soup = BeautifulSoup(poi_request.text)
        tb_div = poi_soup.find_all('table', class_='table table-bordered table-striped table-hover data-table')
        thead_ele = tb_div[0].find_all('th')
        rows = tb_div[0].find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            sql = "insert into " \
                  "poi(name,p_name,c_name,d_name,d_code,tel,area,address,b_c,s_c,poi_x,poi_y) " \
                  "values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}',{10},{11});".format(
                cells[1].text, cells[2].text, cells[3].text, cells[4].text, cells[5].text, cells[6].text, cells[7].text,
                cells[8].text, cells[9].text, cells[10].text, cells[11].text, cells[12].text)
            print(sql)
            sqls.append(sql)
        poi_soup.clear()
        poi_request.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    url_path = 'http://www.poilist.cn/'

    get_catogrys(url_path)

    print('complate')
