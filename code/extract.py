from daraz_scraper import daraz_scraper

class extract:

    daraz_url = ["https://www.daraz.pk/catalog/?q=", "https://www.daraz.lk/catalog/?q=", "https://www.daraz.com.bd/catalog/?q=",
                 "https://www.daraz.com.np/catalog/?q="]
    
    daraz_country = ["Pakistan", "SriLanka", "Bangladesh", "Nepal"]

    def __init__(self, query_parameter):
        self.query_parameter = query_parameter

    def extracting(self):
        #calling daraz scraper class and creating object
        for i in range(4):

            daraz_main_scraper = daraz_scraper(self.daraz_url[i], self.query_parameter, self.daraz_country[i])
            daraz_main_scraper.scrape()

