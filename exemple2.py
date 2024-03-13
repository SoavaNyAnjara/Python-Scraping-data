from bs4 import BeautifulSoup 
import requests
import pandas

url = 'https://fr.wikipedia.org/wiki/Les_Douze_Coups_de_midi'
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

table_master = soup.find('table', class_ = 'center')
# print(table_master)

title_master = table_master.find_all('th')

all_title_master = [title.text.strip() for title in title_master]
# print(all_title_master)

df = pandas.DataFrame(columns = all_title_master)
# print(df)

column_data = table_master.find_all('tr')[1:]
# print(column_data)

for row in column_data:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    # print(individual_row_data)    
    length = len(df)
    df.loc[length] = individual_row_data

print(df)
df.to_csv(r'F:\Fianarana\inclusiv\python\scraping\maitres_de_midi.csv')