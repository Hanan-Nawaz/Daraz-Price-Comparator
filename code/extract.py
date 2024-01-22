from daraz_scraper import daraz_scraper
from telemart_scraper import telemart_scraper

class extract:

    daraz_url = "https://www.daraz.pk/catalog/?q="
    telemart_url = "https://www.telemart.pk/search?query="

    def __init__(self, query_parameter):
        self.query_parameter = query_parameter

    def extracting(self):
        #calling daraz scraper class and creating object
        daraz_main_scraper = daraz_scraper(self.daraz_url, self.query_parameter)
        daraz_main_scraper.scrape()

        #calling telemart scraper class and creating object
        telemart_main_scraper = telemart_scraper(self.telemart_url, self.query_parameter)
        telemart_main_scraper.scrape()

