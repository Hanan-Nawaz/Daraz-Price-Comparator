
import sys
sys.path.append("/Users/HananNawaz/Documents/LaptopScraper/code")

from extract import extract

query_parameter = input('Enter name of Laptop.... : ')

extract_ = extract(query_parameter)
extract_.extracting()

print(query_parameter)