import asyncio
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
import aiohttp
import json
import codecs
import os
from time import sleep


SCROLL_PAUSE = 0.5 
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

def get_html():
    """Open selenium chrome driver and save full load html"""
    chrome_driver_path = 'D:\python_projects\selenium\drivers\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=chrome_driver_path)

    driver.get(url="https://spb.zoon.ru/medical/")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    
    page_data = os.path.join("D:\python_projects\selenium", "data.html")
    file = codecs.open(page_data, "w", "utf-8")
    driver_data = driver.page_source
    file.write(driver_data)
    driver.close()
    
    
if __name__ == "__main__":
    get_html()


