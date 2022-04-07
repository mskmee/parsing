from time import sleep
import lxml
import requests
import os
from bs4 import BeautifulSoup
import json
from random import randrange
from selenium import webdriver
import codecs


# chrome_driver_path = 'D:\python_projects\selenium\drivers\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.skiddle.com/festivals/search/?sort=0&fest_name=&from_date=4%20Mar%202022&to_date=&maxprice=500")

# while True:
#     try:
#         add_more_festivals = driver.find_element_by_id("more_link")
#         sleep(1)
#         add_more_festivals.click()
#         sleep(2)
#     except:
#         break
# page_data = os.path.join("D:\python_projects\selenium", "data.html")
# file = codecs.open(page_data, "w", "utf-8")
# driver_data = driver.page_source
# file.write(driver_data)
# sleep(5)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6"
}

with open("./project_2/data.html") as file:
    src = file.read()


soup = BeautifulSoup(src, "lxml")
all_festivals = soup.find_all("div", class_="grid__col-md-4")
# festivals_dict = {}
festival_urls = []
for festival in all_festivals:
    # festival_title = festival.find("div", class_="card-info").find("a").text
    festival_url = "https://www.skiddle.com" + festival.find("div", class_="card-info").find("a").attrs['href']
    # festival_date = festival.find("div", class_="card-info").find("div", class_="tc-grey").find("p", class_="margin-bottom-0").text
    festival_urls.append(festival_url)
# with open("./project_2/data/festival_dict.json", "a") as file:
#     json.dump(festivals_dict, file, ensure_ascii=False, indent=4)

# with open("./project_2/data/festival_dict.json", "r") as file:
#     all_festivals = json.load(file)

iterations_count = int(len(festival_urls))
locates_url = []
fest_list_result = []
for url in festival_urls:
    try:
        response = requests.get(url=url, headers=headers)
        src = response.text
        soup = BeautifulSoup(src, "lxml")
        festival_title = soup.find("h1", class_="tc-white").text.strip()
        festival_date = soup.find("h3", class_="tc-white").text.strip()
        locate_url = "https://www.skiddle.com" + soup.find("p").find_next("a").attrs["href"]
        contact_response = requests.get(url=locate_url, headers=headers)
        contact_src = contact_response.text
        contact_soup = BeautifulSoup(contact_src, "lxml")
        
        contact_details = contact_soup.find("h2", string="Venue contact details and info").find_next()

        items = [item.text for item in contact_details.find_all("p")]

        contact_details_dict = {}
        for contact_detail in items:
            contact_detail_list = contact_detail.split(":")

            if len(contact_detail_list) == 3:
                contact_details_dict[contact_detail_list[0].strip()] = contact_detail_list[1].strip() + ":" \
                                                                        + contact_detail_list[2].strip()
            else:
                contact_details_dict[contact_detail_list[0].strip()] = contact_detail_list[1].strip()

        fest_list_result.append(
            {
                "Fest name": festival_title,
                "Fest date": festival_date,
                "Contacts data": contact_details_dict
            }
        )
        print(f"Iterations: {iterations_count}/{len(festival_urls)}")
        iterations_count -= 1
        sleep(randrange(2, 4))
         
    except Exception as ex:
        print(ex)
        print("Damn...There was some error...")
with open("./project_2/data/fest_list_result.json", "a", encoding="utf-8") as file:
    json.dump(fest_list_result, file, indent=4, ensure_ascii=False)

    