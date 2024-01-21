# Laptop Scraper

Welcome to the Laptop Scraper repository! This project automates the process of searching for and comparing laptop prices on popular e-commerce platforms like Amazon and Daraz. Utilizing Python, Requests, BeautifulSoup, and Airflow, it streamlines the task of finding affordable laptops.

<img src="/laptop_scraper/process-imgs/laptop-scraper-logo.jpg" width="100%" height="300px" />

## Overview

<img src="/laptop_scraper/process-imgs/laptop-scraper-process.jpg" width="100%" height="300px" />

### Core Features

1. **Dynamic E-commerce Search**: Users input laptop specifications, initiating a search on Amazon or Daraz.

2. **Automated Price Comparison**: The scraper automates laptop searches and compares prices across multiple listings.

3. **Airflow Workflow**: Integrated with Apache Airflow for scheduled and automated execution.

4. **Data Storage**: Extracted laptop details and prices are stored in a structured format.

## Project Process

This repository contains the code and configuration for the Laptop Scraper project. The workflow involves initiating a search on selected e-commerce platforms, extracting relevant laptop details, and comparing prices. The process is orchestrated using Airflow for automation.

### 1. E-commerce Search

- Users provide input criteria for the desired laptop (e.g., brand, specifications).

### 2. Web Scraping

- Python scripts leverage Requests and BeautifulSoup for web scraping to extract laptop details and prices.

### 3. Data Comparison

- Extracted data is compared to identify the laptop with the lowest price.

### 4. Airflow Integration

- Airflow is configured to automate the entire process at scheduled intervals.

### 5. Data Storage

- MongoDb is used to Store Transformed Data.

<img src="/laptop_scraper/process-imgs/laptop-scraper-ERD.png" width="100%" height="590px" />

## Technology Stack

- **Web Scraping**: Python (Requests, BeautifulSoup)
- **Automation**: Apache Airflow
- **Data Storage**: Structured format for extracted data (MongoDb)

## Repository Structure

- `laptop_scraper/`: Contains the code and configuration for the Laptop Scraper project.
  - `laptop-scraper-logo.jpg`: Logo image for the project.
  - `laptop-scraper-workflow.png`: Workflow image for the project.
- `README.md`: You are here, providing an overview of the project.

## Getting Started

To replicate this project, follow these steps:

1. Configure input criteria for the desired laptop.

2. Run the Python scripts for web scraping and data comparison.

3. Optionally, integrate with Airflow for automated and scheduled execution.

Feel free to explore the project directory for more details on implementation and configuration.

## Contributors

- [Abdul Hanan Nawaz](https://www.github.com/Hanan-Nawaz) 

## License

This project is licensed under the [MIT License](LICENSE).

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://hanannawaz.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abdulhanan0/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/HananNawaz0/)

<h3 align="left">Let's Talk about your project 😃 </h3>
<p align="center">
<a href="https://www.upwork.com/freelancers/~yourupworkprofile"><img src="https://img.shields.io/badge/-Abdul%20Hanan%20Nawaz-6fda44?style=flat&logo=upwork&logoColor=white"/></a>
<a href="https://www.fiverr.com/yourfiverrprofile"><img src="https://img.shields.io/badge/-Abdul%20Hanan%20Nawaz-00b22d?style=flat&logo=Fiverr&logoColor=white"/></a>
