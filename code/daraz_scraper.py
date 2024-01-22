from selenium import webdriver
from selenium.webdriver.common.by import By

class daraz_scraper:
    def __init__(self, url, parameter):
        self.url = url
        self.parameter = parameter

    def scrape(self):
        url_updated = f'{self.url}{self.parameter.replace(" ", "+")}'     
        print(url_updated)
        browser = webdriver.Chrome()   
        browser.get(url_updated)

        product_divs = browser.find_elements(By.XPATH, '//div[@class="gridItem--Yd0sa"]')
        for product_div in product_divs:
            print(product_div.get_attribute('a'))
