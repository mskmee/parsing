from ast import Raise
from urllib import response
import requests
from bs4 import BeautifulSoup
import lxml
from time import sleep


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6"
}


def test_request(url, headers, retry=5):
    try:
        response = requests.get(url=url, headers=headers)
        print(f"{url} | {response.status_code}")
    except Exception as e:
        if retry:
            sleep(3)
            print(f"[INFO] retry={retry} => url = {url}")
            return test_request(url=url, headers=headers, retry=(retry - 1))
        else:
            Raise
    else:
        return response


def main():
    try:
        test_request(**params)
    except Exception as ex:
        print(ex)
        continue


if __name__ == "__main__":
    main()