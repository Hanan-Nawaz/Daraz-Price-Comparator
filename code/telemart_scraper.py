from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

class telemart_scraper:
    def __init__(self, url, parameter):
        self.url = url
        self.parameter = parameter

    def scrape(self):
        url_updated = f'{self.url}{self.parameter.replace(" ", "%20")}'     
        print(url_updated)   
        
        browser = webdriver.Chrome()
        browser.get(url_updated)
        browser.maximize_window()

        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="grid grid-cols-12 border-t"]'))) 
        print(element)
