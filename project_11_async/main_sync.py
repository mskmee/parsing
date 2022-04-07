import json
import requests
from bs4 import BeautifulSoup
import csv

    
def take_pagination_count():
    headers ={
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "cookie": "INGRESSCOOKIE=1647184774.026.241327.874768; checkedSwitchClone=1; fuel_csrf_token=58497b1df63fcfa497a84f7626575d38f5fcea9927edcf866be331170ff4fa822d04bb606b8db0abf31fab5a1a47477b820b972d92f51fb22b8843c02ce1d703; fuelrid1=7NxstXN7se0k6bwPltT3yHXE_7ipfDHPH720Dq8dhNHpQGLQfOkpkXgg5zjPGiTx9kxqWEZ1iO01Eos8WZmCqHM3OXJzZ3J3bWk4b1hLNFlubXJqcVBRcy1aT21RNXo1U3oyYVNVUkhma1E; clientCode=881101; drv=rds; kmtx_sync=1549189590302943053; _ga=GA1.2.1111548562.1647184837; _gid=GA1.2.1215085130.1647184837; ui=2; fueldid=T-HiCD-f24MeGEf8KXSk0iR9slOuDhP9-pElj5ddFbqZ1MegtY7Ydp3G1lbG2rk11CoUjTQl8_8YDah-klMKpDlZSW5kTFdsT3JQbHdDTWVROHZVd0FhQVFwWU9VTzY3bHpZVWJNUTdsMDg; kmtx_sync=1549189590302943053; _gat=1; __cf_bm=fuvi_Pwkpld_e9ql6eNhZRmC8UifpPQ1AzqhC6fg97o-1647187891-0-Ae/a8zvmGhHGZzA3CmSPmMzq5ZnY/v5KrLnFiyI5LEaeP4PgGe1GAohQTFVcq3Q4wFbZtRHNPSfb22pgvpdkjSWZJ1OSAiTTQsok6KGMPBhkfuUpaEbp63syFFbwTTn7NQjHqLYvBoXCetTDTAnfKuvfa+aP0FSXgsE8Ron1dJCw; kmtx_sync_pi=0fda0a09-29b7-47a6-8b47-424be8ec92ae",
    }

    url = "https://www.hochschulkompass.de/studium/studiengangsuche/erweiterte-studiengangsuche/search/1/studtyp/3.html"

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    pagination_count = soup.find("ul", class_="pagination").find_all("li")[-2].text.strip()
    return int(pagination_count)


def gather_data(pagination):
    with open("./project_11_async/data.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                "Studiengang",
                "Hochschule",
                "Abschluss",
                "Studienform",
                "Studienort",
                "Studientyp",
                "url"
            )
        )
    headers ={
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "cookie": "INGRESSCOOKIE=1647184774.026.241327.874768; checkedSwitchClone=1; fuel_csrf_token=58497b1df63fcfa497a84f7626575d38f5fcea9927edcf866be331170ff4fa822d04bb606b8db0abf31fab5a1a47477b820b972d92f51fb22b8843c02ce1d703; fuelrid1=7NxstXN7se0k6bwPltT3yHXE_7ipfDHPH720Dq8dhNHpQGLQfOkpkXgg5zjPGiTx9kxqWEZ1iO01Eos8WZmCqHM3OXJzZ3J3bWk4b1hLNFlubXJqcVBRcy1aT21RNXo1U3oyYVNVUkhma1E; clientCode=881101; drv=rds; kmtx_sync=1549189590302943053; _ga=GA1.2.1111548562.1647184837; _gid=GA1.2.1215085130.1647184837; ui=2; fueldid=T-HiCD-f24MeGEf8KXSk0iR9slOuDhP9-pElj5ddFbqZ1MegtY7Ydp3G1lbG2rk11CoUjTQl8_8YDah-klMKpDlZSW5kTFdsT3JQbHdDTWVROHZVd0FhQVFwWU9VTzY3bHpZVWJNUTdsMDg; kmtx_sync=1549189590302943053; _gat=1; __cf_bm=fuvi_Pwkpld_e9ql6eNhZRmC8UifpPQ1AzqhC6fg97o-1647187891-0-Ae/a8zvmGhHGZzA3CmSPmMzq5ZnY/v5KrLnFiyI5LEaeP4PgGe1GAohQTFVcq3Q4wFbZtRHNPSfb22pgvpdkjSWZJ1OSAiTTQsok6KGMPBhkfuUpaEbp63syFFbwTTn7NQjHqLYvBoXCetTDTAnfKuvfa+aP0FSXgsE8Ron1dJCw; kmtx_sync_pi=0fda0a09-29b7-47a6-8b47-424be8ec92ae",
    }
    url = "https://www.hochschulkompass.de/studium/studiengangsuche/erweiterte-studiengangsuche/search/1/studtyp/3/view/wide.html?tx_szhrksearch_pi1%5Bresults_at_a_time%5D=10"


    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    results = soup.find("table", id="wideViewTable").find("tbody").find_all("tr")
    for result in results:
        result_url = "https://www.hochschulkompass.de" + result.get("data-link")
        result_info = result.find_all("td")
        result_title = result_info[0].text.strip()
        result_2 = result_info[1].text.strip()
        result_3 = result_info[2].text.strip()
        result_4 = result_info[3].text.strip()
        result_5 = result_info[4].text.strip()
        result_6 = result_info[5].text.strip()
        with open("./project_11_async/data.csv", "a", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    result_title,
                    result_2,
                    result_3,
                    result_4,
                    result_5,
                    result_6,
                    result_url
                )
            )

    # for i in range(1, pagination +1):
    #     url = "https://www.hochschulkompass.de/studium/studiengangsuche/erweiterte-studiengangsuche/search/1/studtyp/3/pn/{i}.html"

    
def main():
    pagination_count = take_pagination_count()
    gather_data(pagination_count)


if __name__ == "__main__":
    main()