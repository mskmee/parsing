import random
from time import sleep
import lxml
from bs4 import BeautifulSoup
import requests
import json
import csv
from datetime import datetime



# url = "https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6"
}

# response = requests.get(url, headers=headers)

# src = response.text

# with open("./project_1/index.html", "r") as file:
#     src = file.read()

# soup = BeautifulSoup(src, "lxml")
# all_products_href = soup.find_all(class_="mzr-tc-group-item-href")
# all_categoryes_dict = {}

# for item in all_products_href:
#     item_text = item.text
#     item_href = "https://health-diet.ru" + item.get("href")
#     all_categoryes_dict[item_text] = item_href

# with open ("./project_1/all_categoryes_dict.json", "w") as file:
#     json.dump(all_categoryes_dict, file, indent=4, ensure_ascii=False)

with open("./project_1/all_categoryes_dict.json", "r") as file:
    all_categories = json.load(file)

iterations = int(len(all_categories)) - 1
count = 0

print(f"All itterations: {iterations}")
for category_name, category_href in all_categories.items():

    rep = ["-", " ", ",", "'"]
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, "_")
    
    response = requests.get(url=category_href, headers=headers)
    src = response.text

    with open(f"./project_1/data/{count}_{category_name}.html", "w") as file:
        file.write(src)
        
    with open(f"./project_1/data/{count}_{category_name}.html", "r") as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    # check table for exist
    alert_block = soup.find(class_="uk-alert-danger")
    if alert_block is not None:
        continue
    # take headers from the table
    table_head = soup.find(class_="uk-table").find("tr").find_all("th")
    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text
    with open(f"./project_1/data/{count}_{category_name}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                product, 
                calories, 
                proteins, 
                fats, 
                carbohydrates
            )
        )
    # take products data
    product_info = []
    products_data = soup.find(class_="uk-table").find("tbody").find_all("tr")
    for item in products_data:
        products_tds = item.find_all("td")

        title = products_tds[0].find("a").text
        calories = products_tds[1].text
        proteins = products_tds[2].text
        fats = products_tds[3].text
        carbohydrates = products_tds[4].text
        
        product_info.append(
            {
                "Title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fats": fats,
                "Carbohydrates": carbohydrates
            }
        )

        with open(f"./project_1/data/{count}_{category_name}.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    title, 
                    calories, 
                    proteins, 
                    fats, 
                    carbohydrates
                )
            )
        with open(f"./project_1/data/{count}_{category_name}.json", "a", encoding="utf-8") as file:
            json.dump(product_info, file, ensure_ascii=False, indent=4)
    count += 1
    print(f"Iteration {count} {category_name} complited")
    iterations = iterations -1
    if iterations == 0:
        "Work is done"
        break
    print(f"There are {iterations} left")
    sleep(random.randrange(2,4))
