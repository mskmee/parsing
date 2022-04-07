import json
import lxml
import requests
from datetime import datetime
from time import sleep
from random import randrange


headers = {
    "X-Is-Ajax-Request": "X-Is-Ajax-Request",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01"
}


def get_data(url):
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    req = requests.get(url=url, headers=headers)
    data = req.json()
    result_list = []
    # with open("./project_6/data/page_n.json", "a") as file:
    #     json.dump(data, file, indent=4, ensure_ascii=False)    
    page_count = data["pageCount"]
    for i in range(1, 3):
        print(f"Iteration #{i}")
        url = f"https://roscarservis.ru/catalog/legkovye/?form_id=catalog_filter_form&filter_mode=params&sort=asc&filter_type=tires&arCatalogFilter_458_1500340406=Y&set_filter=Y&arCatalogFilter_463=668736523&PAGEN_1={i}"
        req = requests.get(url=url, headers=headers)
        data = req.json()
        for item in data["items"]:
            photo_url = "https://roscarservis.ru" + item["imgSrc"]
            product_url = "https://roscarservis.ru" + item["url"]
            product_title = item["name"]
            vendor_code = item["initial"]["vendorCode"]
            storages_list = []
            for element in item["commonStores"]:
                storage_name = element["STORE_NAME"]
                storage_price = element["PRICE"]
                storage_amount = element["AMOUNT"]
                storage_dict = {
                    "storage_name": storage_name,
                    "storage_price": storage_price,
                    "storage_amount": storage_amount
                }
                storages_list.append(storage_dict)
            data_dict = {
                "product_title": product_title,
                "vendor_code": vendor_code,
                "product_url": product_url,
                "product_photo url": photo_url,
                "storages": storages_list
            }
            result_list.append(data_dict)
            sleep(randrange(2, 4))

    with open(f"./project_6/data/{now}.json", "w") as file:
        json.dump(result_list, file, indent=4, ensure_ascii=False)


def main():
    get_data("https://roscarservis.ru/catalog/legkovye/?form_id=catalog_filter_form&filter_mode=params&sort=asc&filter_type=tires&arCatalogFilter_458_1500340406=Y&set_filter=Y&arCatalogFilter_463=668736523&PAGEN_1=1")


if __name__ == "__main__":
    main()