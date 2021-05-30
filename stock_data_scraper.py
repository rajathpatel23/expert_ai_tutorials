import requests
from bs4 import BeautifulSoup

def getData(symbol):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    url = f'https://uk.finance.yahoo.com/quote/{symbol}'

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    stock = {
    "symbol": symbol,
    "price": soup.find('div', {"class": 'D(ib) Mend(20px)'}).find_all('span')[0].text,
    "change": soup.find('div', {"class": "D(ib) Mend(20px)"}).find_all('span')[1].text }
    return stock

print(getData("TSLA"))