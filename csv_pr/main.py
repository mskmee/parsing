from traceback import print_tb
from xml.dom import IndexSizeErr
import requests
from bs4 import BeautifulSoup
import lxml
import csv


def main():
    data_list = []
    with open("./csv_pr/task_1_4.html", "r") as file:
        url = file.read()

    soup = BeautifulSoup(url, "lxml")
    # data = soup.find("table").find("thead").find("tr").find_all("th")
    # datsa = soup.find("table").find("tbody").find_all("tr")
    data = soup.find_all("table")[0].find("tbody").find_all("tr")
    for item in data:
        td = item.find_all("td")
        id = td[0].text
        name = td[1].text
        genre = td[2].text
        author = td[3].text
        date_pub = td[4].text
        pages = td[5].text
        price = td[6].text
        
        try:
            rating = td[7].text
        except IndexError:
            pass
        with open("./csv_pr/data.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                id,
                name,
                genre,
                author,
                date_pub,
                pages,
                price,
                rating
                )
            )
    # for el in data:
    #     all_tds = el.find_all("td")
    #     tr_list = []
    #     for tr in all_tds:
    #         tr_list.append(tr.text)
    #     data_list.append(tr_list)
    # for el in data_list:
    #     el[0]R
    # for data in datsa:
    #     element = data.find_all("td")
    #     data_l = []
    #     for el in element:
    #         data_l.append(el.text)
    #     data_list.append(data_l)
    # print(data_list)
    # for el in data_list:
    #     for i in range(0, len(el)):
            

    # for el in data:
    #     data_list.append(el.text)
    
    # with open("./csv_pr/data.csv", "w") as file:
    #     writer = csv.writer(file)
    #     writer.writerow(
    #         (
    #         "id",
    #         "Name",
    #         "genre",
    #         "author",
    #         "date_pub",
    #         "pages",
    #         "price",
    #         "rating"
    #         )
    #     )


if __name__ == "__main__":
    main()