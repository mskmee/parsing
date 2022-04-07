from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "D:\python_projects\selenium\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.set_window_size(800, 600)

link = False
while not link: 
    while True:
        try:
            driver.get("https://lays.ua/kinopodarunki?vid=462044246&auth_hash=278c3f3f185f3c1be77adacae77cd8a7")
            link = True
            break
        except:
            time.sleep(3)
            break
        
serch_item = driver.find_element_by_id("kinogift5_mob_page")
serch_item.click()
code_order = driver.find_element_by_xpath('//*[@id="mob_kp4_popup"]/div[2]/div/div[2]/div[3]')
code_order.click()