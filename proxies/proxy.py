import requests
import pickle
from bs4 import BeautifulSoup
import lxml


def get_free_proxies():
    url = "https://free-proxy-list.net/"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "cookie": "_ga=GA1.2.1869351866.1646671961; _gid=GA1.2.485252650.1646812048; _gat=1"
    }
    req = requests.get(url=url, headers=headers)
    response = req.text
    proxies_list = []
    soup = BeautifulSoup(response, "lxml")
    ips_table = soup.find("table", class_="table-striped").find_all("tr")[1:]
    for row in ips_table:
        tds = row.find_all("td")
        if tds[6].text == "yes":
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies_list.append(host)
    with open("./proxies/proxies.txt", "wb") as file:
        pickle.dump(proxies_list, file)
    print("Proxy file have been updating")
            

if __name__ == "__main__":
    get_free_proxies()
    