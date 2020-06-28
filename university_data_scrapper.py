#Import the necesary libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_universities_in_Nigeria'

def scrapper():
    # Get data from website usring the request library
    web_data = requests.get(url)
    # Create a Beautiful soup object to search and clean data
    soup = BeautifulSoup(web_data.content, parser = 'lxml', features= 'lxml')
    
    # Create a variable to store a list of every row data
    row_data =  []
    
    for items in soup.find_all('tr'):
        cell_data = []
        for val in items.find_all('td'):
            cell_value = val.text
            cell_data.append(cell_value.replace('\n', ' '))
        row_data.append(cell_data)
    #print(row_data)
    
    uni_data = pd.DataFrame(row_data[1:], columns= ['Name', 'State', 'Abbreviation', 'Location', 'Funding', 'Founded' ])
    #print(uni_data.head(25))
    uni_data.to_csv('University Data.csv', index= False)
    #print()
      



scrapper()
