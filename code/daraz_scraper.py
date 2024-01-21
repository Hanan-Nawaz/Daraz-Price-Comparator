import requests
from bs4 import BeautifulSoup as Bsoup

class daraz_scraper:
    def __init__(self, url, parameter):
        self.url = url
        self.parameter = parameter

    def scrape(self):
        url_updated = f'{self.url}{self.parameter.replace(" ", "+")}'     
        print(url_updated)   
        response = requests.get(url_updated)
        print(response)
        if response.status_code in (200, 503):
            body = response.text
            print(body)
        else:
            print('error')


scraper = daraz_scraper("https://www.daraz.pk/catalog/?q=", "macbook pro 2021")
scraper.scrape()