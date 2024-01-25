# E-commerce Price Comparator🌐🛍️

Welcome to the E-commerce Price Comparator repository! 🌐🛍️ This project automates the search and comparison of prices across various products on leading platforms Telemart and Daraz in Pakistan🇵🇰. Using Python, Requests, BeautifulSoup, and Airflow, it simplifies the task of finding budget-friendly deals. Shop smartly with this efficient tool!

<img src="/process-imgs/ecommerce-product-comparator-logo.gif" width="100%" height="400px" />

## Overview

<img src="/process-imgs/ecommerce-product-comparator-process.png" width="100%" height="400px" />

### Core Features

1. **Dynamic E-commerce Search**: After user input, Initiate a Product search on Telemart and Daraz.

2. **Automated Price Comparison**: The scraper automates Product searches and compares prices across multiple listings.

3. **Airflow Workflow**: Integrated with Apache Airflow for scheduled and automated execution.

4. **Data Storage**: Extracted Product details and prices are stored in a structured format.

## Project Process

This repository contains the code and configuration for the E-commerce Price Comparator🌐🛍️ project. The workflow involves initiating a search on e-commerce platforms, extracting first page product details, and comparing prices. The process is orchestrated using Airflow for automation.

### 1. E-commerce Search

- User enter its desired product name, Initiating a Product search on Telemart and Daraz (Only first page).

### 2. Web Scraping

- Python scripts leverage Requests and BeautifulSoup for web scraping to extract product details and prices from both platforms.

### 3. Data Comparison (ETL)

- Extracted data is compared to identify the Product with the lowest price.
- We compare data of both platforms, Converting Currency and other relevant parameters and store in MongoDb.

### 4. Airflow Integration

- Airflow is configured to automate the entire process at scheduled intervals.

## Technology Stack

- **Web Scraping**: Python (Requests, BeautifulSoup)
- **Automation**: Apache Airflow
- **Data Storage**: Structured format for extracted data (MongoDb)

## File Structure

- `ecommerce-product-comparator/`: Contains the code and configuration for the E-commerce Price Comparator🌐🛍️ project.
  - `process-imgs/`: Contains helping images related to the project.
    - `ecommerce-product-comparator-logo.jpg`: Logo image for the project.
    - `ecommerce-product-comparator-process.jpg`: Process/Roadmap image for the project.
  - `main.py`: Contains code, generally calling other classes.
  - `code/`: Conatins all the code files.
    - `telemart_scraper.py`: Conatins code to scrape from Telemart.
    - `daraz_scraper.py`: Conatins code to scrape from Daraz.
    - `extract.py`: Contains code to call both scrapers.
    - `transform.py`: Contains code to implement Extract, Transform and Load.
    - `load_to_mongodb.py`: Conatins code to load data into MongoDb using PyMongo.
  - `README.md`: You are here, providing an overview of the project.

## Getting Started

To replicate this project, follow these steps:

1. Clone this project.

2. Run the Python scripts for web scraping and data comparison.

3. Optionally, integrate with Airflow for automated and scheduled execution.

4. The naming convention i use is `snaking case`.

Feel free to explore the project directory for more details on implementation and configuration.

## Contributors

- [Abdul Hanan Nawaz](https://www.github.com/Hanan-Nawaz) 

## License

This project is licensed under the [MIT License](LICENSE).

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://hanannawaz.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abdulhanan0/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/HananNawaz0/)
