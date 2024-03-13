import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

response = requests.get(url)
# print(response)

soup = BeautifulSoup ( response.content , "html.parser" )

table_1 = soup.find('table', class_ = 'wikitable sortable')
# print(table_1)

world_titles = table_1.find_all('th')
# print(world_titles)
world_table_titles = [title.text.strip() for title in world_titles]
# print(world_table_titles)

import pandas 
df = pandas.DataFrame(columns = world_table_titles)
# print(df)

column_data = table_1.find_all('tr')[1:]
# print(column_data)

for row in column_data:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    # print(individual_row_data)
    length = len(df)
    df.loc[length] = individual_row_data
    
# print(df)

df.to_json(r'F:\Fianarana\inclusiv\python\scraping\companies.json', index = False)


