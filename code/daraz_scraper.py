from selenium import webdriver
from selenium.webdriver.common.by import By

class daraz_scraper:

    e_path = r'C:\chromedriver\chromedriver.exe'

    def __init__(self, url, parameter):
        self.url = url
        self.parameter = parameter

    def scrape(self):
        url_updated = f'{self.url}{self.parameter.replace(" ", "+")}'     
        print(url_updated)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--webdriver={self.e_path}')
        chrome_options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(options=chrome_options)   
        browser.get(url_updated)

        product_divs = browser.find_elements(By.XPATH, '//div[@class="gridItem--Yd0sa"]')
        for product_div in product_divs:
            print(product_div.text)
