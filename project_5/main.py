from time import sleep
import requests
import lxml
import json
from bs4 import BeautifulSoup
import pickle
from datetime import datetime
import csv



def get_data(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6"
    }
    correction_date = datetime.now().strftime("%d_%m_%Y")
    print(correction_date)
    # Taking urls list and save it with pickle
    # products_urls_list = []
    # for i in range(1, 10):
    #     url = f"https://shop.casio.ru/catalog/?PAGEN_1={i}"
    #     req = requests.get(url=url, headers=headers)
    #     response = req.text
    #     soup = BeautifulSoup(response, "lxml")
    #     product_cards = soup.find_all("div", class_="product-item")
    #     for card in product_cards:
    #         product_url = "https://shop.casio.ru/" + card.find("a", class_="product-item__link").get("href")
    #         products_urls_list.append(product_url)
    #     print(f"Iteration #{i}")

    # with open("./project_5/data/urls_list.txt", "wb") as file:
    #     pickle.dump(products_urls_list, file)
    with open("./project_5/data/urls_list.txt", "rb") as file:
        products_urls = pickle.load(file)
    result_dict = {}
    all_itterations = int(len(products_urls))
    itteration_count = 1
    with open(f"./project_5/data/result_{correction_date}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
         (
            "title",
            "article",
            "price",
            "photo urls",
            "description",
            "characteristics"
         )
        )
    for url in products_urls:
        photo_urls_list = []
        req = requests.get(url=url, headers=headers)
        response = req.text
        soup = BeautifulSoup(response, "lxml")
        product_title = soup.select("h1", class_="product-card__title")[0].text.split()
        title = " ".join(product_title[:-1])
        article = product_title[-1]
        product_price = soup.find("div", class_="product-card__price").text.split()[-2:]
        price = "".join(product_price)
        photo_urls = soup.findAll("a", class_= "product-card__photo-link")
        for url in photo_urls:
            photo_url = "https://shop.casio.ru/" + url.get("href")
            photo_urls_list.append(photo_url)
        description = soup.find("h2", string="Описание").find_all_next()[4].text.strip()
        characteristics_data = soup.find("h2", string="Характеристики").find_all_next()[4].find_all("tr")
        characteristics_list = []
        for char in characteristics_data:
            items = char.find_all("td")
            characteristics = [item.text.strip() for item in items]
            characteristics_list.append(characteristics)
        characteristics_dict = {key: value for (key, value) in characteristics_list}
        result_dict[article] = {
            "title": title,
            "article": article,
            "price": price,
            "photo urls": photo_urls_list,
            "description": description,
            "characteristics": characteristics_dict
        }
        print(f"Iterration {itteration_count}/{all_itterations}")
        itteration_count += 1
        sleep(1)
        with open(f"./project_5/data/result_{correction_date}.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                title,
                article,
                price,
                photo_urls_list,
                description,
                characteristics_dict
                )
            )
        # with open(f"./project_5/data/result_{correction_date}.json", "a") as file:
        #     json.dump(result_dict, file, indent=4, ensure_ascii=False)
        

def main():
    get_data("https://shop.casio.ru/catalog/")


if __name__ == "__main__":
    main()