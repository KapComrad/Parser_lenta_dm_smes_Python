from ast import pattern
from asyncio.windows_events import NULL
from msilib.schema import File
from sys import getdefaultencoding
import re
import sys
from this import s
import undetected_chromedriver as uc
import requests
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
import os
from datetime import datetime


def get_data_with_uc(url,name):
    try:
        driver = uc.Chrome(driver_executable_path='C:\\Users\\serg\\source\\repos\\PythonApplication3\\PythonApplication3\\chromedriver.exe',use_subprocess = True)
        driver.get(url=url)
        driver.implicitly_wait(20)
        with open ('C:\\Users\\serg\source\\repos\\PythonApplication3\\PythonApplication3\\'+name+'.html' ,'w',encoding='utf-8') as file:
            print("opened")
            file.write(driver.page_source)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()



def read_data_from_dm():
    if (time.time() - os.path.getmtime("index.html")) > 1800:
        get_data_with_uc("https://www.detmir.ru/catalog/index/name/suhie_smesi_i_zameniteli_moloka/brand/9341/stores-2341/age-0~5/", "index_dm")
    if (time.time() - os.path.getmtime("data.csv")) > 1800:
        with open('C:\\Users\\serg\source\\repos\\PythonApplication3\\PythonApplication3\\index.html', encoding='utf-8-sig') as file:
            src = file.read()
        if os.path.exists("data.csv"):
            os.remove("data.csv")
        soup = BeautifulSoup(src,"lxml")
        all_products_hrefs = soup.find_all(class_="SY")
        for item in all_products_hrefs:
            discount_without_html = []
            name_without_html = []
            price_without_html = []
            soup2 = BeautifulSoup(str(item),"lxml")
            product_href = soup2.find_all(class_="SZ")
            for item in product_href:
                soup3 = BeautifulSoup(str(item),"lxml")
                discount = soup3.find_all(class_="LK")
                for item in discount:
                    discount_without_html = re.findall(r'">([^"></]+)</',str(item))
            for item in product_href:
                name = soup3.find_all(class_="SU")
                for item in name:
                    name_without_html = re.findall(r'">([^"></]+)</',str(item))
            for item in product_href:
                price = soup3.find_all(class_="S_4")
                for item in price:
                    price_without_html = [item]
            print(discount_without_html + name_without_html + price_without_html)
            with open ("data.csv", "a", encoding="utf-8-sig") as file:
                writer = csv.writer(file, lineterminator='\n')
                writer.writerow((discount_without_html,name_without_html,price_without_html))
            print("#######")

def read_data_from_lenta():
    if os.path.exists("index_lenta.html") == False:
        get_data_with_uc("https://lenta.com/catalog/tovary-dlya-detejj/detskoe-pitanie/molochnye-smesi/f/brandname=nan/", "index_lenta")
    if (time.time() - os.path.getmtime("index_lenta.html")) > 1800:
        get_data_with_uc("https://lenta.com/catalog/tovary-dlya-detejj/detskoe-pitanie/molochnye-smesi/f/brandname=nan/", "index_lenta")
    with open('C:\\Users\\serg\source\\repos\\PythonApplication3\\PythonApplication3\\index_lenta.html', encoding='utf-8-sig') as file:
        src = file.read()
    if os.path.exists("data_lenta.csv"):
        os.remove("data_lenta.csv")
    soup = BeautifulSoup(src,"lxml")
    all_products_hrefs = soup.find_all(class_="catalog-grid__grid")
    for item in all_products_hrefs:
        discount = []
        name = []
        print(item)
        soup2 = BeautifulSoup(str(item),"lxml")
        product_href = soup2.find_all(class_="sku-card-small-container")
        print(product_href.__len__())
        for item1 in product_href:
            soup3 = BeautifulSoup(str(item1),"lxml")
            soup4 = BeautifulSoup(str(item1),"lxml")
            discount = soup3.find_all(class_="price-label__integer")
            name = soup4.find_all(class_="sku-card-small-header__title")
            print(discount)
            print(name)
            with open ("data_lenta.csv", "a", encoding="utf-8-sig") as file:
                writer = csv.writer(file, lineterminator='\n')
                writer.writerow((discount,name))
        print("#######")




def main():
    #read_data_from_dm()
    read_data_from_lenta()


if __name__ == '__main__':
    main()

#import time

#from selenium import webdriver



#driver = webdriver.Chrome('C:\\Users\\serg\source\\repos\\PythonApplication3\\PythonApplication3\\chromedriver.exe')  # Optional argument, if not specified will search path.

#driver.get('http://www.google.com/');

#time.sleep(5) # Let the user actually see something!

#search_box = driver.find_element_by_name('q')

#search_box.send_keys('ChromeDriver')
#get_source = driver.page_source
#fileToWrite = open('C:\\Users\\serg\source\\repos\\PythonApplication3\\PythonApplication3\\index.html' ,'w',encoding='utf-8')
#print(get_source)
#fileToWrite.write("hjhjhj")
#fileToWrite.close()

#search_box.submit()

#time.sleep(5) # Let the user actually see something!

