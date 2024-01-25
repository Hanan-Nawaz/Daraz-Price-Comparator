from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class daraz_scraper:
    e_path = r'C:\chromedriver\chromedriver.exe'

    def __init__(self, url, parameter, country):
        self.url = url
        self.parameter = parameter
        self.country = country

    def scrape(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument(f'--webdriver={self.e_path}')

        chrome_options.add_experimental_option("detach", True)
        browser = webdriver.Edge(options=chrome_options)
        
        url_updated = f'{self.url} {self.parameter.replace(" ", "%20")}&sort=popularity&service=OS'

        browser.get(url_updated)
        browser.maximize_window()
        
        with open(f'daraz_data_{self.country}.csv', 'w', encoding='UTF-8') as daraz_file:
            print('Scraping from Daraz -', self.country)
            daraz_file.write('name,price,rating,link' + '\n')
            products = browser.find_elements(By.XPATH, '//div[@class="gridItem--Yd0sa"]')

            for product in (products):

                product_name = product.find_element(By.XPATH, './/div[@class="title-wrapper--IaQ0m"]')
                product_price = product.find_element(By.XPATH, './/span[@class="currency--GVKjl"]')

                rating_ = ''
                try:
                    product_rating = product.find_element(By.XPATH, './/span[@class="ratig-num--KNake rating--pwPrV"]')
                    rating_ = product_rating.text
                except NoSuchElementException:
                    rating_ = 'N/A'
                

                product_link = product.find_element(By.XPATH, './/a[@id="id-a-link"]')
                

                formated_line = f'{product_name.text.replace(",", "")},{product_price.text.replace(",", "")},{rating_},{product_link.get_attribute("href")}'

                daraz_file.write(formated_line + '\n')

        browser.close()
