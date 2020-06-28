#Import the necesary libraries
import pandas as import pd
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_universities_in_Nigeria'

def scrapper():
    web_data = requests.get(url)
    print(web_data)



scrapper()
