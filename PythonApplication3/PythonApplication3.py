from ast import pattern
from asyncio.windows_events import NULL
from msilib.schema import File
from sys import getdefaultencoding
import re
from this import s
from tkinter import W
import undetected_chromedriver as uc
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
        time.sleep(20)
        with open ('C:\\Users\\serg\source\\repos\\PythonApplication3\\PythonApplication3\\'+name+'.html' ,'w',encoding='utf-8') as file:
            print("opened")
            file.write(driver.page_source)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def read_data_from_dm():
    if os.path.exists("index_dm.html") == False:
        get_data_with_uc("https://www.detmir.ru/catalog/index/name/suhie_smesi_i_zameniteli_moloka/brand/9341/stores-2341/age-0~5/", "index_dm")
    if (time.time() - os.path.getmtime("index_dm.html")) > 1800:
        get_data_with_uc("https://www.detmir.ru/catalog/index/name/suhie_smesi_i_zameniteli_moloka/brand/9341/stores-2341/age-0~5/", "index_dm")
    with open('C:\\Users\\serg\source\\repos\\PythonApplication3\\PythonApplication3\\index_dm.html', encoding='utf-8-sig') as file:
        src = file.read()
    if os.path.exists("data_dm.csv"):
        os.remove("data_dm.csv")
    soup = BeautifulSoup(src,"lxml")
    all_products_hrefs = soup.find_all(class_="S_6")
    for item in all_products_hrefs:
        print("TUT?")
        discount_without_html = []
        name_without_html = []
        price_without_html = []
        soup2 = BeautifulSoup(str(item),"lxml")
        product_href = soup2.find_all(class_="S_7")
        for item in product_href:
            soup3 = BeautifulSoup(str(item),"lxml")
            name = soup3.find_all(class_="S_2")
            for item in name:
                name_without_html = re.findall(r'">([^"></]+)</',str(item))
        for item in product_href:
            price = soup3.find_all(class_="Td")
            for item in price:
                price_without_html = [item]
        print(discount_without_html + name_without_html + price_without_html)
        with open ("data_dm.csv", "a", encoding="utf-8-sig") as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow((discount_without_html,name_without_html,price_without_html))
        print("#######")
    replace_symbols_in_data_dm()

def replace_symbols_in_data_dm():
    if os.path.exists("data_dm.txt"):
        os.remove("data_dm.txt")
    with open ("C:\\Users\\serg\\source\\repos\\PythonApplication3\\PythonApplication3\\data_dm.csv", "r+", encoding="utf-8-sig") as file:
        fin = open("data_dm.txt","w",encoding="utf-8-sig")
        for line in file:
            rep = ["[","]","'",'<p class=""S_4"">',"</p>",'"','<p class=Td>']
            for item in rep:
                if item in line:
                    line = line.replace(item,'')
            rep2 = [',']
            for item2 in rep2:
                if item2 in line:
                    line = line.replace(item2,' ')
            fin.write(line)

def replace_symbols_in_data_lenta():
    if os.path.exists("data_lenta.txt"):
        os.remove("data_lenta.txt")
    with open ("C:\\Users\\serg\\source\\repos\\PythonApplication3\\PythonApplication3\\data_lenta.csv", "r+", encoding="utf-8-sig") as file:
        fin = open("data_lenta.txt","w",encoding="utf-8-sig")
        for line in file:
            rep = ['<span class=""price-label__integer"">','"[<div class=""sku-card-small-header__title"">','</div>]',"</p>",'</span>',"[","]","'",'"']
            for item in rep:
                if item in line:
                    line = line.replace(item,'')
            rep2 = [',']
            for item2 in rep2:
                    if item2 in line:
                        line = line.replace(item2,' ')
            fin.write(line)



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
    replace_symbols_in_data_lenta()

def main():
    print("PY")
    #read_data_from_dm()
    #replace_symbols_in_data_dm()
    #read_data_from_lenta()
    #replace_symbols_in_data_lenta()

if __name__ == '__main__':
    main()


