# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 09:22:34 2019

@author: haidinata
"""

import bonobo
import requests
from bs4 import BeautifulSoup

def scrape_zillow():
    price = '5000'
    status = ''
    url = 'https://www.bukalapak.com/c/komputer/laptop?'
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        html = r.text.strip()
        soup = BeautifulSoup(html, 'lxml') 
        harga = soup.select('.amount')
        harga1 = harga[0]
        status = harga1.text
        print(status)
        
        price_status_section = soup.select('.amount')
        if len(price_status_section) > 1:
            price = price_status_section[0].text.strip()
    return price

def scrape_redfin():
    price = ''
    #status = ''
    item = ''
    url = 'https://www.bukalapak.com/c/komputer/laptop?'
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        html = r.text.strip()
        soup = BeautifulSoup(html, 'lxml')
        
        barang = soup.select('.product__name')
        barang1 = barang[0]
        status = barang1.text
        print(status)
        
        item = soup.select('.product__name')
        if item:
            item = item[0].text.strip()
    return item

def extract():
    yield scrape_zillow()
    yield scrape_redfin()
    
def transform(price: str):
    t_price = price.replace(',', '').lstrip('$')
    return t_price

def load(price: float):
    with open('pricing.txt', 'a+', encoding='utf8') as f:
        f.write((str(price) + '\n'))
        
if __name__ == '__main__':
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'referrer': 'https://google.com'
    }
    # scrape_redfin()
    graph = bonobo.Graph(
        extract,
        transform,
        load,
    )
    bonobo.run(graph)