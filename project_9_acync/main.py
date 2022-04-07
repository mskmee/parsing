import pickle
from bs4 import BeautifulSoup
import requests
from random import randint
import os
import json


def get_data(url):
    url = url
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }
    proxy_list = get_proxy()
    proxy_index = randint(0, len(proxy_list) - 1)
    # proxy_index = 1
    # proxy = {"https": proxy_list[proxy_index], "http": proxy_list[proxy_index]}
    proxy = {"https": "63.161.104.189:3128", "http": "63.161.104.189:3128"}
    print(proxy)
    req = requests.get(url=url, headers=headers, proxies=proxy)
    response = req.text
    soup = BeautifulSoup(response, "lxml")
    page_count = soup.find_all("a", class_="pagination-number__text")[-1].text
    for i in range(1, int(page_count) + 1):
        url = "https://www.labirint.ru/genres/2308/?available=1&paperbooks=1&display=tabl&page={i}"
        req = requests.get(url=url, headers=headers, proxies=proxy)
        response = req.text
        with open(f"./project_7/data/page_{i}.html", "w") as file:
            file.write(response)
        print(f"Iteration #{i}")


def get_proxy():
    with open("./proxies/proxies.txt", "rb") as file:
        proxy_list = pickle.load(file)
    return proxy_list


def work_with_data():
    result_list = []
    files_name = os.listdir("./project_9_acync/data")
    files_name_list = [f"./project_9_acync/data/page_{i}.html" for i in range(1, len(files_name) + 1)]
    all_iterations = len(files_name_list)
    count = 1
    for i in files_name_list[:1]:
        with open(i, "r") as file:
            data = file.read()
        
        soup = BeautifulSoup(data, "lxml")
        all_cards = soup.find_all("div", class_="card-column")
        print(f"Iteration {count}/{all_iterations}")
        count += 1
        for card in all_cards:
            book_url = "https://www.labirint.ru" + card.find("a", class_="cover").attrs["href"]
            author_data = card.find("a", class_="cover").attrs["title"].strip().split("-")
            book_author = "".join(author_data[0]).strip()
            book_title = "".join(author_data[1:]).strip()
            price = card.find("span", class_="price-val").text.strip().strip("₽").replace(" ", "")
            try:
                old_price = card.find("span", class_="price-old").text.strip().replace(" ", "")
            except AttributeError:
                old_price = "no old price"
            img_url = card.find("img", class_="book-img-cover").attrs["data-src"]
            try:
                percent_sale = 100 - (int(price) / int(old_price) * 100) 
                round_percent_sale = round(float(percent_sale))
            except ValueError:
                percent_sale = "none"
            result_dict = {
                "book_url": book_url,
                "book_title": book_title,
                "book_autor": book_author,
                "price":{
                    "old_price": old_price,
                    "price": price,
                    "percent_sale": round_percent_sale
                },
                "img_url": img_url
            }

            result_list.append(result_dict)

    with open("./project_9_acync/result.json", "a") as file:
        json.dump(result_list, file, indent=4, ensure_ascii=False)


def main():
    get_data("https://www.labirint.ru/genres/2308/?available=1&paperbooks=1&display=tabl&page=1")


if __name__ == "__main__":
    # main()
    work_with_data()