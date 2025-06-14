# Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

# Problem Statement:
The "Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.

## <p align="left">
  <img src="https://github.com/user-attachments/assets/78139eea-d1fe-458c-945c-14c716c739db" width ='100'></p> 
# WEB SCRAPING:
  * I scrapped the datas of 10 state transport corporation buses including the private buses by using automation tool called selenium and store it in seperate csv files.

# <p align="left">
  <img src="https://github.com/user-attachments/assets/c34e4e9a-e83e-482e-b6c5-af6043fbcbfc" width ='100'></p>
# DATA PREPROCESSING:
 * I convert the csv files into dataframe and concat them into single dataframe.
 * I impute the null values in star Rating column by using mean method.

# <p align="left">
  <img src="https://github.com/user-attachments/assets/38f1e83a-9a60-4fb1-8815-391f0e75718f" width ='100'></p>
# SQL DATABASE: 
 * Then I store the dataframe in MYSQL database by creating table and store the values by using sql alchemy.

# STREAMLIT:
 * I create a dynamic filtering web browser by using streamlit with mysql queries to retrieve the data .
 * If the selectors select the State , then based on the state it will show the buses route name.
 * If we select the routename and click the button, then it will shows the bus information from higher star ratings to lower.

   


