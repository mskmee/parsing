import json
import requests
from bs4 import BeautifulSoup
import lxml
from time import sleep
import pickle


def get_data(url):
    hotel_data_result = []
    hotel_urls = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }
    # req = requests.get(url=url, headers=headers)
    # response = req.text
    # soup = BeautifulSoup(response, "lxml")
    # hotel_cards = soup.find_all("div", class_="hotel_card_dv")

    # for hotel in hotel_cards:
    #     hotel_url = "https://www.tury.ru" + hotel.find("a", class_="hotel_name").attrs["href"].split("?")[0]
    #     hotel_urls.append(hotel_url)  

    # for i in range(30, 121, 30):
    #     req = requests.get(url=f"{url}&s={i}")
    #     response = req.text
    #     soup = BeautifulSoup(response, "lxml")
    #     hotel_cards = soup.find_all("div", class_="hotel_card_dv")
    #     for hotel in hotel_cards:
    #         hotel_url = "https://www.tury.ru" + hotel.find("a", class_="hotel_name").attrs["href"].split("?")[0]
    #         hotel_urls.append(hotel_url)

    # iteration_counts = int(len(hotel_urls))

    # with open("hotel_urls.txt", "rb") as file:
    #     pickle.dump(hotel_urls, file)
    with open("hotel_urls.txt", "rb") as file:
        hotel_urls = pickle.load(file)

    for url in hotel_urls[0:15]:
        req = requests.get(url=url, headers=headers)
        response = req.text
        soup = BeautifulSoup(response, "lxml")
        hotel_items = soup.find("li", class_="hotel_info_block").text
        hotel_title = hotel_items.rsplit("Отель")[0]
        hotel_data_result.append({
            "Hotel title": hotel_title,
            "Hotel url": url,
        })
    with open("hotel_data.json", "a") as file:
        json.dump(hotel_data_result, file, ensure_ascii=False, indent=4)
        

def main():
    get_data("https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most&hotel_link=/hotel/id/%HOTEL_ID%&r=1380893784")


if __name__ == "__main__":
    main()