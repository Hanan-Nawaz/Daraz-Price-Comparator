import requests
from bs4 import BeautifulSoup as Bsoup

class telemart_scraper:
    def __init__(self, url, parameter):
        self.url = url
        self.parameter = parameter

    def scrape(self):
        url_updated = f'{self.url}{self.parameter.replace(" ", "%20")}'     
        print(url_updated)   
        response = requests.get(url_updated)
        print(response)
        if response.status_code in (200, 503):
            body = response.text
            print(body)
        else:
            print('error')


scraper = telemart_scraper("https://www.telemart.pk/search?query=", "macbook pro 2021")
scraper.scrape()