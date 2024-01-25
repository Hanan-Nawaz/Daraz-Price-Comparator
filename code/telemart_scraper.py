from selenium.webdriver.common.by import By
from selenium import webdriver

class telemart_scraper:
    e_path = r'C:\chromedriver\chromedriver.exe'

    def __init__(self, url, parameter):
        self.url = url
        self.parameter = parameter

    def scrape(self):
        url_updated = f'{self.url}{self.parameter.replace(" ", "%20")}'     
        print(url_updated)   
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--webdriver={self.e_path}')
        chrome_options.add_experimental_option("detach", True)
        browser = webdriver.Chrome(options=chrome_options)
        browser.get(url_updated)
        browser.maximize_window()

        elements = browser.find_elements(By.XPATH, '//div[@class="grid grid-cols-12 border-t"]')
        for element in elements:
            print(element.text)
