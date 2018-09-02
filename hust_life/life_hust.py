#Yanglin TU
#2018-08-31
import requests
from requests.exceptions import RequestException
import csv
from pyquery import PyQuery as pq
import time

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    doc = pq(html)
    content = doc('.content table:nth-of-type(1) tbody')
    name = content('tr:first-child').text()
    tittle = content('tr:nth-child(2) td:last-child').text()
    subject = content('tr:nth-child(3) td:last-child').text()
    phone = content('tr:nth-child(4) td:last-child').text()
    mail = content('tr:last-child td:last-child').text()
    with open("data.csv", 'a', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'tittle', 'subject', 'phone', 'mail']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({'name': name, 'tittle': tittle,'subject': subject, 'phone': phone, 'mail': mail})

def main(label,number):
    url = 'http://life.hust.edu.cn/info/'+str(label)+'/'+str(number)+'.htm'
    html = get_one_page(url)
    if html!=None:
        parse_one_page(html)

if __name__ == '__main__':
    for i in range(1021,1024):
        for j in range(1000,2000):
            main(i,j)
            time.sleep(1)



