from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Edge("C:\Users\DELL LAPTOP\Desktop\webscrapproject\msedgedriver.exe")
browser.get(START_URL)

time.sleep(10)

dwarf_stars_data = []

def scrape_more_data(hyperlink):
    print(hyperlink)
stars_df_1 = pd.read_csv("updated_scraped_data.csv")


for index, row in stars_df_1.iterrows():

     


    print(f"Data Scraping at hyperlink {index+1} completed")

print(dwarf_stars_data)

scraped_data = []

for row in dwarf_stars_data:
    replaced = []


    
    scraped_data.append(replaced)

print(scraped_data)

headers = ["planet_type","discovery_date", "mass", "planet_radius", "orbital_radius", "orbital_period", "eccentricity", "detection_method"]

new_planet_df_1 = pd.DataFrame(scraped_data,columns = headers)

new_planet_df_1.to_csv('new_scraped_data.csv', index=True, index_label="id")
