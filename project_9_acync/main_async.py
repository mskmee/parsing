import json
from bs4 import BeautifulSoup
import lxml
import requests
from datetime import datetime
from time import sleep, time
from random import randrange
import asyncio
import aiohttp



products_data = []
start_time = time()
now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
headers = {
    "X-Is-Ajax-Request": "X-Is-Ajax-Request",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01"
}


async def get_page_data(session, page):
    url = f"https://roscarservis.ru/catalog/legkovye/?form_id=catalog_filter_form&filter_mode=params&sort=asc&filter_type=tires&arCatalogFilter_458_1500340406=Y&set_filter=Y&arCatalogFilter_463=668736523&PAGEN_1={page}"
    headers = {
    "X-Is-Ajax-Request": "X-Is-Ajax-Request",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01"
}

    async with session.get(url=url, headers=headers) as response:
        # data = await response.json()
        data_to_json = []
        data = await response.text()  
        data_to_json.append(data)
        data2 = data.json()
        print(data2)
    #     for item in data["items"]:
    #         photo_url = "https://roscarservis.ru" + item["imgSrc"]
    #         product_url = "https://roscarservis.ru" + item["url"]
    #         product_title = item["name"]
    #         vendor_code = item["initial"]["vendorCode"]
    #         storages_list = []
    #         for element in item["commonStores"]:
    #             storage_name = element["STORE_NAME"]
    #             storage_price = element["PRICE"]
    #             storage_amount = element["AMOUNT"]
    #             storage_dict = {
    #                 "storage_name": storage_name,
    #                 "storage_price": storage_price,
    #                 "storage_amount": storage_amount
    #             }
    #             storages_list.append(storage_dict)
    #         data_dict = {
    #             "product_title": product_title,
    #             "vendor_code": vendor_code,
    #             "product_url": product_url,
    #             "product_photo url": photo_url,
    #             "storages": storages_list
    #         }
    #         products_data.append(data_dict)
    # print(f"[INFO] Page # {page} comlited")

            
async def gather_data(headers):
    url = "https://roscarservis.ru/catalog/legkovye/?form_id=catalog_filter_form&filter_mode=params&sort=asc&filter_type=tires&arCatalogFilter_458_1500340406=Y&set_filter=Y&arCatalogFilter_463=668736523&PAGEN_1=1"
    headers = headers
    async with aiohttp.ClientSession() as session:
        response = await session.get(url=url, headers=headers)
        # soup = BeautifulSoup(await response.text, "lxml")
        # data = await response.json()
        # page_count = data["pageCount"]
        tasks = []
        for page in range(1, 6):
            task = asyncio.create_task(get_page_data(session=session, page=page))
            tasks.append(task)
        await asyncio.gather(*tasks)


def main():
    asyncio.run(gather_data(headers=headers))
    finish_time = time() - start_time
    with open(f"./project_9_acync/data/{now}.json", "a") as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)
    print(f"Spended time is {finish_time}")

if __name__ == "__main__":
    main()

def get_data(url):
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    req = requests.get(url=url, headers=headers)
    data = req.json()
    result_list = []
    # with open("./project_6/data/page_n.json", "a") as file:
    #     json.dump(data, file, indent=4, ensure_ascii=False)    
    page_count = data["pageCount"]
    for i in range(1, page_count):
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