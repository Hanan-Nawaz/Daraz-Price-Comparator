# Laptop Scraper

Welcome to the Laptop Scraper repository! This project automates the process of searching and comparing laptop prices on popular e-commerce platforms Amazon and Daraz. Utilizing Python, Requests, BeautifulSoup, and Airflow, it streamlines the task of finding affordable laptops.

<img src="/process-imgs/laptop-scraper-logo.gif" width="100%" height="400px" />

## Overview

<img src="/process-imgs/laptop-scraper-process.jpg" width="100%" height="400px" />

### Core Features

1. **Dynamic E-commerce Search**: After user input, Initiate a Laptop search on Amazon and Daraz.

2. **Automated Price Comparison**: The scraper automates laptop searches and compares prices across multiple listings.

3. **Airflow Workflow**: Integrated with Apache Airflow for scheduled and automated execution.

4. **Data Storage**: Extracted laptop details and prices are stored in a structured format.

## Project Process

This repository contains the code and configuration for the Laptop Scraper project. The workflow involves initiating a search on e-commerce platforms, extracting first page laptop details, and comparing prices. The process is orchestrated using Airflow for automation.

### 1. E-commerce Search

- User enter its desired laptop name, Initiating a Laptop search on Amazon and Daraz (Only first page).

### 2. Web Scraping

- Python scripts leverage Requests and BeautifulSoup for web scraping to extract laptop details and prices from both platforms.

### 3. Data Comparison (ETL)

- Extracted data is compared to identify the laptop with the lowest price.
- We compare data of both platforms, Converting Currency and other relevant parameters and store in MongoDb.

### 4. Airflow Integration

- Airflow is configured to automate the entire process at scheduled intervals.

## Technology Stack

- **Web Scraping**: Python (Requests, BeautifulSoup)
- **Automation**: Apache Airflow
- **Data Storage**: Structured format for extracted data (MongoDb)

## File Structure

- `laptop_scraper/`: Contains the code and configuration for the Laptop Scraper project.
  - `process-imgs/`: Contains helping images related to the project.
    - `laptop-scraper-logo.jpg`: Logo image for the project.
    - `laptop-scraper-process.jpg`: Process/Roadmap image for the project.
  - `main.py`: Contains code, generally calling other classes.
  - `code/`: Conatins all the code files.
    - `amazon_scraper.py`: Conatins code to scrape from Amazon.
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
