import pickle
from random import randint
import requests
from bs4 import BeautifulSoup


def get_data(url):
    proxies = get_proxie()
    url = url
    print(url)
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }

    try:
        proxy_index = randint(0, len(proxies) - 1)
        proxy = {"https": proxies[proxy_index], "http": proxies[proxy_index]}
        req = requests.get(url=url, headers=headers, proxies=proxy)
        print(req.status_code)
    except Exception as e:
        print(e)
    print(req.text)


def get_proxy():
    with open("./proxies/proxies.txt", "rb") as file:
        proxy_list = pickle.load(file)
    print(proxy_list)


def main():
    # get_data("https://www.labirint.ru/books/")
    get_proxy()

